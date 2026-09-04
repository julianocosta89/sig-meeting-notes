SIG: Java SIG
Date: 2026-09-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 02:30 Hey, folks.
Well, since we have, required participants for JAMX Metrics.
That's why.
**Jason Plumb** 03:31 bringing it up because Sylvain here. I'm like, yeah.
**Trask Stalnaker (Microsoft Corporation)** 03:34 into it.
**Jason Plumb** 03:34 I've… so, thanks for being patient and dealing with that stupid stuff that I threw out there, and I know the timing is terrible. So I have converted those to draft, and I'm happy to sit on those for a little while, especially while 3 is pending, and the stabilization work is happening.
Is the general… so, is the general approach okay on these, though? Like, am I just… am I super far afield, or is it like, we can… we can shore these up, it's just chaotic right now?
**Sylvain Juge (Elastic)** 04:03 Yes, I think the approach is more or less quite in line with what I had in mind. Maybe the biggest question is, how many metrics should we send by default, like, with the end goal? So, because If we make all metrics stable, it means it will send a bunch of metrics. For example, for Kafka, it could be too much.
But now that I have a PR to allow to enable and disable metrics by name, it might somehow make it, like, easier to use in the future, but… Huh.
**Jason Plumb** 04:36 I mean, does it… is it asking for some kind of, like, subcategories at some point? How granular do we make it? I mean, these are all future questions, right?
**Sylvain Juge (Elastic)** 04:47 Yes, and for now, like, having the ability to, like, include and exclude by stability is already a good step, I think.
But I don't know, like, how many… what would be the level of detail, and…
**Jason Plumb** 05:05 I think it just depends on the user. Go ahead.
**Trask Stalnaker (Microsoft Corporation)** 05:08 I think the include-exclude sort of solves the granularity problem that you're asking about, Jason, because people can do kafka.request.star.
**Jason Plumb** 05:21 Has an exclude or include… okay.
**Trask Stalnaker (Microsoft Corporation)** 05:23 Yeah, yeah, so it kind of… as long as we design the metrics with kind of namespaced groupings, then it kind of gives us that for free without having to invent you know, names to enable and disable different parts of them.
**Jason Plumb** 05:43 Cool. Yeah, yeah.
just as some context, I think that there was some… I think most of these are coming from some AppDynamics instrumentation that customers are used to seeing in certain platforms. So, like, I think I did Kafka and Tomcat. I think I've got, like, 5 others that are, like.
some different target platforms, and one or two of them might be entirely new that we don't have… any platform support for yet, so… just know that there's… these are the first two. There's probably, like.
4 more? Maybe 5 more?
**Sylvain Juge (Elastic)** 06:21 I mean… I think they're great. Yeah, it is fine to have more support, Maybe the question would be, the most time-consuming part that I spent with Robert discussing is, like, deciding on O2 makes them look like semantic convention compliant, like, discussing the naming, and… because you need to have some knowledge about the system you're instrumenting, because otherwise it's just, like, name matching.
**Jason Plumb** 06:48 Right.
Okay, well, I didn't need to talk about this a whole lot, I just, like, I saw Sylvain here, and the agenda was light, so… let's talk about your stuff.
**Trask Stalnaker (Microsoft Corporation)** 07:02 Well, just to… one last follow-up on your stuff, Jason, is, I don't think it needs to be… it doesn't have to wait till 3-0, it just needs to wait till… I just wanted to push back and have it wait until the… the JMX stability stuff that Sylvain is working on lands, and then we could still probably, you know, do this before 3-0, if there's time.
**Jason Plumb** 07:29 Okay, okay, that's cool.
I'm not… I'm not pushing for it in 3-0, like, it doesn't have to be, so… Thanks, I appreciate that, though.
**Lauri Tulmin** 07:39 Since it involves breaking changes, then, at least, like, renaming the metrics. It would be nice to have it in 3.0.
**Jason Plumb** 07:54 Yeah, I guess there are some that change the names, huh?
I don't remember which ones off the top of my head.
**Trask Stalnaker (Microsoft Corporation)** 08:05 Yeah, maybe you could call those out in the PR descriptions, because, yeah, that's a good factor, especially, I think… We're hoping to mark some… some of the… some of them as a good… a good set of them as stable in 3.0.
**Jason Plumb** 08:29 Yeah, legit.
**Lauri Tulmin** 08:31 I think the ones that changed names were those, like P99.
**Jason Plumb** 08:36 Oh, yeah.
**Lauri Tulmin** 08:36 99P.
**Jason Plumb** 08:43 Yeah…
**Lauri Tulmin** 08:44 So, I don't know, like, Since the guidelines for the names, like, require, like, renaming them, maybe… It would make sense to do, like, a pull request that takes the existing metrics and renames them and does whatever is needed.
To make them conform with the guidelines as a breaking change.
And then this pull request could just be applied on top of that.
**Sylvain Juge (Elastic)** 09:12 I think it would be a good approach, and so what we did in the past is changing metric names, And breaking them, basically, but it was not aligned with any, like, major version, so… For this one, it would be better to do that.
**Jason Plumb** 09:29 I think I'm still not… I'm not awake yet. What is the suggestion? It's to do the underlying name change first, so switch P99 to 99P, or whatever the direction is, and then come back with this one afterward?
**Sylvain Juge (Elastic)** 09:43 Yes.
**Jason Plumb** 09:44 Okay.
**Trask Stalnaker (Microsoft Corporation)** 09:46 Yeah, let's stabilize the… we want to stabilize what's there first, is basically, before we add anything new.
**Jason Plumb** 09:53 Got it.
**Sylvain Juge (Elastic)** 10:09 Okay, you probably want to, like, open the first one?
Yeah, the include and includes, yeah, 82.
The one below.
**Trask Stalnaker (Microsoft Corporation)** 10:25 So…
**Sylvain Juge (Elastic)** 10:26 What this PR does, it just introduces a way to filter which metrics are being included and excluded.
And after the initial registration, so even if you register custom metrics.
or you load the metrics from any of the existing YAML files, you have the ability to include and exclude the metrics by name.
And the second PR is built on top of this one.
And, adds the loading of embedded, Resource definitions.
Just before, starting, the JMix Insight.
**Trask Stalnaker (Microsoft Corporation)** 11:13 Sorry, explain this one again?
**Sylvain Juge (Elastic)** 11:17 Okay, so this one enables the ability to include stable metrics by default.
And so, it requires to change, like, to split the definition in stable and unstable, like, in two parts.
And, provide the API and configuration to load the metrics. So, stable metrics are always loaded by default, but we have an opt-in configuration option to enable loading extra metrics, for example, like Unstable Tomcat metrics?
would not be loaded, because we do not have, like, a Tomcat.yaml anymore.
You only have, like, underscore enable matrix.
**Trask Stalnaker (Microsoft Corporation)** 11:58 Got it. So the… we've got, unstable ones, and then…
**Sylvain Juge (Elastic)** 12:05 And so the JVM matrix is a good example, because it's the only one where we have, like, both stable and unstable metrics.
But JVM metrics are disabled, in instrumentation, so this change would only be visible on the consumer side in JMix Scraper.
But whenever we promote, Tomcat metrics from… Unstable to stable, and those would be automatically picked up, at instrumentation.
**Trask Stalnaker (Microsoft Corporation)** 12:35 And which ones are we marking as stable here?
**Sylvain Juge (Elastic)** 12:41 Yeah, the one without, underscore unstable prefix, suffix, sorry.
**Jason Plumb** 12:45 It's only JVM right now.
**Sylvain Juge (Elastic)** 12:47 Yes.
**Trask Stalnaker (Microsoft Corporation)** 12:49 Oh, okay, only JVM.
**Sylvain Juge (Elastic)** 12:52 Which is weird, because it doesn't make any difference in instrumentation yet.
**Trask Stalnaker (Microsoft Corporation)** 12:57 Okay.
And, your thought for… for 3-0, are you thinking to mark some of these as stable?
**Sylvain Juge (Elastic)** 13:07 Yes, I think it would be the next step. So, my goal is to merge this change in the next two.x.
And then, between, the next release and 3.0, mark some of those as stable.
**Peter Findeisen** 13:22 I have a question, if I may.
So, why… Why do we want to… enable, by default, those metrics that are stable? What is… what is the thinking about behind this? Because from my perspective.
The value of the metric is irrelevant compared to whether it's stable or not.
I might be interested in something which is not stable.
But it's not enabled by default, and vice versa. I could be not interested in some of the stable metrics.
Why do we want to connect these two things together?
**Sylvain Juge (Elastic)** 14:07 I think there was a guidance somewhere that, like, by default, we should only emit stable metrics.
And at the same time, so for example, like, let's say you want to use, like, JMIX scraper or instrumentation, you add the agent.
And you have lots of nice metrics that might be useful, for which you could have dashboards and so on, and you need to configure them. For example, you have Kafka, but you need to know, okay, what is the target system of it, or which metrics are relevant, and then you need to, like, configure it explicitly, whereas JMix has the ability to automatically discover available metrics, so whenever we have a metric, it means we should probably capture it by default.
**Peter Findeisen** 14:48 Well, okay, so… well, what it means is that we will have a subset of stable metrics exported by default, that's just fine.
But as the number of stable metrics grows, We will… Export more metrics by default?
I don't think it's a desired, result of… of this.
I don't like this strong connection between stability and default enablement.
**Sylvain Juge (Elastic)** 15:23 Basic, if you need control over which metrics do you want to export, you can always use the include list.
Right. To explicitly, like, list the metrics you want to capture.
**Peter Findeisen** 15:36 No, yes, of course, but that also means, probably, That was… agent upgrade, I will have to modify my configuration, because… I will get some garbage met… garbage from my perspective, Which I don't ca- don't care about.
**Sylvain Juge (Elastic)** 15:56 I think only if you… Only if you exclude metrics. If you include them.
It's kind of filtering. If you configure, like, inclusion of metrics, you only get the included metrics that are explicitly defined or matching the pattern.
**Peter Findeisen** 16:14 Oh, okay.
**Trask Stalnaker (Microsoft Corporation)** 16:16 Right, but that, that would, potentially point to, Not emitting anything by default, and people using the includes to get what they want, and to not.
Get more over time.
I mean, I don't… I act… don't mind getting metrics, like… like Tom… I mean, a lot of these metrics seem very useful, I guess maybe the… Concern might be… like, Kafka, something where, you know, historically I've seen some list of, like, a thousand metrics that come out of Kafka.
That could be, you know, not great.
But, like, a set of, you know, 10 useful Tomcat metrics.
Seems… I mean, if you're using Tomcat, Seems… Okay, doesn't seem like it would be, like, a huge… Noise problem.
**Jason Plumb** 17:31 I haven't reviewed this PR yet, but I have two kind of questions about it.
Are these unstable versions? Are they considered an additional target platform, or is it just, like, it's still part of the same target, but you have to opt in to the unstable for that platform?
**Sylvain Juge (Elastic)** 17:49 Yes.
Okay, so it's, like, the platform name now is only, like, the first part of the file name, and then you have to opt in per platform.
**Jason Plumb** 17:59 And is there… is there a configuration setting to say, give me all the unstable JMS?
**Sylvain Juge (Elastic)** 18:04 Yes, because it's an include pattern on the target system name, so you can just use a star.
**Jason Plumb** 18:10 Got it. But you have to specify that per target?
**Sylvain Juge (Elastic)** 18:14 No, you can, yeah, it's a wildcard, so you can put anything.
**Jason Plumb** 18:18 Okay.
**Trask Stalnaker (Microsoft Corporation)** 18:20 Where I was hoping to, to go with the include-exclude was, like, not even needing that target name.
necessarily.
**Jason Plumb** 18:29 Right.
**Trask Stalnaker (Microsoft Corporation)** 18:30 Because that's an extra sort of mapping that we have… people have to know, and we document, versus just…
**Sylvain Juge (Elastic)** 18:37 So, the challenge I had with that is you need to know all the metrics names in advance.
And I think due to the way the handlers work.
It was a bit hard to get all those metrics and include and exclude them.
M… Huh.
**Trask Stalnaker (Microsoft Corporation)** 18:58 Oh, to loop over the list of all the… Rule files.
**Sylvain Juge (Elastic)** 19:03 Yes, more or less. And you need to, like, iterate over all the metrics, and for all the metrics to know are they stable or not. So, this is why I took the shortcut to say, oh, let's skip the system, at least for the, Opt-in, per system.
But I agree with you, like, ideally, we would have, like, a registry of all the metrics with their stability, and have the ability to, opt-in per metric.
And another issue I had with that is, For example, for Kafka, you have some Kafka metrics, or Kafka broker metrics start with Kafka. And you have Kafka Connect that starts with Kafka.connect, which means if you want to enable all Kafka metrics without having to… including all the Kafka Connect metrics.
You, you need to add an include, and exclude it.
**Trask Stalnaker (Microsoft Corporation)** 20:02 Well, that feels pretty… Natural to me.
**Jason Plumb** 20:05 I… I agree.
Like, the broad wildcard include, and then the more narrow exclude, that seems… seems fine.
**Trask Stalnaker (Microsoft Corporation)** 20:22 Cool, anything else?
We want to… call out…
**Lauri Tulmin** 20:35 If we are going to enable the… stable metrics.
how are we going to handle the clash between the, I don't know, the JMX… the JVM metrics from the JMX and the runtime metrics?
**Sylvain Juge (Elastic)** 20:51 So, they are being explicitly disabled by default in instrumentation.
**Jason Plumb** 20:57 The JM… the J… sorry, the JVM ones are.
**Sylvain Juge (Elastic)** 21:01 Yes.
**Jason Plumb** 21:01 Okay.
**Sylvain Juge (Elastic)** 21:06 You have this in the, like, the installer class? I don't remember exactly, yeah.
**Jason Plumb** 21:13 Does that work for you, Lauri?
**Lauri Tulmin** 21:15 Yeah.
**Sylvain Juge (Elastic)** 21:25 But, I agree with you, like, the opt-in for, like, unstable metrics, would probably have been better by, using the metric name, But in order to do that, we need to first complete, like, the… having a registry definition for all the metrics.
And then, have maybe some processing to, like, generate the registry, content, and be able to do the lookup by name.
**Trask Stalnaker (Microsoft Corporation)** 21:54 Back to just, back to Peter's question about, kind of, I guess, volume and… Do we have any thoughts on how… where we limit these, again, because, I mean, like that Kafka example, or some… systems have, like, thousands of JMX metrics.
And, That would be… I don't think that would be desirable for a default experience.
**Sylvain Juge (Elastic)** 22:34 No.
**Trask Stalnaker (Microsoft Corporation)** 22:36 Like, are we kind of saying, hey, this is a fairly curated list of things that we think are important?
**Sylvain Juge (Elastic)** 22:46 I think it was more or less an intent, and it's… I think it's written in the recommendation for JMX metrics, to say it's not an exhaustive list, but we provide a few metrics that provide a basic experience.
But yeah, maybe we need to have a way to select how much details we want in our metrics.
That is probably not… like, stability is a proxy for now, because we don't have any stability, and… We will likely promote a few metrics at first.
But, if there is any kind of precedence, elsewhere, where, like, metrics are defined in, like, sets, like, you have, like, the essential set and then the extended pack, I don't know.
**Trask Stalnaker (Microsoft Corporation)** 23:35 I don't think so, but I… I think it's… I think it's probably… I think it's okay, at this point, as… Since we're kind of keeping it hand-picked, And smallish.
And we'll kinda… we can cross that bridge later.
**Lauri Tulmin** 23:56 I think the Kafka with Million Metrics was, like, the other Kafka metrics instrumentation.
**Trask Stalnaker (Microsoft Corporation)** 24:02 The bridge… thing.
**Lauri Tulmin** 24:04 Yeah.
And the fun thing about the breach was that, the exact list of metrics that you get depends on the Kafka version, I think.
**Jason Plumb** 24:17 Yeah, because they're probably…
**Sylvain Juge (Elastic)** 24:18 Absolutely.
**Jason Plumb** 24:20 Stuff all the time.
**Lauri Tulmin** 24:22 Yeah, like, you can't, like, document it, because the list is different for different Kafka versions.
And, as for getting, like, all the metric names, from the… YAML files.
It isn't actually possible anymore.
Because, there's this, one Cassandra metric that's implemented in Java.
And the name of that metric comes from Java code.
**Sylvain Juge (Elastic)** 24:54 And so, in this case.
**Trask Stalnaker (Microsoft Corporation)** 24:55 DI.
**Lauri Tulmin** 24:56 Yeah, like, the compaction progress metrics that were too complicated to express in YAML.
**Sylvain Juge (Elastic)** 25:04 And so does it mean, with the Kafka bridge matrix?
We basically capture everything, and we don't provide any way to filter to the users.
**Lauri Tulmin** 25:15 Well, the… SDK provides filtering capabilities, I think.
**Sylvain Juge (Elastic)** 25:20 No.
**Trask Stalnaker (Microsoft Corporation)** 25:21 But that would be… Sylvain, if you could look at that related to… This PR… Cause… And see if, you know, maybe there's something we need to expose.
from that SPI… to… Integrate that facility.
Where, you know, we can pass it an include-exclude, or we can ask it for its names, or something like that.
It would be very confusing if… The include-exclude doesn't work with those metrics.
**Sylvain Juge (Elastic)** 26:02 Yeah, so it actually does with this PR, but I had to, like, add a few, extra steps to first get all the handler names that are part of the rules, and then get, make the handler declare which metrics are being produced.
**Trask Stalnaker (Microsoft Corporation)** 26:18 Okay, cool. I'll look at it. Thanks.
**Sylvain Juge (Elastic)** 26:20 No.
**Trask Stalnaker (Microsoft Corporation)** 26:32 Alright.
A lot of metrics, any… Any other topics?
Anything anyone wants to chat about?
So, as far as V3, our next release is… Scheduled for… so the SDK release will be a week from tomorrow.
So, our release will be the 16th.
And I really do plan to shut 2X down with that release.
I'm tired of 2X myself. And, Whatever survives will be 3-0 after that.
Cool. Last chance. Otherwise, we can get some time back today.
**Jason Plumb** 27:48 Sounds good.
**Trask Stalnaker (Microsoft Corporation)** 27:51 Alright, thanks all.
