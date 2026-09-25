SIG: Java SIG
Date: 2026-09-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Gregor Zeitlinger** 01:35 Hello!
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 01:40 Hello.
**Trask Stalnaker (Microsoft Corporation)** 01:41 Ayy…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 01:45 Hello.
**BRUNO Baptista** 01:53 Hello?
**Trask Stalnaker (Microsoft Corporation)** 02:22 Alright, add your topics!
Jason?
I see you.
**Jason Plumb** 02:41 Here I am.
**Trask Stalnaker (Microsoft Corporation)** 02:48 Is this an actual org restructure?
**Jason Plumb** 02:51 No, it's just me being snarky.
Shocker, I know.
**Trask Stalnaker (Microsoft Corporation)** 03:13 So… I… We need to get out a release.
I need to look through… the remaining things on my list.
So, I think I will probably give an update on… Monday… Lauri, thanks for starting to look at those… the messaging ones.
I will.
try to… I'll… I saw you left some good feedback on one of them.
And I'll get the rest probably into review today. They're more like… Bug fixes anyways, because it's more… they're more about duplicate… Avoiding duplicate instrumentation when, We have messaging frameworks and, messaging clients.
Wrapping messaging clients, and we have instrumentation in both layers.
There's a bunch of small things that, so I'll look through those and, send PRs for those, I was kind of this… I got derailed a bit.
Yeah, cause I still… I want this to be… the last 2X release. I want to get 3.0 out. I want to stop, spending… Aw, so much time on that.
any… Questions? Anything anyone wants to… Raise… Yeah, what, if Monday is still September, so… I would say, wednesday… I really don't want it to go past September, so let's say Wednesday's September 30th.
Latest release.
30… 2, I think.
Alright, let's… Move on, Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:30 Yeah, so, there's a ish… Oh, wow, that didn't actually link. That auto-linked, I guess, yeah.
**Trask Stalnaker (Microsoft Corporation)** 06:40 Yeah, yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:41 I like.
**Trask Stalnaker (Microsoft Corporation)** 06:42 It's not… it's not you.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:45 Okay, so, service instance ID.
there's… There's, like, sort of competing specs that say… that talk about its stability level.
From a semantic convention standpoint, the attribute is stable, and the stable convention talks about its generation, and how, you know, you should use a UUID-based generation strategy, if that's, like, you know, lower priority than if, if it's provided by a more reliable source.
And that's good. But, over on the spec level, There's a set of named resource detectors, and there's 4 of them. There's host, Container, service, and… Process? Process. And, I added those to the specification because I needed, like, I needed to tame the Wild West of resource detectors, where it's like, there's a concept called resource detectors, but there's no standardization across languages.
I needed, like, a standard set of resource detector names, so that those could become part of the declarative config schema.
And so that you could reference them language agnostically in your YAML files.
And that part of the specification where we list these named resource detectors is still in development.
And so, you know, on the semantic invention side, it's stable, and on the specification side, the named service detector that provides service instance ID Is… is in development, but, you know, again, that… that only exists for the purposes of, declarative config.
And so, what this PR here does is it stabilizes the service instance ID detector that's not used in declarative config, it's the one that's used when you're using system properties and environment variables.
And I think it's the right thing to stabilize this, you know, given this sort of, like, ambiguity and conflict between semantic conventions and the specification, you know.
I view system property and environment variable configuration as this sort of legacy or deprecated feature, and we haven't officially deprecated it yet, but it's going to be supported forever. And, you know, in this Old world of doing things, our resource detectors, like, the way that you select them and enable them and disable them is by using their fully qualified class name.
And that's sort of, like, what we're stabilizing here, is that, like, hey, there is going to be a resource detector with this fully qualified class name, and you can reliably toggle it on or off via our system properties and environment variables.
And it will be, you know, available by default.
And, you know, today it's actually already available by default, for almost all of our users, because it's bundled into the agent.
So this is a no-op for, like, everybody that's using the agent.
Except for, I guess, the fully qualified class name changes, so that, that, if somebody is relying on the old class name.
Done.
That would affect them, if they're toggling it off.
But, yeah, that's… this is, you know, I saw an empty agenda, so I'm like, hey, let's talk about this real quick. This service since its idea has been around forever. It's kind of crazy that it's the year 2026, and it's still not stable.
So…
**Trask Stalnaker (Microsoft Corporation)** 10:41 Is this the only unstable resource provider in the core repo?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:52 Yes, I… and, you know, I guess you have to distinguish between… for declarative config and system properties and environment variables, because on the declarative config side, we sort of reinvented what a resource detector is, and they have their own sort of names.
short names, not fully qualified class names. But yeah, all the other resource detectors from the old world, system, property, and environment variables, those moved over to the instrumentation repo a long time ago.
And I haven't reviewed this yet, like, maybe I reviewed it one time, but, like, the build was broken for a long time. But I opened the issue, that this PR, you know, sort of implements. So, you know, this is something I've been thinking about, and… It's… it's sort of a trivial thing to… the mechanics of how you stabilize it, the more important question is just, like, conceptually, do we want to?
**Jason Plumb** 11:53 So, I haven't… I'm just looking at this for the first time, but stabilizing it seems good. At first glance, it looks like there's a small or easily overlooked semantic change in this PR.
Which is that the service instance ID can be provided through the resource, environment variable?
And previously it was that conditional resource provider, and it checked to see if there was already one in there.
And it wouldn't apply the random one.
So it seems like a.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:21 Yeah, yeah, that's… that's true. So, like, okay, and the reason that they did this was because the conditional resource provider, that interface, is experimental.
**Jason Plumb** 12:34 Yo.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:34 And so, you can't have a stable resource provider that extends an experimental interface.
And… Sure. But, like, you know, and help me walk… just, like, walk through this in my head, or walk through this with me. So, right now it's conditional, and it's like, hey, does the existing, resource contain a service instance ID?
What's the difference between that check and just the… an ordering? Like, putting… putting the service instance ID resource provider, like, very low in the order, such that anything else is evaluated later and applies on top of it?
**Jason Plumb** 13:17 Is there a… is there… I follow your train of thought. Is there a resource provider for the environment variable?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:25 For parsing, like, hotel resource attributes.
**Jason Plumb** 13:29 Yeah, exactly, yeah, that one.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:31 Yeah, that's represented as a resource provider.
**Jason Plumb** 13:33 Okay, and yeah, so as long as that had a higher order, I think, than what you're saying, it makes sense.
Cool. That's not… it wasn't readily apparent to me from this, but if that's the… if that's the way it works, and that's the intent, cool.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:47 Yeah, that's a good question, and that's, like, into the nuance of, like, this. So, yeah, good call out.
**Jason Plumb** 13:55 I mean, I kind of want to discourage people from putting service ID in there anyway, in the environment variable, but people might have their reasons, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:03 Yeah, they might have their reasons. They might want a service instance ID that's stable across restarts, something like a, A daemon set, that, you know, like, where…
**Gregor Zeitlinger** 14:14 Yeah, the hotel, operator actually does it.
**Jason Plumb** 14:17 Okay.
There you go.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:20 So, oh, the operator, it must be setting the pod name, or the pod UUU ID, as, like, the service instance ID, right, Gregor? Something like that.
**Gregor Zeitlinger** 14:29 a concatenation of, I think, namespace, pod UUID, or name, and container name, because, you could have… different containers.
**Jason Plumb** 14:43 Cool.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:47 So they're basically just using whatever downward API they can to get something, you know, more informative than a UUID set, so… Yep.
APIs, hotel resource attributes, and the environment variable.
**Jason Plumb** 15:01 Yeah.
Cool, that makes sense.
**Trask Stalnaker (Microsoft Corporation)** 15:07 Yeah, a couple of the… I think a couple of the cloud, resource detectors populate the service instance ID also.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:19 So, I guess, like, in my head, this kind of works as long as the Service instance ID resource detector has the lowest priority.
Right? And so, if we can set that, and I… yeah, I always forget if, like, the order is, like, if max means the lowest, or max means the highest.
**Trask Stalnaker (Microsoft Corporation)** 15:42 I hope it means the highest, I hate it when it means the reverse.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:45 If it doesn't… if that means the highest right now, then I'm gonna go and recommend that we change that, and change it to the lowest. Let's say that. Like, conceptually, what I want it to be is the lowest priority, so that everything else that has a better answer than a UID can trumpet.
**Gregor Zeitlinger** 16:03 Well, you should be aware that it could, also have Or an order declaration somewhere in the, agent.
So, we could break something.
**Jason Plumb** 16:21 Oh, there's a test for this.
That resource configuration test has this use case.
**Gregor Zeitlinger** 16:28 But is it testing all the resource providers.
**Jason Plumb** 16:31 No, of course, no, of course not, no, but the one I was talking about.
**Gregor Zeitlinger** 16:34 Okay.
**Jason Plumb** 16:35 Yeah, that's cool.
It's the explicit Service instance ID, yeah, that one.
Yep, so the custom one got in there.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:04 I don't hear any dissent, so I'm gonna… I'm gonna move forward with stabilizing this.
**Trask Stalnaker (Microsoft Corporation)** 17:11 Stabilizing is good.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:13 Yeah.
**Jason Plumb** 17:18 I love that none of us know the actual order, min-max, like, bigger or small. It's, like, exactly like the thing with sampling. Like, when you sample something, is it included, or is it not included?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:30 I did know at one time.
**Gregor Zeitlinger** 17:31 I know that I got confused by it a couple times.
**Jason Plumb** 17:37 How long have we been doing this?
**Trask Stalnaker (Microsoft Corporation)** 17:41 I gotta say, though, the final boss of that is… problem is the GitHub team, parent-child team.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:48 Oh, my gosh.
So on it.
**Trask Stalnaker (Microsoft Corporation)** 17:52 If you know, if you know, if you know, you know.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:00 And I just checked. Higher is, higher runs later, so higher number of order means, you know, higher priority.
So… We got…
**Trask Stalnaker (Microsoft Corporation)** 18:09 Yeah, Jason, I'm curious how that test was passing.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:13 Right, that's what I was thinking, exactly.
**Jason Plumb** 18:15 Whoa, yeah.
**Gregor Zeitlinger** 18:18 Oh, no, now I remember. Running later does not necessarily mean, that it has a higher priority, because if you implemented this conditional interface and were checking that it was not populated before.
then the semantics is inverted. That's… I think that was the reason why I got confused.
**Jason Plumb** 18:40 Makes sense.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:43 We gotta take a close look at this implementation.
**Trask Stalnaker (Microsoft Corporation)** 18:50 Alright, let's move to… Rule-based routing sampler.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:59 Yeah, you all remember the rule-based routing sampler. We added it a couple years back to solve the most upvoted issue in instrumentation, which is like, hey, I wanna skip sampling my health check spans, like, I don't want those included.
So the spec got around and, added this composable rule-based sampler, which is the alternative to rule-based routing sampler. And it's landed, it's available in declarative config, it is still experimental.
So that's sort of, I don't know, it's a data point. But, yeah, right now, so, you know, it's… it's conceptually a superset of rule-based routing sampler, so it can do everything rule-based routing sampler can and more.
And, you know, we have two things that do the same function. So, should we deprecate rule-based routing sampler, or should we wait until some condition is satisfied? Like, you know, composable rule-based routing… composable rule-based sampler is stable, or something like that.
**John Watson** 20:11 Is rule-based routing sampler stable, or is it in an alpha artifact?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:17 Contrib and Alpha.
**John Watson** 20:19 Okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:20 So we're substituting one sort of experimental for another experimental component.
**Trask Stalnaker (Microsoft Corporation)** 20:29 So that… then we would… replace… the agent today is using the contrib one, and not the core one?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:39 The agent can use both, because the agent packages in declarative config and the SDK incubator package, And so, yeah, if you reference the composable rule-based sampler in declarative config with the agent, it would work.
**Trask Stalnaker (Microsoft Corporation)** 21:02 Now would be a good time for us, if we're going to deprecate it in the agent, with 3.0.
Cause that would… given that it was a popular issue, we probably have a decent number of users using it.
And it would be a breaking change for us to remove it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:25 It's a good point.
**Lauri Tulmin** 21:25 How's the agent actually use it?
**Trask Stalnaker (Microsoft Corporation)** 21:30 What's that, Lauri?
**Lauri Tulmin** 21:31 Does the agent actually use it?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:35 It includes the package, the contrib package, so it bundles it in and makes it available for users to use, but the user has to sort of, like, opt-in by using declarative config and referencing it.
**Lauri Tulmin** 21:48 I mean, the contrary sampler.
So, it's only usable by… when the user uses declarative config, I guess.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:57 Correct. Okay. Because it has an expressive syntax that requires declarative config.
But yeah, the, you know, the benefit from the agent's standpoint is that the agent gets to remove a contrib dependency. Maybe that doesn't mean anything, because there's other contribencies, but
**Trask Stalnaker (Microsoft Corporation)** 22:22 No, it's good. It's better to have one way.
To recommend, document, do things.
So, yeah, that would be my only… Concern, though, is, like, it would be… Like, technically we could do it in a… I think, to Laurie's point, that it's only supported in declarative configuration.
We could do it in a minor version, since all of declarative config is experimental.
But I would prefer to do it in a major if… If possible, given the popularity of the feature.
**Lauri Tulmin** 23:04 Actually, I think it was added to the agent quite recently.
Only when the declarative configuration was introduced.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:13 It's been available for a while, though.
Like, you didn't have to use it, but…
**Trask Stalnaker (Microsoft Corporation)** 23:18 It wasn't through, oh, we had a file. You could give it a file?
**Lauri Tulmin** 23:22 Well, I think it wasn't included in the agent, like, it was included in the Splunk distribution, where it was configurable via a system property, where you could just, like, give a set of URLs that it would exclude.
But the upstream Agent didn't have anything. I think… was it Gregor who added it, maybe?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:43 I think so. I think it's been there forever, and it recently got split off into a dedicated declarative config package, but before it was just in, like, the SDK incubating package.
And so, which the agent has been pulling in forever.
**Trask Stalnaker (Microsoft Corporation)** 24:01 Still our all-time high.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:08 Like, is it that… this was sort of the full end-to-end flow for users is what I was aiming at solving, with this, and so, you know, it was twofold. It was, like, building the rule-based routing sampler, and also incorporating it into declarative config without either of those, it doesn't work.
**Trask Stalnaker (Microsoft Corporation)** 24:43 Okay, so… We've sort of… at least advertised it for… A good while, but… Probably… We might not have brought it in automatically, people may have had to add it as an extension, is that what you're remembering, Lauri?
**Lauri Tulmin** 25:03 It was added to the Agent about a year ago.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 25:06 Yeah, and 221.
**Lauri Tulmin** 25:16 The sampler was, like, written, like, way before it was actually added to the agent.
So.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:24 Look at that example that I posted in that issue that Trask was highlighting.
Because I… so many things in the agent, or there are several things in the agent that depend on the SDK incubator package.
**Lauri Tulmin** 25:39 Yeah, but the rule-based sampler isn't part of the SDK incubating package.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:45 Right, the rule-based sampler isn't, but declarative config is, which means that declarative config has been usable for a while.
Are you saying that the rule-based sampler was the recent addition?
**Lauri Tulmin** 25:55 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:56 Oh, okay. Misunderstood.
**Lauri Tulmin** 26:00 It hasn't been available in the agent that long, I think.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:04 Nice.
**Lauri Tulmin** 26:05 For about the year, actually, like…
**Gregor Zeitlinger** 26:09 A year is not long.
**Lauri Tulmin** 26:12 Considering, how long the issue was open.
**Jason Plumb** 26:16 Okay.
**Lauri Tulmin** 26:19 I think we can probably remove it.
I actually don't think it has that many users.
**Trask Stalnaker (Microsoft Corporation)** 26:35 Yeah, and we can remove it… We can go ahead and remove it, deprecate it, I'll deprecate it, probably, in the… this upcoming release, and we can remove it in 3.0.
And then we can… this is kind of… independent.
Then…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:04 Okay, then we can, I guess from a, a Java… class standpoint.
Update the classes to include the deprecated annotation, and… I guess we wouldn't want to stop deleting, or stop publishing that package for some… some period of time. Like, we maybe want to be more Generous, then.
than typical. Typical is, like, 3… 3 cycles? Three release cycles, but maybe we could go to 6 months, trade it more just like the open tracing shim, or the open census shim, which have got a longer cycle, or Zipkin.
**Trask Stalnaker (Microsoft Corporation)** 27:47 Yeah, I think it's fi- like, once we release 3.0, I think it's probably fine to remove it.
Because probably, I would guess most of the users of it are through the Java agent anyways.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:03 Hey, there's a question. So, since you have to support 2.x for some period of time, Is… is the publishing period of the contribib component sort of coupled to that in any way?
**Trask Stalnaker (Microsoft Corporation)** 28:19 Only if there was a CVE in a contribrib component.
And then, yeah, we would have to… Probably patch.
that contrib… And then…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:32 I… So, let's say there is no CVE, like, are you… when you do publish… patch releases for… like, are you doing regular renovate updates for the 2.x version of the Java agent, and would those include, updates to the contrib components.
**Trask Stalnaker (Microsoft Corporation)** 28:54 Lauri, do you remember what we… we went through this.
**Lauri Tulmin** 28:57 Last time, I think we did regular renovate updates. We even updated the SDK.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:06 Got it, okay, so…
**Lauri Tulmin** 29:07 If I remember correctly.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:09 than that.
**Lauri Tulmin** 29:09 I'm not sure whether we are ready to do it this time.
**Trask Stalnaker (Microsoft Corporation)** 29:15 Not really, though, to delete, because it will just… it'll just get stuck on the latest.
Oh, well, we have a overall, probably, contrib… bomb.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:27 Yeah, maybe you'd have to just exclude, have, like, a one-off exception version for the sampler component.
Sampler artifact.
**Trask Stalnaker (Microsoft Corporation)** 29:35 out.
That's fine.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:37 Broke up.
Alright, sounds good.
**Trask Stalnaker (Microsoft Corporation)** 29:54 Alright.
We are halfway… through and all out of topics. Anybody… Have anything else?
I want to chat about?
**Jason Plumb** 30:12 Trask, you missed the CNCF meetup in Portland, like, last week.
**Trask Stalnaker (Microsoft Corporation)** 30:18 What's it?
**Jason Plumb** 30:20 It was fun.
**Trask Stalnaker (Microsoft Corporation)** 30:21 What… what projects were there?
**Jason Plumb** 30:24 There was, so I guess that SRECon or something was here, like, the week before, so there were some people in town. One of the maintainers… of the Fluentbit docs was there, and gave a talk about contributing to that project using AI, and then Reese gave a talk about OTTL.
**Trask Stalnaker (Microsoft Corporation)** 30:44 Nice.
**Jason Plumb** 30:44 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 30:50 Alright, folks.
Well… And have a… enjoy the half hour.
**Jason Plumb** 30:56 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 30:57 Thanks.
**Jason Plumb** 30:57 Bye, everyone.
**Gregor Zeitlinger** 30:58 Bye.
