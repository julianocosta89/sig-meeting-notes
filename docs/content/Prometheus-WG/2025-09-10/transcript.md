SIG: Prometheus WG
Date: 2025-09-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Juraj Michalek 00:02:18 Hey, everyone.
GZ Gregor Zeitlinger 00:03:44 Hello.
Juraj Michalek 00:03:47 Hey.
GZ Gregor Zeitlinger 00:04:35 Owen, do you feel like adding the recent discussion around a translation strategy, or is this already discussed enough?
Owen Williams (he/she) 00:04:44 I think we've sort of mostly discussed it enough. I just had a good one-on-one with Bjorn sort of talking through some of it, and I think… I think it makes sense to have
you know, a bid on it at the next online dev summit. I mean, I'm happy to… I'm also happy to talk about it here, if people want.
Juraj Michalek 00:05:13 Let's see if Arthur's gonna join, since his first topics… the first two topics are his.
I'm gonna… Drinking.
May have Artemed.
Arthur Silva Sens 00:06:09 Hello.
Juraj Michalek 00:06:14 Since the first topic is yours, do you want to start?
Arthur Silva Sens 00:06:20 And, I was in another meeting, I'm still opening stuff.
Juraj Michalek 00:06:23 No worries.
Arthur Silva Sens 00:06:36 Okay, yes, I can start.
Let me remember… Oh, okay.
So… Recently, this week, the collector Sick, reached out to me.
Asking if the A1… like, some context first.
every single renovate PR that upgrades Prometheus Libraries fails.
It doesn't pass the CI, first try.
Based on that, the collector sick asks if we prefer to remove the Prometheus
upgrades from the… from Renovate. So we do them manually.
Instead of, like.
We need to jump on PR, saying, please don't merge this, because we need to figure out some other stuff first.
I… So I told them to wait, that I would bring this topic to this group.
And see what you think, like…
Do you prefer that we do manual, like, every upgrade should be done manually by us, or should we…
Juraj Michalek 00:07:45 I mean…
Arthur Silva Sens 00:07:46 Does he have hopes that…
Juraj Michalek 00:07:50 Isn't it that what it ends in anyway, basically?
Arthur Silva Sens 00:07:57 Yeah, yeah, somehow it does.
It feels a little bit stressful to…
like, hunt PRs and tell them, please don't merge this.
Juraj Michalek 00:08:08 Then, I guess my only question is really…
Okay, who's gonna do it then? Who's gonna remember to do it?
Arthur Silva Sens 00:08:16 sub to us?
I can easily remember to do it. I don't want to do everything by myself, but I can easily remember, hey, Prometus was just baited.
We should open a PR.
Juraj Michalek 00:08:30 You can also have something drop a message in the hotel Prometheus channel, right? With releases, like, subscribe to the releases of Prometheus.
And be like, I guess… and then just potentially discuss, like, in the thread of that, like.
And he volunteers to do this one.
Arthur Silva Sens 00:08:46 That is actually a very good idea.
Juraj Michalek 00:08:47 Should we then, if nobody's against this approach, right?
Should we then document, like, how to, like, do a couple of these upgrades and then write it down, somewhere?
I don't know where, somewhere, right? So, like, when somebody else is like, okay, can I try this one so they have a document to follow?
GZ Gregor Zeitlinger 00:09:11 Is it not possible to just fix the process so that it's done automatically?
Arthur Silva Sens 00:09:18 The problem is that every time you progress something, something breaks.
So it's not just… the problem is not automating the merge. The problem is…
Understanding what changed, what broke, and fixing.
Juraj Michalek 00:09:33 Yep.
No, I mean… Yep.
GZ Gregor Zeitlinger 00:09:36 the PR to renovate would fail.
I still don't understand why this is a problem, then you would see that there's a failing PR, and then you fix it.
Arthur Silva Sens 00:09:46 They're… like, usually the fails are flaky.
Oh, yeah. Yes.
GZ Gregor Zeitlinger 00:09:54 Okay.
Okay, then I understand that this is… A can of worms.
Juraj Michalek 00:10:00 To be fair, I saw even… saw Fred even somewhere, I don't know who was pinged there, that we broke Kubernetes to recently.
Arthur Silva Sens 00:10:08 Yeah, it was, upgrading common.
Juraj Michalek 00:10:10 What is…
Arthur Silva Sens 00:10:11 A similar problem, different… Different people.
krajo Krajcsovits 00:10:16 By the way, I mean…
Renovate, I guess, has some feature, too.
Vital stuff, to…
Or otherwise to, you know, prevent automatic updates, right? Does it have a feature to actually
have some custom message on the PR that it creates, because that could be enough to
just say in the PR that, you know, don't do this yourself, and then if the message also at us, it mentions us, then that's a kind of thing.
Juraj Michalek 00:10:51 There's some templating you can do.
Arthur Silva Sens 00:10:54 We are pinged, like, we… like, if the coach touches any of the components, like, we are pinged because we are code out.
krajo Krajcsovits 00:11:02 Yeah. Yeah, I'm not following my guitar notification, that's close, because I have too many. So I just do, basically, triage and open the…
thing and look at it every week or two weeks. Okay, yeah, I see.
Arthur Silva Sens 00:11:16 But how do you like about URI's idea? Like, we tell them to remove from renovate, and we have some automation in Slack.
Yeah, that's much… I mean…
krajo Krajcsovits 00:11:28 The one thing I want to avoid is having a single point of failure, which would be you. You know, what happens if a tram hits you, or something? You know, that doesn't work.
Juraj Michalek 00:11:37 It's called Bus Factor of 1.
krajo Krajcsovits 00:11:40 Yeah.
So, yeah, I would be fine with that. I do see strike notifications.
Arthur Silva Sens 00:11:48 I'll suggest that, then.
Juraj Michalek 00:11:51 I think you can just, like…
GitHub pages… GitHub releases, right? They have an RSS feed, so you can use Slack to subscribe to that RSS feed. I don't know if that is enough for this use case.
So you can just subscribe to the RSS feed of releases of Prometheus, and
other couple of repos that this Tetris.
That's how we kept up-to-date Prometheus in my previous trips, until we stopped using it.
Arthur Silva Sens 00:12:24 Awesome, I'll look into that then.
The other one is…
somewhat the other way around, like, another suggestion that they made is that we run the collector tests in Prometheus, or are there…
other projects that the collector uses, for example, OTLP translator, client calling.
The idea is not that if the test fails, we should block the PR, but just to make us aware in advance.
What do you think about this?
GZ Gregor Zeitlinger 00:13:16 Do we have any end-to-end tests right now?
Arthur Silva Sens 00:13:23 Which end-to-end tests? Like, what, what entities?
GZ Gregor Zeitlinger 00:13:31 Because you were saying, that we don't have end-to-end tests.
Arthur Silva Sens 00:13:36 I mean, like, when we do a PR in Prometheus, Prometheus.
The suggested automation is that we clone the collector repository We do replaces in GoMods.
And we run the Prometheus receiver, Prometheus exporter, Prometheus remote write exporter tests in the Prometheus CI.
Owen Williams (he/she) 00:14:00 Right. Is the… are we surprised when we…
break the collector? I mean, for instance, like, this recent one in common, like, we had a breaking change, we put it in the release notes, so it's like, yeah, we knew we were gonna break people, so it's not like… and usually.
That implies you could do something in Prometheus to fix the problem, but usually it's, like, the other project needs to update their… I… yeah, I'm just not sure what this gets us.
Arthur Silva Sens 00:14:26 We were surprised a few times. For example, this change in config that now needs to call a load.
There's a…
like, in the past, we could just create a config file and use it, but now Prometus requires that once you have a config file struct, you need to call a function called load.
And this load will toggle a Boolean that is private.
in Prometheus, and then we can use them. This is something that Bartek did… I don't remember why.
But that broke us in the collector, and it was quite hard to fix it.
I don't think we have a clean solution still, like, we are still working around it.
GZ Gregor Zeitlinger 00:15:15 So, I have made good experience with end-to-end tests, and I'm the maintainer of one project that allows such an end-to-end test. Not saying that this has to be used, but it has spotted
Couple of issues that have not been spotted in,
collector. That is what… that was the recent one, but also in SDK, so it has helped us a couple of times.
But other people have their hands raised, sorry for that, didn't see that.
Kyle Eckhart 00:15:43 That's okay, I wasn't sure. I was gonna ask, like, is there a level of expectation around configuration, like,
stability, right? Like…
Because then, like, having that inverse dependency feels a little bit awkward. If there are certain APIs within Prometheus that are expected to stay stable, like, having concrete tests that prove that is really good, but…
you know, if people are gonna reach into Prometheus, Prometheus, and depend upon something, there's gotta be a level of, like, okay, like, that's on you.
Arthur Silva Sens 00:16:14 Yep.
Okay, may I… answer, or…
Okay, yeah. So there is no guarantee on Prometus API, we don't promise anything, we are free to do whatever we want, we don't want people to depend on the Go code.
Owen Williams (he/she) 00:16:36 Yeah, so my point is sort of, like,
So yeah, Prometheus makes a change. In this case, it was…
needed to make sure the config was more robust. It's gonna require a change from everybody
calling that code, which is what Hotel Collector is doing.
when that… if we had this test, it would break, and we'd be like, yup, it breaks, collector will need to update their code, what do we do? There's no action there. We're not gonna change what we're doing in Prometheus, this is a change we need to do.
And then, next time.
collector updates Prometheus, it will break in the way that we expect. So, I don't… I don't see what the difference is, unless what
the OTEL people are hoping is that instead of their automated wonderfulness automatically working, and then it breaks, and then they don't know what to do, that we are jumping in proactively to do the updates to Prometheus and fixing the problems for them.
In which case, I still don't know what the difference is. We can look at the automated thing that fails and fix it. They can just safely ignore that Prometheus did not update automatically. I don't understand how this is a problem for the… I don't understand how this is a problem for them.
that any of these solutions will actually fix, unless the thing that is the problem is, I don't like seeing an automated thing fail, which is…
okay, but, like, it's… that's… I want to be clear about what problem we're solving for them.
Arthur Silva Sens 00:18:17 Cryo, do you have a different question?
So I'm just gonna answer, Owen, like, I… this was not, like, them coming to us, hey, this is a problem and we need to fix.
It's like… the… They came to me saying… asking, hey, do you want to remove Prometus from Renovate?
And I answered with, I… to be honest, I want things to just pass, and not require manual integration.
And they just suggested… one idea is you could run the test in Prometheus, and I just thought, maybe that could
Maybe that could help, but we are free to ignore, it's just a suggestion.
Okay.
krajo Krajcsovits 00:19:07 Yeah, now I find the unmute button.
So, yeah, if the testing Prometheus is not required, then people will very soon learn to ignore it, and will ignore it, so it will still fall on us to look at
That.
So, in that sense, I wouldn't put it into…
if we even do it, I wouldn't put it into PRs, because it would just confuse people if it's not required. I would put it on main.
And…
Arthur Silva Sens 00:19:33 Hmm.
krajo Krajcsovits 00:19:33 we could take a look. Like…
That could be a part of triage that we do regularly, or something.
Arthur Silva Sens 00:19:44 That makes sense. If we merge your PR into main, And it fails.
the tests in Collector. We could have an automation that pinged us on the PR,
Saying, hey, just let you know, this broke, No, no action needed.
just… Be aware.
krajo Krajcsovits 00:20:05 Yeah, that's a… that's a good heads up, but, like, So, yeah.
Arthur Silva Sens 00:20:13 Oh, what?
You're, you're muted.
Owen Williams (he/she) 00:20:16 Yeah, I think that's a great idea. Okay, thanks, and thanks for clarifying the situation. Yeah, helps to understand the exact context, yeah. I mean, I think…
I think in general.
well, I was gonna say, in general, Prometheus should be able to merge automatically, but I feel like, in practice, things are… it's pretty… it's pretty active, and things are always breaking. Yeah.
I know that I've… I know I've seen on some GitHub projects that they have little badges on the front page that's like.
is the build passing? Or, you know, they got those little things. I wonder if that's a place we could surface this as kind of a mini dashboard of, like, hey, is this still working with hotel or something? As opposed to, I mean, a Slack, notification
channel is also good.
it just feels like a dashboardy thing that I want to see what the status is, and I don't know where, like, the go-to place for that would be, because that might be useful.
Arthur Silva Sens 00:21:26 Yeah, I like that idea too.
Kyle?
Kyle Eckhart 00:21:29 Does Renovate update any time there's a change, or does it update on tags? Because potentially, right, like, might be a good, interesting thing as a part of, like, the release process, as well.
Arthur Silva Sens 00:21:42 They, they would pay it on techs.
It can be done on, like, every commit, but, like, that would be just impossible.
To keep up to.
Kyle Eckhart 00:21:54 Yeah, injecting it into that process might also… I mean, obviously, it's a little bit later in the process, but at least it's a well-known, okay, this is going to happen.
Another song.
Arthur Silva Sens 00:22:13 Cool. I'm gonna… I'm gonna write a proposal with the ideas, and…
if we… if something comes up that everybody likes, let's do it. If not, we can just…
Just forget about it.
Thanks for the discussion. Next topic is, loops.
You're right.
Juraj Michalek 00:22:38 I have a few… this is… More of an…
FYI, just for… so everybody's aware, but…
I mean, Arthur, you talked about this, not necessarily sure what the outcome about it's gonna be, but basically.
there was a PR recently in the remote bread exporter, I'm not a co-donor, right, so they, I guess, shouldn't have merged it with just my approval, then somebody else approved it, who is a maintainer of,
Collector, but not a code owner of any of these components.
It… there was a bug, we didn't catch in the review,
It introduced flakiness in the test, it was later fixed, but then the fix, like, the original fix was like, okay, let's revert this, because we found pretty quickly, like, these tests started to fail after an hour, hour after this was merged.
Then they chose to, instead of reverting it, implement another fix that, again.
That was an actual proper fix, but again, got merged with a single, review from not a co-owner of any of these components, into the… into the component. So it's… it's a sort of…
a questionnaire, like… Is there anything we want to do about this, or…
Also just an FAY that this sort of happened, and yeah, so you might…
there's, like, unless we have a conversation about it, it can happen again, that they just make changes to components without the reviews of code owners. And I'll be definitely more careful in reviewing peers. Yeah, I missed a small thing that…
Beautiful.
Even though, like, my preview is sort of just non-binding right now.
Any comments or questions around this?
Owen Williams (he/she) 00:24:30 Isn't this a… isn't this a setting that you can set in GitHub to require reviews from code owners?
Juraj Michalek 00:24:38 Mmm…
Arthur Silva Sens 00:24:40 Yep.
Owen Williams (he/she) 00:24:41 Good.
Arthur Silva Sens 00:24:41 Yeah, but, like, they are… the maintainers are co-owners of everything.
Owen Williams (he/she) 00:24:46 Oh, okay.
So… So the problem here is that…
it was not the right code owner? I'm sorry, yeah.
Juraj Michalek 00:24:56 Yeah, well, like, they're technically a code owner of the whole repository, right? But nobody who is specifically a code owner slash approval for remote read exporter actually looked at it. I mean, I reviewed it, I didn't catch the mistake, but I'm not a code owner, I'm… or.
Owen Williams (he/she) 00:25:10 Yeah. Like, approver, whatever they call it in Autel.
Arthur Silva Sens 00:25:15 Yeah, for example, like, in Prometheus, we are working on making cod owners of services discoveries, right? Then we have a, like, a Prometheus team.
And then we have…
other… another group that are co-owners of Service Discovery. If a member of a Prometus team… a Prometus team member approves a PR in the Service Discovery, that would suffice
And that's exactly what happened here.
as someone that is higher level than us in the collector group approve the PR, and that counts as an approver… as an approver, even though the
The Prometheus folks didn't approve.
But, like, what can I… what can we do? Like, we were talking about how… what do we want to do in the future? Like, I don't think we have…
Any power here?
Juraj Michalek 00:26:10 I guess that's… that's fair.
Just sort of FYI, that happened.
Arthur Silva Sens 00:26:16 Kyle, Kyle has a raised hand.
Kyle Eckhart 00:26:18 Was there anything test-wise that could have been done? Because, like, it was a data race, right? Like, just following to, like, the route, because, you know, if we can't prevent people from approving
Is there better, like, more progress tests that we could put in place for something like this? Because it seems like that's the only reasonable thing that could be done.
Arthur Silva Sens 00:26:39 Yeah.
better test coverage sounds like the way to do it. Like, if the tests fail.
They wouldn't merge… wouldn't have merged.
Juraj Michalek 00:26:49 Definitely, yeah.
In the end, at least, it was caught by, like, having the runs on main, right? The moment it started to be that flaky, like, I noticed the issue.
Other people did too, right? And then we started to talk about reverting it, and then they fixed it instead.
Arthur Silva Sens 00:27:05 I think we have a serious problem with test flakness, like, we are getting pinged so much about tests being flaked lately.
Juraj Michalek 00:27:13 Yeah, even I have, like, a PR now that's…
I don't think I broke those tests, but they're failing. I'm gonna talk to you a little bit later. I think you were talking about the same thing in the Slack, but…
And it's not even specific to our components, right? I just checked the issues today, and there's, like, test flakiness being reported on, like, 2-3 other components that are not Prometheus-related.
So it just seems like…
this flakiness in the alter repo is, Cool.
Arthur Silva Sens 00:27:45 Yeah, but…
Juraj Michalek 00:27:46 Boom.
Arthur Silva Sens 00:27:46 We can keep our garden clean, and let the other…
Juraj Michalek 00:27:51 We care about them.
Yeah, I guess if that's all that topic. The other topic is, I was actually asked this yesterday, and I didn't know what to say.
So…
I guess, what would be the recommendation of even this group, right? Would we recommend interesting into Mimi or Cortex, or Prometheus via the OTL pain point?
Or would we recommend Remote Ride Exporter? Like, do we have some documentation that, like, recommends one over the other, potentially even with reasoning, why we should do one or the other?
I think there's, like…
some edge cases, like Tanos, Tanos doesn't have an LTLP endpoint, but outside of that, yeah, Kyle?
krajo Krajcsovits 00:28:40 Close the stupid mute button again.
I don't know, it's a…
I have a thread somewhere internally in Grafunnel that I want to look up what we recommend, but I think it's…
A little bit related to the use case, although we… if… if I'm, you know.
thinking from OpenTeametry, and OpenTeometry point of view, I would definitely say the hotel endpoint.
And also, at least Mimir said that it's first-class citizen, and it should work, basically perfectly.
Juraj Michalek 00:29:19 instantly.
Arthur Silva Sens 00:29:20 I guess it's just trade-offs, like, if you're doing only metrics.
I… there's… I don't see a reason… like, if you're doing only Prometus metrics, I don't see a reason to use OTLP.
Remote ride is optimized.
network… CPU just works better with the Prometheus data format.
If you're doing more than metrics, or if you're not using Prometus metrics, use OTLP.
Juraj Michalek 00:29:48 Yeah, I guess, as you said, it's kind of trade-offs. And then, yeah, Thanos, for example, I don't think… I know there was a PR to add an OTL pinpoint, I don't think it was March, though.
Arthur Silva Sens 00:29:58 It was, it was Nicholas Sakashi built it, I'm pretty sure. That was, like, almost a year ago now.
Juraj Michalek 00:30:05 Oh, cool.
I'm gonna double-check on that.
Okay. That brings, Owen's favorite topic, translation strategy.
What the hell? That's new! Zoom just asked me if I'm speaking Czech.
I don't know why, though, I am… Anyway, the… right, I'm…
continuing with my work on the remote red we to support in the Remote Red Exporter,
I do need to do two more PRs in the translation layer, and I think by now, one of the PRs I want to raise, basically, is…
I think a support for no translation strategy, at least for remote ride version 2 in the remote ride exporter, so people can actually get their metric names a year later. But the question that brings, right, is…
the Prometheus ulti endpoint in Prometheus has a translation strategy field.
That has 3 options. No UT of escaping with suffixes, underscore escaping with suffixes, and no translations, right?
But the rebuild red exporter only has one option that is a bool, that is addMetrix suffixes. And so…
The question is, what do we do with that, right? Do we…
One option would be make a braking change, right? We replace that bull with
the same options Prometheus has, and implement that with the caveat of, like.
no translation is only valid if you enable RE2.
We can do braking changes, I think I would rather avoid that, if possible.
There's also… yeah.
Owen Williams (he/she) 00:31:50 Yeah, so, so yeah, we are trying in general to move towards the translation strategy option everywhere, so OTEL Collector has it, OTEL SDK has it, and then Prometheus Endpoint in Prometheus has it, so we're trying to be…
universal about it. There are actually four, four options, not just three.
Juraj Michalek 00:32:14 Sorry, I missed the first four one.
Owen Williams (he/she) 00:32:16 Yeah, and so… ideally, yes, it would support all… all four. I'm not sure this has to be a breaking change. The only…
the… in the other systems, there's… we've sort of deprecated the previous bool, in this case, add metric suffixes, and you have to solve the question of, okay, what happens if somebody sets both of those things? In general, the correct thing to do is
Pick the newer option, so translation strategy should…
elide whatever add metric suffixes does, and maybe throw a warning, I don't know, but, like, we don't have to delete add metric suffixes as a… as an option. But that's generally the approach we're taking. And also, moving towards this enum means that in the future, if…
Somebody else needs another translation strategy, we can add it.
without creating new flags, which has been the unfortunate proliferation of Booleans, yeah.
Arthur Silva Sens 00:33:20 We had the same situation in the Prometheus Exporter. Prometheus Exporter had to add metrics to fixes. The way we did there, we added a feature flag.
That disables the existing behavior, and makes the translation strategy… A transition strategy…
does not have a feature flag to enable it. It's always there. But we have a feature flag that disables the previous
flag.
And then we are slowly removing the add metrics to fixes.
In, like, 2 or 4 releases, something like this.
Translation strategy always takes precedence, even if the other is there.
And yeah, that's… that's how we're doing. I think we can do the same in the remote ride exporter.
Juraj Michalek 00:34:12 Yeah, I think that's gonna be my thinking, just go look at what exactly is implemented into the Prometheus one, and sort of…
Borrow that.
With one caveat, right, it's, one extra thing I have to keep in mind, right? I think, at least from our remote, right, specification, it's clear that
the metric names have to be translated for Remote Red V1, so there's the other caveat that, like, in case of the remote ride exporter, at least according to the specification, I should only allow null translation, node…
If you also use email dreaded, yeah, Kyle.
Kyle Eckhart 00:34:50 Oh, I was just gonna ask a potentially dumb question, like, is there a direct translate? Like, if someone's using add metric suffixes, there's no translation strategy that's, like, a one-to-one, just because of how the translation strategy has evolved? Is that correct?
Owen Williams (he/she) 00:35:06 Say that again?
Kyle Eckhart 00:35:08 So right now, there's the iMetric suffix as if you move to the translation strategies, there's not one that you could just enable by default that's, like, the same, right? Like, there were some
Changes?
To them.
Owen Williams (he/she) 00:35:22 It's… so the underscore escaping with suffixes is the.
Juraj Michalek 00:35:29 That is… that is the default, that is the intended default, that is.
Owen Williams (he/she) 00:35:33 how… all of the specs up to now have said you should translate your OTEL names to Prometheus.
Kyle Eckhart 00:35:41 Okay.
And someone using the existing behavior, like, they would not get breaking changes from going to that, right?
Owen Williams (he/she) 00:35:49 Correct with one caveat, which is that there were inconsistencies in the way translation was being done in different projects that we have now unified.
Now we picked as our gold standard Prometheus, so I believe, yes, it should be… it should be consistent. But, like, there was a difference in whether double underscores got shrunk down to single underscores, and there was a difference with…
prefixing label names that began with an underscore with the word key, and then Hotel Go had separate options for type and unit suffixes, separately.
So, like, we are ironing all of these out to make them consistent, so I can't 100% guarantee, but it sh… because this is Prometheus, it should be the same.
Juraj Michalek 00:36:42 I think also whatever these changes would have led to has already happened in the remove that export in the first place, because that would have been done as part of the migration to the OTLIP translation package, right? Now, my changes would be just passing a different configuration to it, but it's already being used.
Owen Williams (he/she) 00:36:58 Okay, yeah, then… then that… then I could say, yes, it will not change.
Arthur Silva Sens 00:37:03 Like, we have 4 projects all doing different stuff, and now we are consolidating into one. It's just impossible that we don't break something.
Juraj Michalek 00:37:15 Yeah, we already broke things.
Owen Williams (he/she) 00:37:16 Yeah, and by the way, our solution for this was we added extra bools in those particular projects, which is like, okay, you can do translation strategy, and then your stupid other thing that you were relying on, you're fine. Because it… yet, some people are relying on the weird behavior. So… but we're trying to make sure that those
Uniquenesses are in those projects, and not.
Juraj Michalek 00:37:40 But they don't.
Owen Williams (he/she) 00:37:40 But everybody else's, yeah.
Juraj Michalek 00:37:44 I love this. Anyway… I think that's it for… yeah.
Arthur Silva Sens 00:37:51 Yurai, your next topic is quite interesting.
Juraj Michalek 00:37:56 Yeah, is it? Oh, is it the switching of the time?
Arthur Silva Sens 00:38:01 Yep.
Juraj Michalek 00:38:02 Yeah, I was just curious about this, because, like, AI switched jobs two weeks… two months ago, and now I have a… and it was originally a weekly meeting, and they made it bi-weekly, and they chose the same week this one happens, and so I haven't joined the meeting yet two months in, and I feel like maybe I should at some point?
So I was just curious if there's any trends…
Also, the other… if we could make this still bi-weekly, right? But the other week.
And then the follow-up race.
who can change it, I don't… yeah.
Like, who can update the calendar, I guess? I don't know who can update.
Arthur Silva Sens 00:38:39 Hey, this is Alolita is the owner. Maybe David Ashbold, but I'm not sure.
But I can reach out to them if the group prefers, but I… but then we need to come to an agreement what is the other time, because the other week we have open metrics.
Which is also something that is very related to this group.
Juraj Michalek 00:39:05 It's at the same time?
krajo Krajcsovits 00:39:08 No, it's earlier. I mean, Opamatrix is earlier.
Arthur Silva Sens 00:39:11 Oh, I thought the Warriors same time.
krajo Krajcsovits 00:39:15 I checked, but… that's why I wrote I still would prefer, you know, having them on different things, because
Dude.
very… they're very different contexts. I mean…
Juraj Michalek 00:39:27 The other thing, again, like, I don't know if that works for the rest of the group.
It's, like, just moving it hour… early or hour late.
If we can't move it, then it's okay too, I'll just build all that on this one at times, because I might…
Need to go to the other one at times.
And the… Reference, any suggestions?
Arthur Silva Sens 00:39:56 I, I think… You know that that is a tool…
where people can vote in times, I don't remember what the name is.
Juraj Michalek 00:40:06 I can… I can bring that, yeah, something like that for the next session, so we can find if there's another time that would work better for this group.
Arthur Silva Sens 00:40:13 I…
I don't want to just throw this link in the hotel Prometheus, because then we will have a lot of random votes from people that don't join anyway.
Juraj Michalek 00:40:22 Yeah, we can, we can just put it in the meeting notes for the next one, and vote in it.
Arthur Silva Sens 00:40:28 But not only that, but I also reached out to, at least, reached out to the people who joined the last few months, I guess.
Juraj Michalek 00:40:33 Yeah.
Yeah, like, we don't have David here, right? And he's kind of important.
Dammit.
Yeah, I can…
Arthur Silva Sens 00:40:41 Could you… could you do that?
Juraj Michalek 00:40:43 Yep.
I mean…
It's also not that hard, potentially, because out of this group, Jonathan is the only person who either cannot access their work calendar, because we all work in the same company.
But yeah, now we can, we can, like, there's, there's other people who join frequently, at least frequently enough, that also…
We might want to accommodate, so I'll handle that.
I think that's it for me and my topics.
Arthur Silva Sens 00:41:13 Right?
krajo Krajcsovits 00:41:14 Yeah, I just wanted to note…
There was a bigger change in Prometus in the OTL pinpoint, how it works.
David and myself worked on that.
And, I noticed that the…
there's a package in… in order. OpenCollectorContrib that is very similar. I don't know the history, like.
If it's intentionally very similar, it was just…
Arthur Silva Sens 00:41:40 For me to use… Prometus copied the code from Collector?
directly into Prometus, and then… People just work on that, and they eventually defer.
Juraj Michalek 00:41:51 Yep.
krajo Krajcsovits 00:41:52 Okay.
So there's no… Okay, do we want to converge them again at some point, or is it okay?
Juraj Michalek 00:41:59 Thank you, please.
Arthur Silva Sens 00:42:00 Nope.
No, no, actually, with your change, Cryo, like, that… so Prometheus in the past received OTLP, transforming to Promethe Remote Write, and then we append it. But now, it just receives OTLP,
and appends without transforming to Prometheus remote, right? So couldn't we just remove the… delete the code in Prometheus?
krajo Krajcsovits 00:42:24 What do you mean?
Alright.
Arthur Silva Sens 00:42:26 the… the code that transforms OTLP into Prometheus Remote, right?
krajo Krajcsovits 00:42:33 Couldn't, like, this is not being used anymore in Prometheus, right?
No, but it's… it's now converting to TSDB. So, I mean, you cannot just remove the whole thing, because you… you cannot, you know, import the contributing Collector. So, what you could do is put it again into a third
like an outside package, like the OTRP transmission.
Juraj Michalek 00:42:59 Because…
Arthur Silva Sens 00:42:59 like, why would the collector want to transform OTLP into TSDB?
krajo Krajcsovits 00:43:06 it wouldn't, but there's… the point of that PR is that we are not…
converting into anything in particular now. We are converting to an interface.
And Prometus implements the interface towards TSDB, And… .
Juraj Michalek 00:43:23 Mimir is implanting it to convert into something else.
And so can, I guess, cortex and tanos.
krajo Krajcsovits 00:43:30 Yeah, anyone can…
Juraj Michalek 00:43:32 and…
Yeah, yeah, so we could do the same, right, in the translation logic to RV1, RB2, that would actually make
That would potentially… because right now, like, the code for RV1, RV2 is just a lot of duplication, because the structs are different, right? So that would actually probably allow me to clean it up pretty nicely.
But…
Yeah, it would require, again, moving it to a neutral… well, no, like, another third-party repo, because otherwise we get cyclic dependencies again.
krajo Krajcsovits 00:44:06 Yeah, the obvious question is, would you want to put it next to the… the, like, the name translation that's already in the third-party product?
project, or not project, but… Repo. Repo, yeah.
Arthur Silva Sens 00:44:16 Oh man, I was hoping to release 1.0 this week. If we do this, like, that would delay a lot of stuff.
Juraj Michalek 00:44:24 Well, could you add it after releasing 1.0?
Arthur Silva Sens 00:44:29 But… We could, but, like… I'm not confident to just copy code over there and say it's done.
And I honestly don't have the time to, like, fully understand this.
Juraj Michalek 00:44:41 I… Can try to do that.
But yeah, it won't be fast.
Arthur Silva Sens 00:44:48 Do you have the time to do that, realistically?
Juraj Michalek 00:44:51 Well, like, it'll take time, right? Like, I do this in the evenings, but… I can try.
krajo Krajcsovits 00:45:00 Yeah, I mean, obviously it won't… it…
I mean, it shouldn't block 1.0 if you want to raise that artery. This is, like, a big new feature, totally warrants 1.1 or 1.0, whatever.
In the library.
Juraj Michalek 00:45:18 We can hold off on making the decision, and let's not delay the 1.0 release, right, and…
I can just look at it, see how much work it would be, and yeah, then we can potentially discuss it later if I want to do it or not.
Arthur Silva Sens 00:45:33 Absolutely.
krajo Krajcsovits 00:45:34 You want to, include Bartek in the discussion, because He's actually…
thinking of and suggesting to have that interface that's now in use be the appender interface in Prometheus.
Which might complicate things, although which might not make actual sense, we don't know. So this is, like, again.
you know, one more thing against putting into the 120, this is not… this is completely new. Like, it has to prove itself in production, and we might make some changes still, so…
But…
Juraj Michalek 00:46:10 Good.
krajo Krajcsovits 00:46:11 making a POC out of it would be nice.
Juraj Michalek 00:46:13 Yeah, I can speak with Bartik, we're mentoring with him and another guy from Tunnels, the mentorship around RV2.
In Prometheus.
Arthur Silva Sens 00:46:28 Hey, Jonathan added another topic.
Jonathan (jojo) 00:46:32 Yeah, but I'm not sure if I have enough context to talk about it.
I just… That this issue needs triage.
Arthur Silva Sens 00:46:44 Okay, I can talk about it.
So, one guy,
Open an issue about the Prometus Remote Write Receiver.
Asking to add an option to, to keep, some labels.
more specifically, if a remote write request comes with job and instance, today we are translating those… those labels to service name, service instance ID,
And they… they are requiring… they are asking us to add a translation option called Translation Strategy.
That does not transform the labels.
I said that translation strategy that we have today is completely different. It is not about translating labels into
Like, job instancing to service name.
But I also said that This is a requirement from the spec.
I'm not sure what we can do there.
But does anyone have an opinion?
Owen Williams (he/she) 00:47:56 So, okay, so this is… receiving Prometheus remote rights in the collector.
So this is kind of a reverse translation. It's going from Prometheus to Otel. Yeah, I mean…
Short answer is, calling this no translation would be very confusing.
Arthur Silva Sens 00:48:18 Yeah, yeah.
Owen Williams (he/she) 00:48:19 So, I don't love that. I see what they're saying, though. The intent is essentially the same, which is like, hey, I know you want to do this thing, but actually, I want… I want the names to be what I sent, don't munch them. And they even say, like.
they could duplicate it, they could have both sets of names for consistency.
So… on the face of it, I don't have, like, a serious objection.
Just that, yeah, the naming choice kind of… Confuses things.
Kyle Eckhart 00:49:08 Oh, one of the things I was kind of interested about that they didn't really chime in on is, like, more generally, like, what's their use case? Like, it's a… it's a very specific ask for something, and it's like, on the surface, it doesn't seem bad, but at the same time, like, what's this trying to support? Just… just even for context? Yeah.
Arthur Silva Sens 00:49:27 He mentioned that he has a query.
that uses job instances in the label matchers, and then when he goes through the collector and then sends somebody somewhere else that I have no idea where.
They expected the job instance to be there.
I… I said that if you're receiving Prometheus, we translate to OTLP, and if you're translating OTLP back to Prometheus, this translation will do the same. We'll translate service name, service instance ID, into job and instance labels.
That apparently he's not sending with Prometheus components, Prometheus exporters.
Owen Williams (he/she) 00:50:10 Did I?
Juraj Michalek 00:50:12 Yeah, proper.
Arthur Silva Sens 00:50:13 I'm sorry.
Juraj Michalek 00:50:13 And on the point of the spike, right, we have updated it in the past. If we think this… adding this option makes sense, we can just update the spec again to allow it.
Or make it optional impossible.
And also don't love the name, because of the same complaint. Like, that would just confuse everybody, bye.
Arthur Silva Sens 00:50:34 I think Prometheus has an option that does that. Like, something, yeah, something like this.
Juraj Michalek 00:50:44 Yep.
So, I guess we already even have a precedence for that.
krajo Krajcsovits 00:50:50 Do you like that name, by the way? Because… I like him because I named that one.
They'll keep identifying.
Juraj Michalek 00:50:57 Well, they could own no translations in this context.
krajo Krajcsovits 00:51:00 Oh, fair enough.
Arthur Silva Sens 00:51:03 I… I… to be honest, identifying labels, like, every label is identifying, so I find that every… a little bit confusing.
But… Yeah, that's what we have.
krajo Krajcsovits 00:51:15 Yeah, that came from, like, a user… basically a support case that we got at Grafana. Somebody was really annoyed with that, and…
The name came from them, basically, so…
I should have consulted this group, probably, but I wasn't here at that time.
GZ Gregor Zeitlinger 00:51:31 Not every label is identifying.
Arthur Silva Sens 00:51:35 In Bermetus, it is.
GZ Gregor Zeitlinger 00:51:38 Well, from a conceptual point of view, if you have,
pod labels, then the pod UID, or the pod name, is identifying, but then you also have non-identifying things, like cluster name, or something like that.
So, from a conceptual point of view, I think, It's clear.
Arthur Silva Sens 00:52:09 Yeah, but so, about this, adding this configuration option, if we call it
Keep identifying labels or something else.
Do we want to add that to the spec?
And then… And then work with all the SDKs, all the exporters to implement this.
Juraj Michalek 00:52:27 Well, you can add it as optional, right? You can say.
can, and that they don't have to implement it unless somebody specifically asks for it. I think we have done that, at least. Wasn't that what was done for the thing with the underscores also? Right? Like, not force everybody to implement it, but allow it being implemented where it was necessary.
Arthur Silva Sens 00:52:47 Yeah, then we used May.
Juraj Michalek 00:52:50 Or, I don't know which one, but one of those.
Arthur Silva Sens 00:52:57 I'm… I'm not really excited to do this work, but I'm not gonna block anyone if…
If you want to do it.
GZ Gregor Zeitlinger 00:53:06 Where is this issue was… identifying labels, I didn't follow.
Arthur Silva Sens 00:53:14 Let me find it.
It does exist in Prometus configuration today.
Kyle Eckhart 00:53:30 Yeah, it's one of those things where it's, like, it feels like the amount of workarounds to, like, not have this be a problem are large, or it's, like, the amount of people that would be impacted by it is so small.
I don't know.
Arthur Silva Sens 00:53:59 Here we have… Spam of docs in the chat.
krajo Krajcsovits 00:54:07 Yeah, I just linked to the docs on Prometus I.O.
And I wanted to see if it has a name for job end instance, but… Not really.
it does say that they serve to identify the scrape targets, so identifying is kind of fair? I don't know. I don't want to name something else and then be blamed for it, so…
Juraj Michalek 00:54:32 Up to you.
Arthur Silva Sens 00:54:33 Oh, yeah.
That's not your fault, like that, for sure.
GZ Gregor Zeitlinger 00:54:38 I think I know where this is coming from,
I think this is a set of,
resource attributes that is predefined, and that is around, service. So, service, name, service.
instance ID and service namespace.
But this should be, specified somewhere, I'm surprised.
Oh, yeah, it says service name, service name, service, and service instance ID, just 3 lines above.
So what… what are you taking issue with? I still don't un… I still don't get it.
Arthur Silva Sens 00:55:23 They, like, with the…
the person is asking is that we add this option to the receiver, so when a remote ride request comes to the remote
Right? Receiver.
We… we…
We don't translate the job and instance labels to the service name, service namespace. We keep job and instance as they are.
And they are asking for that because they have a query that expects those labels to be there, and after passing through this receiver, they lose it.
GZ Gregor Zeitlinger 00:56:03 And here it says that, so service name should be duplicated, both in service name and in job.
Because it says, on top of converting them into instance and job.
Arthur Silva Sens 00:56:18 They say it should be duplicated.
Juraj Michalek 00:56:20 Yeah, I think because that's what the thing does in Prometheus, right? It keeps it, so it still does the translation.
But, it also keeps the original one. Would it?
Now that I'm thinking about it, can't they just fix this? So if they're receiving… can't they just fix this in the pipeline with,
With, like, a processor, they can just copy it manually using a processor, no?
GZ Gregor Zeitlinger 00:56:44 Do we reconstruct?
Arthur Silva Sens 00:56:45 It could.
GZ Gregor Zeitlinger 00:56:46 Sure.
Juraj Michalek 00:56:47 Do we want to suggest that as a first option? Because as Arthur said, like, until somebody else complains, that sounds like a lot of engineering work.
One person wanting to do something that they can do in the pipeline.
with that processor.
GZ Gregor Zeitlinger 00:57:02 This is not just for one person, this is important user feedback that many users are struggling with, because,
They, don't understand, that service name suddenly is something else, so I would not discard this as a single person.
Arthur Silva Sens 00:57:23 Yeah, that's fair, too.
Juraj Michalek 00:57:25 But then that's more of a documentation problem, because that is the behavior defined in the spec, then something we should necessarily fix by changing the spec.
GZ Gregor Zeitlinger 00:57:35 Well, this is, a little bit saying that, just read the manual,
And,
I don't think that's… that's a good answer. So, at least I don't agree with it. I think,
This is an important feature that makes it easier for users, to,
Work with the data, and impose less constraints on them.
Arthur Silva Sens 00:58:09 So, maybe we can tell, like, what Yurai said, like, tell them the workaround, use a processor?
And also say that we are happy to do this new configuration thing.
But this… this needs to be through the spec.
So it's consistent. It's not just one thing that we do in one place and not in the others.
GZ Gregor Zeitlinger 00:58:34 Yeah, that's fair, of course, yeah.
Juraj Michalek 00:58:36 You could… Also mention, right, if we don't really have the time for it, that…
It might happen eventually, and if they want it to happen earlier, they have to drive the actual work, like raising PRs to change the spec, raising PRs to implement this.
Arthur Silva Sens 00:58:51 Yeah.
Juraj Michalek 00:58:51 If it's important to them.
Kyle Eckhart 00:58:53 They did… I mean, they did say they'd be happy to contribute. Maybe not all the way back up to the spec, but…
Arthur Silva Sens 00:58:59 Yeah.
Juraj Michalek 00:59:00 the.
Arthur Silva Sens 00:59:00 Yeah, I have a suspicion that they think it's just a single code change and that's it.
GZ Gregor Zeitlinger 00:59:07 That's always how it starts, isn't it?
Juraj Michalek 00:59:10 Well, the person commenting on it, they also are a member of OpenTelemetry, so… and a contributor, so it's probably not their first rodeo in the organization.
Arthur Silva Sens 00:59:21 It's actually… it's actually a collector approver.
Juraj Michalek 00:59:24 Oh, cool, so…
They might actually have, like, an understanding of, like, this is gonna be a fun thing to do.
Arthur Silva Sens 00:59:32 Yeah, yeah.
Okay, we have 3 minutes. Any last-minute thing to discuss?
Juraj Michalek 00:59:42 Was it kind of write the message? Are you.
Arthur Silva Sens 00:59:46 Do you want to…
Juraj Michalek 00:59:46 -
Arthur Silva Sens 00:59:47 I can do it, no problems.
Juraj Michalek 00:59:49 Thank you.
Arthur Silva Sens 00:59:56 Alright, if there's nothing else… See you around. Bye-bye.
GZ Gregor Zeitlinger 01:00:02 See you!
Juraj Michalek 01:00:02 I'm back.
