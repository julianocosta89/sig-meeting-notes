SIG: Java SIG
Date: 2026-10-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Gregor Zeitlinger** 00:59 Hello!
**Trask Stalnaker (Microsoft Corporation)** 01:48 Hugger!
Could you approve this for me? I broke the build with a couple of conflicting commit, PRs.
**Gregor Zeitlinger** 02:01 Huh.
**Trask Stalnaker (Microsoft Corporation)** 02:02 Thank y'all.
**Gregor Zeitlinger** 02:39 Are you in a rush to get a lot of stuff through Trask?
**Trask Stalnaker (Microsoft Corporation)** 02:45 It's… it's our chance to make all the breaking changes.
keep pushing back 3-0, but I feel like… October is the backstop, so by the end of the month.
It'll be out.
**Gregor Zeitlinger** 03:05 You gotta look back to this time with fond memories.
**Jason Plumb** 03:13 And then you get to celebrate it at KubeCon.
**Trask Stalnaker (Microsoft Corporation)** 03:17 Yeah… Yeah, so that's the… update on… V3 stuff is… continuing to wind down, and of course, finding more new things. Oh yeah, thanks for… that.
target is, pushed the target back a week, so next Wednesday, but I could see that. The backstop I have is, has got to go out in October, so… It's gonna happen.
**Jason Plumb** 04:05 Is that self-imposed, or is that external influence? Where is that coming from?
**Trask Stalnaker (Microsoft Corporation)** 04:10 It's just me.
**Jason Plumb** 04:12 Okay.
**Trask Stalnaker (Microsoft Corporation)** 04:14 Hey, Juan, I need to move on to other stuff.
**Jason Plumb** 04:18 Yep.
**Trask Stalnaker (Microsoft Corporation)** 04:18 But also, Yeah, I mean, we could be working on this 3.0 release forever.
We have been. It was when it was originally supposed to go out in July.
It's just… Never-ending amount of things that, once you start… Once you also, once you start pointing LLMs at the repo and asking it to find, semantic convention conformance problems.
**Jason Plumb** 04:50 find stuff.
**Trask Stalnaker (Microsoft Corporation)** 04:51 Wow. Yeah, I mean, it's legit. But, man.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:55 Then you can't unsee the bug. You can't unsee it.
Big fat.
**Trask Stalnaker (Microsoft Corporation)** 04:59 Exactly.
Alright, yeah, Jack?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:11 Yeah, it's one of those, I… I didn't kind of realize that this was maybe timely with the, with the V3, crunch, but maybe it is. So, as Jason and Trask are aware, I've been making some PRs to instrumentation to update the resource providers to make them be entity aware.
So, so far, the service resource providers and the process resource providers produce entity-aware resources.
The next one that's, on my list is the host resource providers. And this one's a little bit tricky because, there's actually two resource providers. There's a host resource provider and a host ID resource provider.
Host provides host.name and host.arch, and hostID resource provider provides host ID. So it, like, it's like two providers that are providing, you know, attributes that are all related to the host. And this is problematic from, from making these entity aware, because all of these attributes are part of the same entity, definition.
And so, as a prerequisite to making the host's entity aware, I'm proposing merging these together.
And the reason I think it's, like, you know, at least worth conversation is because by some definition, and I'm not sure if this is your definition, it is a breaking change, because, you know, resource providers can be enabled and disabled by their fully qualified class name. And so, you know, I'm proposing basically that we get rid of the host ID resource provider, and therefore.
Anyone, depending on that.
changes.
And I guess also, if you're programmatically calling host resource… host ID resource get, you know, you… that would be a breaking change for you as well. So…
**Trask Stalnaker (Microsoft Corporation)** 07:00 Yeah, but that's an alpha artifact.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 07:03 Right, exactly. So, like, to… I guess I don't… I'm… I'm sort of out of touch in the… in the practices of instrumentation in terms of, like, for alpha artifacts, what kind of hoops do you jump through for backwards compatibility?
**Trask Stalnaker (Microsoft Corporation)** 07:19 We generally do a one-cycle deprecation, If possible.
But it's accept… it's… it's allowed to not… do that.
That's just a… best effort.
**Jason Plumb** 07:36 I mean, let's get it in this week, and it can be breaking.
Yep.
**Trask Stalnaker (Microsoft Corporation)** 07:41 Exactly.
**Jason Plumb** 07:41 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:42 You don't have to worry about any of that right now.
Just break away.
Just add it to the changelog. The changelog is gonna be massive.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 07:56 So should I, it sounds like folks are roughly, like, aligned with this, then, like, do I tag this somehow, just to make sure it doesn't get lost in the fray, or, like…
**Trask Stalnaker (Microsoft Corporation)** 08:07 Oh, yeah.
Fair.
So we add the milestone, and then, yeah, just add the, add the… add a changelog entry.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:21 Oh, we're doing that now? Like, changelog entries, okay, I'll add a changelog entry.
**Trask Stalnaker (Microsoft Corporation)** 08:26 Yeah, we do it for braking changes only in the PRs.
Okay. Just as, like, an extra… Make sure we don't miss it in the… when we construct the real changelog.
**Jason Plumb** 08:42 The lines change thing is awesome, I don't know how you did that, but congrats.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:49 That's so weird.
It's not, like, it's not even, like, a strict, like, fine replace either, and it just worked out perfectly.
I noticed that too.
**Jason Plumb** 09:01 Cool.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 09:05 Alright, you're not at the bottom.
**Trask Stalnaker (Microsoft Corporation)** 09:07 Yeah, I think Lyudmila had even asked in the Java Slack channel about this, why we had this in two different resource detectors. So yeah, combining them.
Yes, follow-up from last… Weeks, or two weeks ago, discussion.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 09:35 Yeah, I actually was supposed to do a little bit more homework before this discussion that I didn't do, which is to go and compare this to what the collector does in terms of its maintenance policy. I didn't have a chance to do that, but So, yeah, just the context was that we don't really have a formal policy for requirements for components to stick around and contribib. And so, every time we're thinking about, like, hey, should we do this, or should we do that? We just kind of collectively shrug, and we sort of re-litigate things over and over again. So, I think having, like, a policy just allows us to be more, objective, and, like, and algorithmic with just, like, hey, you know, this criteria has happened, and so we are going to end-of-life this component, or, you know, you're continuing to meet this criteria, so thumbs up. And there's, like, less subjectivity in it.
And, let's see, like, what is the basis for the contribib policy that's, like, worthy of discussion? So, you know, what I would propose is, you know, components in Contrib need at least two component owners. A component owner has to be somebody within the OpenTelemetry org.
So, that's the… that's the library of people that can be, component owners.
Component owners are expected to be responsive, and if you repeatedly ignore maintenance responsibilities, that triggers removal of, from being a component owner. So, this responsive definition becomes load-bearing, and you sort of have to define that a little bit. What does it mean to be unresponsive?
And, what I… what I think I said was, you know, unresponsiveness is like somebody tags you explicitly to look at an issue, or PR, and you don't respond in a certain number of calendar days. Like, 14 days is what I proposed up there. And if you have a certain number of unresponsive infractions in a certain amount of time, then, like, then you get kicked off of being a component And I think this is… this could be automatable, which is, like, a feature that I want to have of this policy. So, even though I didn't propose the automation scripts right now, I, like, at least in my head, want it to be, like, feasible to automate this.
And, yeah, so, like, you can tweak the knobs a little bit. You can be like, hey, like, how many days do you have, qualifies as being unresponsive, and how many unresponsive, you know, events do you need in what amount of time in order to be kicked off? So those are, like, configuration knobs, but, like, the rough structure is, like, you need to be responsive, and if you're unresponsive a certain amount of times, you get kicked off.
And then a component, which dips below the component owner requirement enters a phase where it's like, it's like actively recruiting new component owners for a deterministic amount of time, and if it fails to solicit someone new to volunteer, it, it gets, it gets removed.
So this is, like, the… this is the rough structure.
And… Let's see, is there anything else worth talking about? Does anybody have any feedback?
**Trask Stalnaker (Microsoft Corporation)** 13:03 I like this recruitment period.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:09 Yeah, like, I've… Trask… and as you're reading this, just, like, you know, you've done a lot of automation with, you know, GitHub Actions and tooling. Does this seem like something that could be, like, encoded into, like, Python scripts and GitHub Actions to run in the background?
I thought yes.
**Trask Stalnaker (Microsoft Corporation)** 13:31 So…
**Jason Plumb** 13:32 We have automation that does that around, not component owners, but, you know, around, approvers and stuff.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:40 Yeah, right. Marillia set up this automation to automatically open the PRs to remove people as approvers and maintainers. Yep.
So it's similar, but there's… this is a little bit more complex, because there's.
**Jason Plumb** 13:53 like this.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:54 There's this, like, solicitation window where you're trying to recruit more new component owners.
And, I think also you have to… you have to think about the difference between alpha components and stable components. We have, like, exactly one… one or two stable components, and the rest are alpha, and, like.
you know, I think being stable has certain considerations, but, like, doesn't exempt you completely from this, from this component ownership requirement, because, like, like, if you… you can imagine, like, Okay, you've got a stable component, and it dips below the component ownership, like.
we can't just stop publishing it immediately. Because it's stable, I think we owe the users, like, a deprecation cycle, where we publish it with deprecation annotate… deprecated annotations. And then… Like, you know, then you have to consider, well, what happens if you've published a deprecated version, and then a component owner comes back and volunteers, and like, you know, you're all of a sudden in the green again? Well.
you have to be okay with that, I think. You have to be okay with things like marking things as deprecated, then undeprecated, and even getting to the point where you delete a stable component, and then maybe bring it back exactly as it was a bit later. Like, so, like, maybe it becomes deprecated, is deleted, and then, you know, 4 months later, you start publishing it again, and it's not deprecated, because people stepped up and volunteered for it.
I think that's just kind of the reality, and I'm okay with that myself.
**Trask Stalnaker (Microsoft Corporation)** 15:34 I think that deprecating is a good idea. I don't know if you've captured this already during that recruitment phase, like, once we hit that, like, we could… because that could be a good way to generate recruitment, is by releasing a deprecated Version, because people who are using it will then see that deprecation notice.
**Jason Plumb** 15:57 Maybe.
They might see it.
I was gonna… I was gonna question the value of the deprecation, because for components that have been published, I mean, people can certainly continue using those published versions. Like, a component that is effectively unmaintained is gonna be identical between releases, basically, anyway, if no one's maintaining it. And so, just silently dropping… I mean, we shouldn't do anything silently, but, like, dropping it from future publications because we removed the module… It doesn't prevent people from using the older version that was… Barely maintained anyway.
So what do we… what do we… what do we gain?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:41 It's, like, the slim chance that somebody sees that deprecation warning, that new deprecation warning in their build output, and then is, like, concerned by that, and goes and acts on it, and volunteers to be an owner.
**Jason Plumb** 16:55 Yeah, I mean, I think that is… I think that is what we gain, is, like, the… it's more transparency and more planning for people to work around stuff.
I guess.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:04 But I did qualify it as, like, that deprecation thing that only happens for stable components. I think on stable components, you just… At least in this formulation, and I'm okay, I'm okay with feedback on this, but, yeah.
**Trask Stalnaker (Microsoft Corporation)** 17:20 I wish that, Maven Central had a concept of deprecated package.
I know that, like, NuGet, does, and I don't know if other package managers do, but it's super… Nice way to be able to communicate.
**Jason Plumb** 17:38 Yeah, it'll tell you about ma- like, majors, it'll point you to, like, the newer version, but you can't end… you know what I mean? Like, there's that thing that it'll point you to.
There's a newer version of this.
**Trask Stalnaker (Microsoft Corporation)** 17:48 Oh, if you rename… if you rename the… if you rename it, yeah.
**Jason Plumb** 17:52 Yeah, but that's not the same thing.
I like this policy, I mean, I think this is good. We need something like this.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:04 Yeah, and we've got to align the incentives, and I was actually thinking about, like.
Whether something like this makes sense at, like, the project level as well, like, Like, we have SIGs, and we have repos that sort of live on well past their maintenance. Like, people stop attending the SIGs, but it stays on the calendar. The repo stops being maintained, but it, you know, it keeps… there's no, like, signal that it's unmaintained, it just, like, sort of gradually falls off.
I was wondering if, like, at a project level, like, you know.
It's like, it would be nice if things default expired, and you needed to meet certain criteria for them to continue.
So everything had, like, a default TTL, and you need to, like, renew, like, the SIG. You need to renew the repo by meeting some activity or other criteria in order to continue going. And that would be, like, a natural garbage collection process.
**Trask Stalnaker (Microsoft Corporation)** 19:03 I can see having, like, once a year, or whatever we… interval we choose to basically post in this issue… post here, and ask all component owners to basically re-up pack.
And, you know, if they don't hack it, you know, and we follow up and they still don't hack it, that's, you know, then… It's, like, avoids that silent drop-off.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:32 Right.
**Trask Stalnaker (Microsoft Corporation)** 19:36 And yeah, I definitely think there's… there's stuff to be learned or shared across other repos, like if we're, you know… I think that's a good idea to see what the collector contrib is doing, but then if you find, you know, some automations or some other processes Sharing that more broadly.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:57 Yep, so I'll do that. I don't think we're in a rush to get this in, but, you know, I think we should sort of march towards progress on this, so we can sort of resolve these questions that come up every once in a while about what is our policy on Contrib?
**Trask Stalnaker (Microsoft Corporation)** 20:17 I had one thought here, which was, as you were asking how to, like, as far as automating how to… how long it's… how do we know if somebody's not responding to stuff?
I guess issues is one thing, PR is… Like, we could track, you know, if it's… Something is waiting on reviewers for 2 weeks.
That could be a… Trigger.
To escalate something.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:51 Yeah, and you need some sort of log of, like, an event log, so, like, you know, because if you are counting infractions in a certain amount of time, then you need to know that, like, an infraction occurred, and I don't know, it doesn't feel great to have that in a public dashboard.
Bye.
Maybe you could encode it into comments or something hidden.
**Trask Stalnaker (Microsoft Corporation)** 21:19 Yeah, there is, I don't know, historically… so there's a… All the dashboard stuff is, Yes.
Oh, okay, okay, so… in… So, for our repo, so the dashboard… Date is here… So, potentially, you could look at the history… I'll drop this link.
But potentially you could look at the history on this branch.
I forget exactly what's all there.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:15 Okay.
Take a look.
**Trask Stalnaker (Microsoft Corporation)** 22:22 Because, yeah, I had some thoughts. I think it would be cool with the dashboard in general, or the data from that, we could see… like, how long, in general PRs across repos are waiting on reviewers as sort of, like, a benchmark for how well We're handling reviews.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:48 I know there's some people that have, Marillia has some data on that, but, like.
it's hard to track. You basically have to download the entire Git history and activity history of every repo to some local place so you can do your local analysis.
**Trask Stalnaker (Microsoft Corporation)** 23:07 Yeah, the da- but the dashboard has all of that. It… that data.
Oh, yeah, I guess.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:14 It's a requirement of it, huh?
**Trask Stalnaker (Microsoft Corporation)** 23:17 So, like, if you look at… It actually keeps track of the age, meaning how long it's been waiting on reviewers.
Damn.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:35 Everybody knows that, though.
**Trask Stalnaker (Microsoft Corporation)** 23:36 time.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:37 Is it all, like, point in time, or does it have, like, a local data source somewhere, like a cached, you know, exported view of, you know, the GitHub, essentially, audit log?
**Trask Stalnaker (Microsoft Corporation)** 23:49 Yeah, that's what this, the link I dropped in chat.
This is the state.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:55 Oh, I see.
**Trask Stalnaker (Microsoft Corporation)** 23:56 In the shared… so we've got… each repo has its own branch in shared re… shared workflows, where it keeps track of the state and caches, so that it doesn't have to
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:11 I'm following now, there's repo-specific state on a specific branch.
**Trask Stalnaker (Microsoft Corporation)** 24:16 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:17 before.
**Trask Stalnaker (Microsoft Corporation)** 24:18 In theory, you could… I think you could recalculate everything every time, but it would just be exorbitantly expensive.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:26 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 24:35 Alright, next, let's see, we've got cleverchuk, K…
**cleverchuk** 24:46 Yeah, hello.
**Trask Stalnaker (Microsoft Corporation)** 24:46 reconfig.
**cleverchuk** 24:49 Yeah, I think it came up one time, but, it hasn't been spoken again, so, like.
I would like to be able to, like, configure, like, the export and stuff basically completely with the declarative config, but it doesn't have the… the proxy configuration, I suppose, that way. So, to configure the proxy, you just have to, like, do it programmatically. So do we, like, have plans to, like.
Make that… Possible?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:23 Yeah, so this is a… This is a… You know, The way that this flows, the way, like, a property gets added to the declarative config schema is, like.
and therefore gets encoded into the Java implementation of declarative Config is, you know, there's an OTLP specification that specifies the set of configuration options that all OTLP clients should have.
And, you know, declarative config is unopinionated. It just, like, uses the spec as a reference for which properties it should capture, and so it says, oh, there's a… there's a spec property for the endpoint. Okay, we're going to encode that in the declarative config schema. There's a spec property for the timeout, we're going to encode that in the declarative config schema.
And, And then, you know, Java sees that, and it's like, oh, there's a declarative config schema property for endpoint for timeout, so we're going to recognize those.
And, so, like, the right way to do this is to go all the way to the root of it, and to update the OTLP specification to include proxy options. And so, you know, try to work with the other maintainers of the other languages, and be like, hey, we think that it's good for OTLP clients to have proxy options, and this is the standard way we want to represent those and configure them. And then, you know, that would follow through in declarative config, and then Java could pick up those declarative config options and, you know, encode them in its implementation.
So that's, like, the best way to do it, and it can be sort of tricky and take a while, to.
**cleverchuk** 27:07 Look at this.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:08 stuck, but
**cleverchuk** 27:11 So, yeah, so, like, the other languages, they sort of don't have this issue. I didn't look too deep into it, because they all support, like, a HTTP proxy or something.
And, java doesn't have, like.
That special one, except if you set it on the JVM.
So, is it possible to, like… I don't know.
do it in Java without having to, like, get the… The spec going first.
To let me support stuff that…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:49 We don't have… we don't have… in theory, we could do that, like, we could, have Java-specific properties on the OTLP, exporter, declarative config schema, and, like, say, you know, hey, even though this isn't part of the official schema, we recognize that if you set, like, you know, the proxy endpoint and this other pro- option, then we're gonna respect those and configure OTLP exporters accordingly. So we can do it in theory, but we don't have, like, precedent for it, and so we don't really know how that works yet.
There's not examples I can point you to that say, like, hey, you can just go follow this. And we also, like, not having precedent, like, it also means that we don't have answers to, like, when and why we do it. So you… we kind of have to, like, develop that… that precedent, here, if you wanted to take that route.
But, Trask, okay, proxy options.
**Trask Stalnaker (Microsoft Corporation)** 28:45 Yeah, like, so, wondering if that would be an option for us to support the Java… options, and clever check if this would… address what you're looking for. It wouldn't support it via declarative config, but… I'm assuming that's what you meant by other languages don't have this problem, because at the language level, you can configure the proxy for the built-in ACTP library?
**cleverchuk** 29:20 Yeah, so the issue with the JVM one is that it's so… that is for the whole JVM. It will, like, affect every, Every outbound call.
Like, if you wanted to…
**Trask Stalnaker (Microsoft Corporation)** 29:35 Other languages solved that.
**cleverchuk** 29:39 Yeah, like I said, I didn't look… I didn't look too deep into it. I don't know if that affects the whole call out of the… Language process or not.
**Trask Stalnaker (Microsoft Corporation)** 29:48 Okay.
Yeah, no, that makes sense that you may not want that to affect the whole JVM.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 30:02 Forget, is there any… There's a spec issue about this.
**Trask Stalnaker (Microsoft Corporation)** 30:13 Yeah, I mean, I think that's where I would start, Is look for… see if there is a spec issue. If not, open it over there to, Open a spec issue.
Share it, you know, do some research on If this affects other languages as well.
And how to, you know, get support for that across… Generally, we look for, I mean, it… I would… there's roughly 3, languages or support, at least for getting something all the way to stable, but, I think that's a good… Sort of litmus for whether we get broad enough support to push something forward in the spec.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:03 But we also want to need it to be stable to start, like, using this, right? So, even if the spec added a in-development option for its OTLP client specification that said, hey, there's these new proxy options, and they're still in development.
Declarative config would go and take that as a signal to add these proxy options to its schema in, you know, with a development suffix that, like, indicated that it's still subject to breaking changes.
And, you know, then OpenTelemetry Java would start respecting that, those properties in the schema, and you could reference them. So, you know, they would still be subject to breaking changes, but at least you could start using them.
So… I think… I think proxying, where I lean on this is, like, proxying is a common enough request, and it's language agnostic enough that I think it is good to work this out at the spec level and not have… take the shortcut of, like, just doing a Java-specific thing for expediency.
**cleverchuk** 32:05 Alright, sounds good. Thanks.
**Trask Stalnaker (Microsoft Corporation)** 32:12 Alright, moving on, exporter back pressure…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 32:22 Yeah, so, person.
I think their name is Aditya, opened this PR to try to sketch out what a back pressure mechanism would look like that would allow our processors to evolve into being able to call exporters concurrently.
Trask's pet project for all these years.
And so the way that they've… The way that they've gone about this is they've added a new method to exporters called concurrency limit, and it returns an integer, and the idea is, like, hey, if an exporter supports Higher concurrency than 1, it implements this and returns how many times its export can be called concurrently, and then it's on the processors, it's on the callers to coordinate.
So all the processors then have to be updated to be like, hey, this exporter supports concurrency level of 5, and we need to do all this, you know, work to make sure we respect that and don't exceed it.
And that, I think, works. There's some… there's some trade-offs, but, like, the other approach that we could take is, and I have a comment about this below, is… where the… an exporter adds a new Boolean method, so instead of an integer, it's a Boolean, and it's just like, hey, do you support exporter back pressure?
Yes or no? And default is no. So, like, by default, we continue doing it as is, and, like, you know, processors will just, like, you know, call export sequentially. They won't call export at the same time. But if they return true for this, then, the idea is that, processors will call export, Yeah, they'll still call export sequentially, but they won't await its completable future to resolve before they call it again.
And so, it's up to the exporter to signal BRAC pressure to the caller, to the processors, by switching its export mechanic from being, like, to be, like, selectively blocking, right? So, you know, let's say you have… it has, like, 5 background working threads, and, you know.
The first 5 calls to export, they return very quickly, because they have a completable future that resolves when those background threads doing each of those 5 requests resolve. But on request 6, then all of a sudden, it's, its thread pool is saturated, and it blocks the export call until the, until there's, you know, until the pressure relieves, until there's capacity in the thread pool.
And, there's some slightly different trade-offs between these. It's like, you know, basically, it comes down to who is… who is doing the, who's doing the coordination for, like, understanding, like, the concurrency and… and orchestrating it.
And if you take the… if you take this alternative where, you know, there's a Boolean, then the exporter controls this, and I think I'm slightly in favor of that approach.
Because I think that the exporter has the most… has the ability to have the most knowledge about its, the state of its… its… its worker threads, the state of its back pressure, and it doesn't have to count on the caller to do any coordination or call it in a particular way in order to… in order to not… not get overloaded.
So, what I told this…
**Peter Findeisen** 36:09 I like the approach with the Boolean a little bit more, because it offers more flexibility. You can have an exporter that changes the number of concurrent operations over time, depending on Different things.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 36:26 Right, there could be some sort of expandable worker pool, which expands and contracts over time, and another thing that this allows is, let's say you want your back pressure mechanism to not be concurrency-based, but, like, byte-based.
Like, like, so, you know, you may want to support many, many small concurrent requests, but if they become really large, like, you know, tens of megabytes or hundreds of megabytes, maybe you want to stop at just one or two concurrently. So, it gives you more ability to be finer-grained control.
**Peter Findeisen** 37:00 Yes.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 37:07 So what I told this contributor is, like, hey, before we get into the code specifics, let's align on, on the overall design, on, like, the architecture, and then we can, like, we can talk about code later. And, yeah, so if folks have thoughts on this, have preferences, if you could leave comments on that, please do. Don't get into the code specifics yet, let's, like, let's keep the conversation focused on, like.
high-level strategy.
And then, you know, I think the code falls out from that.
Pranav.
**Pranav Sharma (Google LLC)** 37:39 Yeah, this… this might be clear once I go through it again, and, like, probably, like, an implementation detail, but I was just wondering, for metrics, we have this requirement where the metrics need to go, like, in order, right?
In case of concurrency, like, will we be able to actually… Ensure that that happens, like.
If there are concurrent exports, then the metrics might get out of order.
Just wondering about that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 38:13 Yeah, it's a… it's a good question, so… We wouldn't have to change the periodic metric reader, just because the metric exporter can be called concurrently. I think, like, of all the signals, metrics has the least utility in this, you know, because, you know, it's already exporting on a regular cadence. Every 30 seconds, every 60 seconds by default.
And, you know, it's not like it benefits much, by being able to call… make those calls concurrently. And so the real utility is for log… the batch log processor and batch span processor.
And I guess that would be a choice that we have to make, is like, do we even want to consider bringing this over to metrics at all?
**Pranav Sharma (Google LLC)** 39:00 I see, yeah, that makes sense.
Okay.
I'll take a look at this issue. Thank you.
**Trask Stalnaker (Microsoft Corporation)** 39:10 Jack, what's your thinking on, spec.
Like, whether this is something that should be aligned on at the spec level, or with other languages.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 39:23 Let's go back to the conversation we were having in the spec call a couple of weeks ago, where there's already languages that have taken this interpretation.
And…
**Trask Stalnaker (Microsoft Corporation)** 39:34 But they haven't… have they provided a concurrency limit Or they kind of imp…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 39:42 they, like… look, we could have taken this approach from the start if we hadn't made the interpretation like them. Like, consider this Boolean approach, right? Like, Erlang is an example of, like, one of the languages that took this approach, so they don't need a Boolean signal on the exporter's ability to handle, like, concurrency and brack pressure, because they, like, that was the default interpretation from the beginning. And so, like, I view this as, like, a backwards compatibility mechanism.
**Trask Stalnaker (Microsoft Corporation)** 40:17 Got it. That makes sense to me.
**Jason Plumb** 40:22 I raised my hand because I was having some sort of weird network glitch earlier, is that gone, or am I still having it?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 40:29 Sound clear to me.
**Jason Plumb** 40:30 Okay, cool, thank you. I like you.
**Peter Findeisen** 40:33 Yeah, it happened a couple of minutes ago.
**Jason Plumb** 40:37 Okay, weird.
**Trask Stalnaker (Microsoft Corporation)** 40:37 You look like you're in the Shining, hotel, though.
**Jason Plumb** 40:41 What, with these kids?
**Trask Stalnaker (Microsoft Corporation)** 40:42 Oh, Ida, yes, okay, so you are.
**Jason Plumb** 40:47 To Pranav's point, OpenTelemetry doesn't have a guarantee for delivery order, does it?
For metric data points.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 40:58 Pranav, I think, was asserting that it does.
**Pranav Sharma (Google LLC)** 41:01 Yeah, or the…
**Jason Plumb** 41:04 There's an expectation that they will be delivered in order, but I don't think there's any guarantee of it from the spec, is there?
**Pranav Sharma (Google LLC)** 41:11 I remember something about caring about the order when I was doing the batching thing, but, yeah, I'll take a look at this in more detail, yeah.
**Jason Plumb** 41:22 Okay.
Yeah, cool, thanks.
**Pranav Sharma (Google LLC)** 41:25 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 41:32 Alright, Jason!
Yeah, Caesar, you're up.
**Jason Plumb** 41:38 Well, yeah, we went through these kind of quickly, I wasn't… I wasn't ready. I'm… I just wanted to bring something… Yeah, we do use a lot of reflection, right, when we have these extensions in Core.
For example, the, the one that happened recently with… the entities on the resource. It's like a bunch of extension stuff that uses reflection, and… Cesar was like, yeah, I think at Elastic, we hit some rough edge around that when using a minified app. So, they might already be using some of these, like, new, NC features.
And in the Minified app, obviously that doesn't work, because the names all got changed, I guess.
To which, I mean, the obvious solution is, well, don't change the names, but… I'm just wondering if we've… has this come up before, and have we given any thought?
**Trask Stalnaker (Microsoft Corporation)** 42:37 I mean, it's a pretty standard minification problem.
And I… Not that minifiers were good enough to be able to detect reflection and not rename those, if you're…
**Jason Plumb** 42:53 Right?
**Trask Stalnaker (Microsoft Corporation)** 42:54 doing that.
**Jason Plumb** 42:54 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 42:56 But…
**Jason Plumb** 42:57 Cool, I didn't have any more detail, I just wanted to bring it up in case it sounded familiar to anybody.
And…
**Trask Stalnaker (Microsoft Corporation)** 43:04 I think I've seen projects that will, like, publish… sometimes you can have, like, a, you know, ProGuard or whatever the, you know, if I are using the configuration.
Yeah. For it, to, like, help people.
**Jason Plumb** 43:18 Yeah, we have some of that in Android already, and we're not using entities because they're brand new, but once we started, maybe this was something that we would need to give some consideration to, if it doesn't… If it doesn't work, and by work, I mean if it doesn't account for those name changes in the minification.
And hopefully our smoke test would catch that, but it will be our… Our next version bump, because… it just… that just got merged.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 43:45 What name changes are you referring to?
**Jason Plumb** 43:47 When you minify… When you run a minifier, it'll change method names, and so the reflection can't find it. That's all I mean.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 43:55 Have you seen that, maybe you're familiar with this, with, like, GraalVM, you have to publish this, like, reflectconfig.json as part of your artifacts that, informs the Graal compiler of, like, where you're using reflection?
**Jason Plumb** 44:10 I haven't seen that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 44:11 It sounds, like, very similar to this, and I wonder if the minifiers Have their own standard, for how you declare reflection usage?
**Jason Plumb** 44:25 Is that something?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 44:25 Just look for reflect-config.json.
Right, there's a bunch of examples of this.
**Jason Plumb** 44:35 That's cool.
Is the… is the recent stuff in there?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 44:44 It, it, yeah, it's… we have, we have tests that…
**Jason Plumb** 44:48 Cool.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 44:49 Verify this.
I'm trying to…
**Jason Plumb** 44:52 So maybe we can…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 44:53 out loud whether it's perfect or not, whether we can perfectly test that all the required reflect config is present.
**Jason Plumb** 45:00 But maybe we could leverage that.
**Gregor Zeitlinger** 45:02 Oh!
**Jason Plumb** 45:02 That's cool.
**Gregor Zeitlinger** 45:03 So whenever I added a feature to add those files, I also added a test that makes sure that this is actually required.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 45:15 Gregor, wouldn't we have to make sure that the GRAL, tests Basically exercise all the code paths that use, that use reflection, and thus would need this reflect.con… reflect config.
I think that would be the only way to ensure…
**Gregor Zeitlinger** 45:31 It's the test?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 45:34 Yeah, because if we're testing that reflect config, it's… Sorry, go ahead.
Oh, Jesus.
**Trask Stalnaker (Microsoft Corporation)** 45:46 Then you need perfect test coverage.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 45:49 Yeah, and the test coverage needs to exercise, like, in a way that would depend on reflectconfig.json being present and complete.
And if… and I think that would… that's only the growl tests.
Native image tests.
**Gregor Zeitlinger** 46:07 Yes, that is true, it's only the prior tests, you're right.
**Jason Plumb** 46:14 Cool, I suspect the cases, we just haven't… butted up a case yet from Android where we're using something that… Gets minified that we rely on the reflection extension stuff.
And… I don't even expect that we'll… I don't anticipate that we'll hit it with the next version, but I guess we'll see.
But cool, I didn't know about that, reflect config. So that's a good… good thing to know about. Thank you.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 46:43 Yeah, and I guess my point is, like, if there's another standard format for our conveying reflection usage.
That's, like, maybe used by the minifiers or something like that. I think we have precedent for publishing that type of, metadata.
**Jason Plumb** 46:59 As an input to the minifier.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 47:02 Right, as an input to the minifier.
**Jason Plumb** 47:04 Yeah, okay, cool.
I'll keep that in mind.
Yeah, I think that's good. Thank you.
**Trask Stalnaker (Microsoft Corporation)** 47:14 Alright. Hey, Abiy, we made it to your topic.
**Abiy Asfaw** 47:18 I trust everyone.
**Trask Stalnaker (Microsoft Corporation)** 47:19 by the way.
**Abiy Asfaw** 47:20 Thank you.
So, yeah, for me, I, raised, an issue for a feature request, to make some Enhancement to the existing standard out exporter, which is in experimental stage.
So basically, yeah, I'm proposing, 4 additional configs, to be added to the existing exporter.
Which are a marker prefix, an option to set a marker prefix, which will be used to distinguish, telemetries generated from the SDK and application logs.
And, another one is, an option to encode.
In Pace64.
And, Also an option to have a GZIP compression.
And, setting, max line, byte, and, some mechanism to enforce it.
So all of this will be an opt-in.
If they're, they'll be off by default, and, Should not impact, yeah, how, telemetries are sent to standard.orafile right now, if we disable them.
So, yeah, wanted to get, feedback on… This proposal and, yeah, guidance on how to, contribute this.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 48:58 So, these, This kind of relates to the previous conversation about, the scope of projects like OpenTelemetry Java, and the standard exporter is defined in the spec, and, there's… it's configure op… configuration options are part of the spec as well. And, you know, for example, there was someone recently that wanted the JSON encoding to be pretty printed, so that it was easier to read in your, you know, debugging console.
And, you know, that got pushed back to the spec.
And I'm just wondering, like.
**Abiy Asfaw** 49:38 Let's see.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 49:39 Like, these are kind of specific options, like a marker prefix and, like, an encoding and a compression, but I'm also kind of recognizing that they could all be sort of, implemented if we provided a standardized, like, mapping utility? Like, if you could provide a configurable mapper, which took, like, the Marshalled JSON and mapped it to some other JSON, however you wanted, you could have that mapper Append the prefix, apply whatever coding you wanted, and in compression you wanted.
And it would be… it would be pretty, extensible and flexible.
**Abiy Asfaw** 50:22 I see, so is that going to be outside of the SDK?
Duh.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 50:25 So, the idea that I'm, like… and I'm just coming up with this on the spot, so, like, I'm definitely open to feedback on this, but the idea would be, like.
Add a new programmatic configuration option where you can configure, like, an arbitrary mapper, that takes your… the output string and, you know, returns another output string based on that, with whatever changes you want to make to it.
And then you, the user, would have to configure this mapper to do whatever you want, to include the prefix, to apply the compression, to use whatever encoding you want, and so on and so forth.
**Abiy Asfaw** 51:06 I see, makes sense. Okay, I'll take a look into that. But yeah, so if we want to go with this approach, we have to first, raise an issue in the hotel space.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 51:19 Well, so I think you would need a… I think you would need an issue in the spec if you wanted us to, like, add all of these, sort of, very specific options, like a prefix option in base64, max line bytes.
And… but, like, with this mapping type approach, I think that's generic enough, and it solves enough problems that, I, as a maintainer, would be okay just, like, adding that as a programmatic option.
What I don't want to do is I don't want to, like, add very specific options that end up intersecting with and conflicting with the spec later.
Like, that's kind of what I want to avoid.
Gone.
**Abiy Asfaw** 51:59 Makes sense, okay. Do you have any resource on the mapping approach? I can, yeah, take a look into that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 52:09 Jason?
**Jason Plumb** 52:10 Yeah, I wanted to point out that, compression is a little bit of a tricky, sticky wicket here, because… the output of a gzip operation, or most compression operations, is, like, some binary payload, and so that kind of… prevents the output from being implicitly line-based anymore, and so if you need to specify a terminator or a terminating character, it needs to be outside and if it's binary output, then you can't specify a terminator that's outside of the output set, right? If it's arbitrary binary. So it kind of implies Base64 encoding, or some other encoding, in addition to just being compressed, right?
**Abiy Asfaw** 52:49 Right, yeah, so it will also, yeah, be Base64 encoded. So, yeah, GZ will imply,
**Jason Plumb** 52:56 Is that written in this issue?
**Abiy Asfaw** 52:59 No, it's not, but yeah, I'll, make sure. I think you'd want to cover that, and then…
**Jason Plumb** 53:05 Also, if you hit your max length, then I think that decoding that line might not be feasible, right?
**Abiy Asfaw** 53:14 Right, then yeah.
**Jason Plumb** 53:16 If you've gzip something, you base 64 encod it, and it's longer than the line length, then you have to throw out that whole line, basically, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 53:23 Yeah, it's corrupt.
**Abiy Asfaw** 53:24 Right, yeah, but the idea is, yeah, to split it before, with the discipline, Inc. code.
**Jason Plumb** 53:32 Oh, split, okay, okay.
**Abiy Asfaw** 53:34 Yeah, so, matrix, will be split into, like, data point level.
And, log records and traces will be an individual record.
**Jason Plumb** 53:46 Okay.
Do you have a specific use case in mind right now for this?
Yeah, so…
**Abiy Asfaw** 53:55 Yeah, so the use case is, for, AWS Lambda in a serverless environment, yeah.
**Jason Plumb** 54:02 Cool. Yes, anymore.
**Abiy Asfaw** 54:04 Yep.
**Jason Plumb** 54:05 Cool, thanks.
**Abiy Asfaw** 54:07 Okay, thank you.
**Trask Stalnaker (Microsoft Corporation)** 54:15 Alright, we have almost made it to the end of our agenda.
Jack… I wanted to say something about, hotel JavaScript.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 54:27 Yeah, Hotel JavaScript, they released a V3.
The other day, and, I was looking into this a little bit, and, like, what the breaking changes they made into it, and kind of how they were thinking about it, and the… their API is still on 1.x. There's no API major version bump, and the major versions are coming to the SDK and SDK-related components.
And the way that they're thinking about it is they're getting into a regular major version bump cadence. For them, I think it's, like, once a year. And, you know, that's an opportunity for them to make, sort of, you know, big breaking changes to APIs that are user-facing, but they don't have to only do that. They can do more mundane things, like, what they did in this is they updated their minimum node version requirement for this.
And, I'm not saying that necessarily is applicable to us, but, like.
I don't know, the wheels just started turning in my head, and I was like, hey, what kind of things would we want to clean up if we entertain the idea of a major version bump in the SDK? Not the API, but in the SDK?
That's all.
**Jason Plumb** 55:42 can drop Java 8 support.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 55:45 No, that's…
**Jason Plumb** 55:47 I'm gonna keep saying it.
Be bold.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 56:00 Yeah, I can think of a few APIs that I don't like that we have in the SDK.
That would be nice to clean up.
And I would also feel more comfortable about Things like, you know how we have this issue, which is, like, we don't want to use shared internal code?
like, I'd be much more comfortable, like, carte blanche publishing all shared internal code to, a public API place, this implementation package, if I knew that we could, change it in a year or two from now. So I think that's just something off the top of my head. I think it could allow us to make meaningful progress on the no shared internal code Issue.
**Trask Stalnaker (Microsoft Corporation)** 56:46 Bumping the major version of the SDK doesn't… bother me.
I'm trying to think… What it means for the instrumentation repo, whether we would… Need to coordinate, essentially, a major version bump there.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 57:10 I think we would.
**Trask Stalnaker (Microsoft Corporation)** 57:11 well.
Yeah, because the instrumentations themselves only rely on the API, but we've got too many things, like the Spring Boot Starter and the Java Agent extensions that…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 57:25 Yep.
**Trask Stalnaker (Microsoft Corporation)** 57:26 Rely on the SDK.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 57:29 and behaviors of the SDK as well, not just the APIs, but like, you know, major version changes would be opportunities to change the behaviors.
like GRPC.
Stop making that the default for auto-configure.
**Trask Stalnaker (Microsoft Corporation)** 57:49 Yes…
**Jason Plumb** 57:51 I bet you distros… I bet you distros depend on the SDK a bit, too.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 57:56 Oh, definitely.
**Jason Plumb** 57:58 Fair enough.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 58:02 Anyways, food for thought, I'm not interested in making a thing about this, but, like, you know, there's precedent in other languages, and, you know, you don't have to… You don't have to sort of boil the ocean and make a bunch of really impactful braking changes, but, like, it gives you a space to do sort of the routine maintenance, the types of cleanup, and housekeeping that you'd like to do, but can't because of backwards compatibility.
**Trask Stalnaker (Microsoft Corporation)** 58:32 Bruno's not here today, but it might be worth… just DMing him on Slack, just to kind of, be curious from… Their perspective, what… how that would impact Somebody like a corkus.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 58:53 That's a good point. Maybe I'll… maybe I'll open an issue or something like that, just to, like.
But I don't know, is that… is opening an issue a bad idea? Like…
**Trask Stalnaker (Microsoft Corporation)** 59:01 That's why I was just gonna say DM. At this point, gather more… Feedback.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 59:12 Yeah.
Alright, that's all.
**Trask Stalnaker (Microsoft Corporation)** 59:23 Alright.
We made it.
Good to see everyone.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 59:30 Alright, take care. Bye.
**Jason Plumb** 59:32 I agree.
