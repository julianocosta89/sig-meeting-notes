SIG: System Sem Conv Stability SIG
Date: 2026-10-22
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 01:20 Hey, guys.
**Christos Markou** 01:21 Hey, everyone.
**Pablo Baeyens (Datadog)** 02:08 Looks like Braydon will be a few minutes late.
Maybe we can wait one more minute on start.
Alright, should we start?
**Dmitrii Anoshin (Splunk Inc.)** 03:20 Hi, everyone.
**Donal O'Sullivan** 03:26 Hey, Dmitrii.
**Pablo Baeyens (Datadog)** 03:38 You want to start at all?
**Donal O'Sullivan** 03:41 Yeah, sure, I only had one thing, it was just kind of regarding your RFC, Pablo, I know it talks about making the, collector core.
V1 by KubeCon 2027 in Europe, so I was talking to Christos some… for making host metrics be one as well? I think you have those, the, the issue there to promote host metrics receiver to stable, so I guess we could start on that stuff.
**Pablo Baeyens (Datadog)** 04:15 Yep.
That's right.
**Donal O'Sullivan** 04:18 I think it's just following the guidance, isn't it?
on, stability.
**Pablo Baeyens (Datadog)** 04:24 Yeah, I guess we'll have to add the thing that we talked about, like the document that Braydon was going to write, but otherwise, yeah, I think it should be… Straightforward.
There's one thing that is… Maybe a bit weird about the host metrics receiver specifically, which is that it depends on the filter module from Core?
Which… I don't think it's a dependency of any other of the high priority components.
think dependencies through M-DataGen.
And… I don't know, maybe it's something that we can just… stabilize, or maybe it's something that we can fold into in data gen. I don't have a… strong opinion, because I haven't taken a deep look at it, but… there's that API dependency there.
We should talk about.
**Donal O'Sullivan** 05:32 Yeah, and that's not dependent yet, is it? Or, sorry, that's not, stable yet, is it?
**Pablo Baeyens (Datadog)** 05:37 No, that's not stable yet. Luckily, it's, like, a very small… There's two types with… Two functions, or methods?
But… Yeah, I wonder if we should just put it inside and data genera, something that we generate for… each module, I don't know. Does anybody have context about the filter package? I'm not even sure.
**Dmitrii Anoshin (Splunk Inc.)** 06:09 Who wrote it?
So, it was introduced to, kind of, provide Standardized way to… Apply filters on all of the companies?
It wasn't adopted.
as well as I would expect. It's only adopted by MDataGen.
The thing is, is that there are many places when we need to filter by something, like, by some attributes, or… some value… some strings, so I was… and… all of the places, they are pretty inconsistent. So, in one place, we have one configuration interface for that. In other, we use gloves. In that one, we use rejects plus strict, but they are, like, defined differently. So we… it was an attempt to standardize.
the approach.
So, I think it's still important to make it consistent across all the… All the companies.
**Pablo Baeyens (Datadog)** 07:21 Okay.
Let me check whether this is actually used.
Mmm… the 8th.
I'd say it's only… receivers.useit.
Nope.
I was going to send a list of receivers, but… It's too long for a Zoom.
But it's… 39 components, and they are all receivers, so… probably… Most of them are through IndeedGen.
**Dmitrii Anoshin (Splunk Inc.)** 08:04 So your suggestion is to generate that instead?
It'll be auto-generated code, I don't know.
**Braydon Kains (Google LLC)** 08:11 Yeah, I remember I thought about this when… when I was going to introduce the original, like, name-matching design. I wasn't sure if I was going to have it as a package in Collector Core, or if I was going to have it as like, a generated library in every mdata gen that used it, and I decided not to go the latter because you'd be repeatedly generating This, like, match… little, small matching library, which is, like, not… it wasn't a lot of code, but, like, regenerating it for every component was kind of a… a mess.
So I was gonna do it as a package in Collector Core, and then… the filter package became available, and so I started trying to just use that instead.
I joined late, but I assume we're talking about, like, trying to get name-matching… Like, being able to enable and disable en masse, right?
**Pablo Baeyens (Datadog)** 09:09 We are talking just about the host metric receiver, depending on the filter module, on, like, that means that we need to think about it, but yeah, I guess… The problem it's trying to solve is relevant here.
**Braydon Kains (Google LLC)** 09:23 That was… that was the… so, I mean, it… well, it depends on it, because MdataGen generates code that uses it, but my intention was to use it more, and use it as a way of, like.
I hadn't thought through this super deeply, but it was basically, like, you could have a list of rules that were, like, enable, filter.
And I had some PRs ready to introduce a filtering that matched Go SDK's wildcard matching pattern.
And just because of… collector core PR limits, I hadn't opened that. I think I have a, what's it called? We have a draft PR somewhere.
**Pablo Baeyens (Datadog)** 10:16 If you can find a link to please.
**Braydon Kains (Google LLC)** 10:20 Yeah, I will.
**Pablo Baeyens (Datadog)** 10:24 Would you prefer Dmitrii instead of… And I guess Braydon as well, like, what would you prefer we do with this module? Like, improve it in some way that makes it more useful for other…
**Dmitrii Anoshin (Splunk Inc.)** 10:39 I don't think there is any improvement is actually necessary, it's just maybe we adopt it more in other places, like processors and exporters, where mostly processors where some filtering required.
I think it was potentially… KTest Attributes Processor would be the one, but it's 1.0, so maybe not the right time.
And, I guess… Docker… something? Docker… I don't remember what was there.
maybe observers as well, I don't know. But anyway, even if we don't adopt it, like… store in other companies. We still… it's still required for the receivers, the mdata generate, and it's being used, I guess?
Hanges.
**Braydon Kains (Google LLC)** 11:32 used for resource attributes only right now, but I think it was gonna be used for more stuff later. But it was, like, enable resource attributes on… like, this resource attribute enabled on anything that matches, like, a regex.
That's your name.
**Dmitrii Anoshin (Splunk Inc.)** 11:45 And there is nothing wrong with that approach, right? It works fine, right? We don't want to… we don't want to change that.
approach.
**Braydon Kains (Google LLC)** 11:54 Yeah, I was hoping to use it more, actually, was what I was planning to do. I had this issue opened, where I… I had… first, I had a PR, that wasn't related to adding functionality, but was just, like, necessary for the… because it was, like, just… the metadata YAML didn't use something that it needed to, I forget. I think it was something to do with, like, the… the config schema generation. So I opened that first, and then I had a branch ready to open a follow-up once that first one was done, and because, like, when you're from a fork, you can't open, like, stacked PRs on GitHub, so I always do it, like, where I open a PR, and then I have a branch comparison to the first one that I, like, link, and be like, this is what I'm gonna open next when the first one's done, and that's what I did in this issue.
**Dmitrii Anoshin (Splunk Inc.)** 12:43 I see. Yeah, we don't have any problems with that as being used. I guess we could just stabilize it even without wider adoption.
Does that make sense?
So that's what we're talking about here, right? We need to stabilize cosmetrix receiver, and that depends on the filter. Filter is not stable yet, we need to decide what to do, right? I guess we can stabilize filter, I don't see any problems with that.
Braydon, what do you think, Pablo?
**Braydon Kains (Google LLC)** 13:12 I am okay with it. I don't know if… the… adding the new pattern type would be a breaking change, necessarily? I don't think so. So, I'm fine with stabilizing it.
**Dmitrii Anoshin (Splunk Inc.)** 13:24 Yeah, I think it's written in a way that it's expandable to… to add additional pattern matching if you want to, like blops or.
**Braydon Kains (Google LLC)** 13:33 Yeah, I… I'm pretty sure all I did was I added a new pattern type, and if the type was… This new pattern type.
for the filter, then it would parse that field differently, but it wouldn't… it didn't add or change any of the struct fields, I don't think.
**Dmitrii Anoshin (Splunk Inc.)** 13:48 Right.
**Donal O'Sullivan** 14:04 Sounds good, so that's probably the first chunk of work that has to happen before the other, Work can begin for,
**Braydon Kains (Google LLC)** 14:14 I can… I can pick that back up. The filter… the filter PRs, those two are both pretty small.
And then the part where we integrate it into mdataGen is gonna take a bit more thinking before I… Just go, like, adding stuff.
But at least the two PRs for the issue I linked.
I should be able to get those… those through relatively quick.
**Dmitrii Anoshin (Splunk Inc.)** 14:41 Yeah, I don't think it's a blocker for marking it stable.
**Braydon Kains (Google LLC)** 14:47 Yeah, not for marking the filter package stable.
Okay. I do think we, in the stabilized host metrics receiver issue, one of the things that we were talking about was Like, deprecating the processes scraper.
Yes. And before… I felt comfortable deprecating the processes scraper in favor of everything coming from the process scraper. I wanted to allow an easy way to enable just the processes, plural metrics, to get the old functionality for people who are still configuring the plural scraper.
And there wasn't an easy way to do that, because you couldn't… this, like, match multiple metric names at once to, like, mass enable or mass disable, and so I wanted to introduce the… the matching in mDataGen, and I had an RFC for that, but the procedure I came up with was way too complicated.
And so… My… my second, or maybe this is my third pass now, is to use the filter package instead.
And so that was… Just gonna add the pattern to filter.
And the pattern matches the Go SDK's metric view-enabled disabled pattern, so it's the same as that.
and then somehow add something to mdataGen where instead of the weird, wacky, like, map key regex thing I was trying to do, just have, like.
An array of filters.
For enabling and disabling, and…
**Dmitrii Anoshin (Splunk Inc.)** 16:15 Makes sense.
**Braydon Kains (Google LLC)** 16:17 Do them in order, basically.
**Christos Markou** 16:19 So that won't be breaking, right? Or it will be breaking.
**Braydon Kains (Google LLC)** 16:24 The…
**Dmitrii Anoshin (Splunk Inc.)** 16:26 Boom.
**Braydon Kains (Google LLC)** 16:27 the idea I have in my head for how it would work would be purely additive, but I don't.
**Christos Markou** 16:31 Here.
**Braydon Kains (Google LLC)** 16:32 I can't say for sure, because I haven't fully thought that through.
**Dmitrii Anoshin (Splunk Inc.)** 16:35 I don't think that's gonna be breaking… And, We still need to prioritize enable-disabled explicitly.
Under metric name.
**Braydon Kains (Google LLC)** 16:46 field? Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 16:48 Okay, so that one, if you don't… if you have, like, that enabled, disabled, it's still gonna work, even if you add filters, I guess.
**Braydon Kains (Google LLC)** 16:56 Yeah, right, the way I figured was that, like, mass… like, pattern enable and disable would always be less lower precedent than if it was specifically specified in the… Metrics Builder Config.
**Dmitrii Anoshin (Splunk Inc.)** 17:07 Makes sense, yeah. And it'll, like, work much better for config schema compared to what… compared to what we discussed before, when you have, like… when you have flexible keys, essentially, that's gonna…
**Braydon Kains (Google LLC)** 17:20 Yeah, that… that ended up being extremely awkward, and I had to come up with, like, a priority system, because map keys are never in a specific order, and it was just… it was messy.
Cool.
I think this one.
**Dmitrii Anoshin (Splunk Inc.)** 17:34 Yeah, I think we are… we're not blocked by this work, we can just stabilize it in that case.
**Donal O'Sullivan** 17:41 Yeah, so Justin.
**Christos Markou** 17:42 RMS.
**Donal O'Sullivan** 17:43 There's a question there, sorry, are we blocked on the deprecation of the processes scraper, though, to go to stable for host metrics?
**Braydon Kains (Google LLC)** 17:50 For host metrics, receiver… I don't know. Now that we're changing our tune a little bit on, stabilizing before Sem Conv, I don't know how important it is that the process of scraper get deprecated before stabilizing.
That might be… it might end up being a V2 thing.
I mean, one important thing is that the The alternate method of getting everything from one scraper, it's, like, better performance-wise, because you only scrape slash proc once per scrape, and get all the information instead of having to do it twice.
I don't know how much impact that's going to… Matter for a lot of people, but… So, like, it is better, but whether we have to, like, rush it before hitting V1, I don't know, like, making a major breaking change like that before V1 might not be worth it.
**Dmitrii Anoshin (Splunk Inc.)** 18:44 I agree.
**Christos Markou** 18:49 The… the rest of the issues, though, are, like, workable right now, right? Like, the requirements list for stability.
**Pablo Baeyens (Datadog)** 19:00 So, yeah.
**Braydon Kains (Google LLC)** 19:02 Let me refresh my memory on what was in that issue. Maybe we'll look at it in some time.
We actually ma- I made this issue… or, like, one of the, like, parent tracker issues I made before we even had, like, the priority stable component list.
Was it this, this, oh, it wasn't this issue, was it?
**Christos Markou** 19:20 Yeah, it's this one. Donal did that. I'll send it here as well.
**Braydon Kains (Google LLC)** 19:25 Right.
Oh yeah, okay, yeah, September 20th, 2024. Oof.
I can't believe this issue has been open this long.
Amen.
So… this… this old issue that I had, I don't know if we're still necessarily using this for tracking or not.
But I had a list of tasks But I figured at the time, And… I think… Introduce Semantic Convention's feature gate is done.
Refactor the scrapers to do… the data collection. This was before mdataGen had a design for this, so this task is defunct.
And… I had a Semcom spec to each receiver, also defunct. So… I think we can basically close the original issue I had open, and then… The… the one…
**Pablo Baeyens (Datadog)** 20:35 Put it as a sort of issue, like Kristen said.
**Braydon Kains (Google LLC)** 20:39 Yeah, we can open it as a sub-issue, and I'll figure out what I'm, What all stuff in that original issue still matters?
And then all the other sub-issues in the 1 and 44552, this, I think we can all… we can work on all this stuff.
Someone opened a node-exported parity gap as a blocker for stability, which is… Not actually a blocker's first ability.
**Christos Markou** 21:15 for, for Sem Con things, I think we had a discussion, similar discussion with Tyler yesterday about the Qiblet stats receiver, because I said… I asked him what's his opinion about proposing this, component for stability as well, as part of, like, the KubeCon, goal, and… he asked me about semant conventions. I think for this component, and I guess it's the same for host metrics receiver, should be fine to see those as V1 with very least candidate Semant conventions, if we have them by then. I think it's reasonable that we will have them by then.
And then keep the feature gates in alpha for the whole V1, Which means that the semantic conventions are in a list candidate, and then we can document explicitly that the goal is, in V2, to switch the gates to beta and have the stable semantic conventions. I think this would be… this could be a fair, statement from our side.
Across these similar components, like cost metrics, kibel stats, and whatever we target that. Because metrics can be… metrics Transitions can be tricky. It's not the same as the Cates attributes processor, that was only resource attributes.
Chill.
I don't know, any… any thoughts on this? Any objections, concerns?
**Braydon Kains (Google LLC)** 22:41 No, I think that sounds fine to me. I still have to write the strategy doc for Hosemetrics Receiver, but I was going to end up… like, once I finally write it, the plan is I'm going to say.
the… we're shipping V1 with the metrics that are here right now. This original metric schema is frozen, and we will not introduce any new features or changes to this schema. If you want to introduce new features, they have to be Under semantic conventions.
**Christos Markou** 23:13 Yeah, that sounds good. We should probably copy exactly the same.
For QBliss starts then. Yeah. Yeah, follow the same pattern.
**Braydon Kains (Google LLC)** 23:21 I'll… I'll… once I'm finally out of… Patching everything we own because of the certificate authority hack.
Then I'll make that the next thing I work on, so that CubaStats can adopt it too.
**Christos Markou** 23:37 Do we have any blocker? I mean.
Regarding Semconf, how far we are from making them, release candidate? We have process namespace already in release candidate, the system namespace is, like, in progress. Is there any significant block here? I think it was a PR from Logger. How far we are?
**Braydon Kains (Google LLC)** 24:00 Yeah, the PR Roger worked on, I think, is… is pretty much approved. I think I approved it, at least, and I saw a few other approvals.
That one was a stability blocker.
But I think we're pretty much settled on the direction for that, so I don't feel too worried.
**Roger Coll** 24:18 So we are applying those changes for the Stability version?
Well, I think we would… land on… B2?
**Braydon Kains (Google LLC)** 24:28 Or, sorry, we're just in Sem Conv, we're saying.
**Roger Coll** 24:31 Like.
**Braydon Kains (Google LLC)** 24:32 just for stabilizing them in Sem Conv, I think we're gonna release Candidate the version with two attributes.
**Roger Coll** 24:41 Okay, and I guess in the document that you were mentioning about the… well, the frozen version of host metrics, we need to explicitly mention that the the metrics will be stable, but the metrics in Semcom won't be stable, so that's a bit of a difference.
**Braydon Kains (Google LLC)** 25:01 Yeah, so the metrics… the, the metrics under the Sem Conv gate.
I think that depends on whether we're going to say… Are we going to bring any of our semantic conventions in before Release Candidate?
Even though I guess Release Canada isn't strictly stable, either.
So, I don't know.
**Christos Markou** 25:25 I think…
**Roger Coll** 25:25 I need to work.
**Christos Markou** 25:26 be optional to enable or experiment with release candidate metrics as part of V1. And once… I think the sequence would be that After a while, that we feel that the metrics are mature enough and already ported in the view on host metric receiver, we can declare them stable in some ad conventions.
when Semat Conventions will be released, and OpenTelemetry Go will be released, I guess that implies that, behind the feature gates, again, in host metric receiver, the metrics come as stable from Semat Conventions.
As they are. And after 8 months or something, we can discuss V2, and there we switch the gates as well.
So…
**Roger Coll** 26:11 Yeah, yeah, I agree, that's why I think the document should mention that the metrics are stable from a component perspective, but not from semantic conventions.
**Braydon Kains (Google LLC)** 26:23 Yeah, I think maybe, maybe the strategy docker can explicitly state, like.
There… we will be introducing metrics in House Metro's receiver.
At release candidate phase, so that they can be experimented on, which means they aren't strictly stable, like, they can still change after release candidate.
And… and then maybe we can… Say outright that we won't introduce semantic things from the semantic convention schema that are in beta, because they are very liable to change.
**Roger Coll** 26:54 I'll convertible.
**Braydon Kains (Google LLC)** 26:55 I'll mention that in the document as well.
**Roger Coll** 27:00 And now an unrelated question, there's a PR in the host metric receiver that they want to add a hardware scraper.
**Braydon Kains (Google LLC)** 27:10 Hmm, yeah.
**Roger Coll** 27:11 It's been a while.
**Braydon Kains (Google LLC)** 27:12 I'm a cat.
**Roger Coll** 27:13 Yeah, now my question is, do we want to add data scraper? Do we want to consider data scraper for V1, or not? I did a quick look.
And it seems that all the metrics and attributes that they are adding, they are part of SemConf already, they are defined, so… That's not a revocation.
The question is that if we want to include it or not.
**Pablo Baeyens (Datadog)** 27:42 My vote would be that we don't, at least not enable… like, maybe under a feature gate, but not… Enabled.
by default.
Even if they are on some other conventions. If I recall correctly, those… conventions… They were added a very long time ago, and have not been really worked on or owned by anybody, so I would be a bit wary about them.
**Braydon Kains (Google LLC)** 28:10 Yeah, I haven't actually seen the main person who owns those conventions. I haven't seen them in… A couple years.
And I've always been scared of them. People have always referred to them as, like, yeah, they're in semantic conventions, let's use them, but I'm like, I don't think they're, like, the same as other semantic conventions. I don't treat them the same, because… They don't fully follow the Semantic Convention's rules because they haven't been touched since they were initially added.
And… When there's confusion between Stuff in system versus stuff in hardware, because there's sometimes overlap.
For what looks like overlap, at least.
I don't know, it's always… always been annoying, but I think, like… The concept of a temperature scraper makes sense, and… I guess it's just a question of, like, are we going to… Consider this, like… Semantic conventions, because it's in semantic conventions, just like our… like, other… Like, is it going to be under our semantic conventions feature gate?
Because they're in semantic conventions and it's brand new.
I don't know, this is… this is… the same thing is… Kind of an issue with… the… raid?
scraper, people really want the RAID and MD stats in host metrics receiver, and I remember reviewing a bunch of MDStats, PRs, and Semconv, so that they could be added to postmetrics, and I can't actually even recall where those went.
And… how we're handling that for V1, I also don't know.
**Christos Markou** 29:55 Is the concern, because we're adding… we're going to add new metrics?
**Braydon Kains (Google LLC)** 30:02 Yeah, they're… all the metrics that are coming from… The new temperature scraper, and from… stats one.
We're all… they're all in semantic conventions, because I… I made the MDStats people put it in semantic conventions.
**Christos Markou** 30:16 Okay, but they are explicitly declared as, development or experimental.
**Braydon Kains (Google LLC)** 30:23 They're in development stability, yeah.
**Christos Markou** 30:26 I guess that's fine.
**Braydon Kains (Google LLC)** 30:27 That's wild.
**Christos Markou** 30:28 We have similar metrics in cumulates. They are added in both places, they are declared as in development, and I guess we are fine to leave them as they are. I think going forward, that would be the reasonable way to handle things.
It's the contract that, yeah, we can rely on.
Okay, prove.
**Braydon Kains (Google LLC)** 30:51 I'll think about this and try and include something in the strategy doc, too, but yeah. Alright.
Thanks, everyone.
**Roger Coll** 30:58 Thank you, have a good one.
**Christos Markou** 30:59 of… bye.
**Donal O'Sullivan** 31:00 you guys.
