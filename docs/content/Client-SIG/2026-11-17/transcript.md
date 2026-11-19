SIG: Client SIG
Date: 2026-11-17
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba (Raintank, Inc. – Grafana Labs)** 00:58 Hi, Michael.
Well, it's gonna be just the three of us.
I haven't heard from Hanson.
**Jason Plumb (Splunk Inc.)** 01:45 I was around yesterday for the Kotlin call.
There's an empty agenda. Do the… do those, Prs from last time, are those still around? Looks like they might be.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:02 Oh, it's… yeah, actually, you know what? This is supposed to be from… for today. I… I didn't change the date here.
**Jason Plumb (Splunk Inc.)** 02:10 Oh, I see. And I copied it unnecessarily. Let me delete that. Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:18 Yeah, I mean, I guess we can talk about these. So, I think the only thing that we have in progress right now is… Still the migration of the… Client-side semantic conventions from the core registry.
Which is… let me share my screen really quick.
Paints here.
Which is, yeah, this… These are sub issues. Actually, these are… These are the PRs in the core registry to deprecate them there. I have approved these, and they need to happen first before, Before we can add them to our registry, kind of like we did with end user. Hey, Hanson.
So all I'm asking here is just if you have time, can you just stamp these? I think they're pretty straightforward. This device one.
It's obviously, relevant to mobile… to your mobile folks, the session button and app onto.
And once these are merged, we'll just… I think we have actually corresponding PRs in this registry, in the client-side registry, that can follow immediately after these are merged, so…
**Jason Plumb (Splunk Inc.)** 03:47 Well, and then after some amount of time, presumably… They'll get removed?
Deprecated is one thing, right? But then eventually they're gonna get removed?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 03:59 well…
**Hanson Ho** 04:02 I… Don't think they're ever removed, right? I think they always say, stay deprecated. So, in theory, if you include deprecated, attributes, you can use them in… in perpetuity, I think.
**Jason Plumb (Splunk Inc.)** 04:20 So they will exist in two places in perpetuity.
**Hanson Ho** 04:24 The keys will, but the… it'll be like, you know, foo exists as a deprecated attribute in core for 1.44, but it'll exist as a live attribute in client-side, you know, 1.0 or something like that.
**Jason Plumb (Splunk Inc.)** 04:43 Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:46 I mean, they actually moved to a target deprecated folder.
**Hanson Ho** 04:49 sooner.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:50 And they're, like, marked as duplicated, so I think Weaver doesn't include them.
**Jason Plumb (Splunk Inc.)** 04:57 Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:58 Yeah.
**Hanson Ho** 04:59 I think the generated source will, though, like, unless you explicitly exclude deprecated, I think that key is still available, right? Like, if we build, or if somebody generates, you know.
conventions based on a repo that has deprecated attributes, they should still show up unless they filtered them out, right?
**Jason Plumb (Splunk Inc.)** 05:24 I don't know the answer.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 05:27 I don't know either. I mean, I just… so I don't have a lot of experience with Beaver, to be perfectly honest, but I… I thought that this, like, they… first of all, they're… annotated is deprecated, and they also excluded from resolution, so…
**Hanson Ho** 05:41 Okay, okay, cool.
I think that's fine, this has changed to the core repo, right? Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 05:52 Yep, yeah.
Anyway, yeah, if you have… if you can just stand these three, that'd be great.
**Hanson Ho** 06:03 Don't do that.
**Jason Plumb (Splunk Inc.)** 06:04 Seems doable.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 06:09 And we have… Shit.
And I didn't… I don't think these… the iOS and Android are being moved yet. I don't know if you… Would prefer one of you two.
To take this on, Hanson.
**Hanson Ho** 06:38 I can do that, I'm finally sticking my head out of, out of, whatever I was in, I… I sent 3 pull requests yesterday, for updating some info stuff. So yeah, I can… I can do that, this week.
**Jason Plumb (Splunk Inc.)** 06:54 Hanson, do you anticipate that'll basically be the same… does the deprecation then work effectively the same way, where we will still have these conventions defined in Android? They will just be annotated as deprecated?
**Hanson Ho** 07:07 Yeah, so, however… excuse me.
however Martin deprecated the other ones, I'm gonna deprecate the ones, in the same way, so move it to deprecated, and kind of keep it going on, yeah.
**Jason Plumb (Splunk Inc.)** 07:21 Okay, I just wish we could clean that up at some point.
**Hanson Ho** 07:25 As in, like, erase them from existence?
**Jason Plumb (Splunk Inc.)** 07:28 Yeah… Yeah.
**Hanson Ho** 07:30 These are… So, the ticket is just for the Android namespace, right?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 07:36 Yep.
**Hanson Ho** 07:37 we probably have some… actually, do we have some attributes in the Android project that we can erase? Because I think… I think the ones that have been published in the semantic conventions will… those are gonna live in perpetuity somewhere, so I don't think we can get rid of those, but I think the things that we have internally in Otel Android, the ones that are, don't have a namespace or whatever, that stuff, I'm more thinking of just getting rid of and not deprecating.
**Jason Plumb (Splunk Inc.)** 08:11 What's the… why is it different?
**Hanson Ho** 08:14 Because somebody out there would be consuming the, core Android, semantic conventions, assume… I assume they would be. Versus, I don't know how many people are consuming the OTEL Android projects, internal semantic conventions, and saying, hey, is there…
**Jason Plumb (Splunk Inc.)** 08:32 There's something that… you use the word internal, which I think is important. Is there something that designates them as internal?
**Hanson Ho** 08:39 That we never published it in a version.
That is independently consumable from a registry, like, the…
**Jason Plumb (Splunk Inc.)** 08:48 Okay.
Like…
**Hanson Ho** 08:49 I think what the federated semantic convention registries, we have versions, and these are public, and, you know, even in dev, we probably can't get rid of it. But I don't believe we've ever published a semantic convention for… the conventions in the Android project that states that we have a version that you could depend on in perpetuity. So I think that's the difference. It's like unofficial, almost. It's in the telemetry, so there's always that, like, you know, somebody depending on Android telemetry, depending on that.
But they would be depending on the version generated, by some Android, instrumentation, rather than some semantic invention. So, I'm hoping we could, be a bit more, not cavalier, but, We can throw away some garbage as we move, you know?
**Jason Plumb (Splunk Inc.)** 09:42 Does this… does the existence of this or this make you sad? This is brand new, right? Like, I think this might make me sad, then.
**Hanson Ho** 09:52 But is it a registry, or is it artifacts? Because those artifacts will always exist. That's not a problem.
**Jason Plumb (Splunk Inc.)** 10:01 I guess I'm not clear on the distinction. This is definitely artifacts.
**Hanson Ho** 10:06 So, what I'm thinking is, is actually not artifacts, is, is registry, entries.
**Jason Plumb (Splunk Inc.)** 10:13 What does that look like? I'm… there's a gap in my brain or something.
**Hanson Ho** 10:17 in the YAML, it's defined, and it is published as a version.
**Jason Plumb (Splunk Inc.)** 10:25 So I don't think… like, if you go to here, for example, I don't know… Yeah, we don't, like, have an explicit, like, semconf… Exactly. Offset or anything, but… We do have YAML… Right, like, we've got…
**Hanson Ho** 10:44 Not a register.
**Jason Plumb (Splunk Inc.)** 10:45 tough…
**Hanson Ho** 10:47 I don't think we have a,
**Jason Plumb (Splunk Inc.)** 10:50 This thing…
**Hanson Ho** 10:53 But it's not a ref. It doesn't define, like, a schema URL.
Hmm.
**Jason Plumb (Splunk Inc.)** 10:59 That was defined up here.
**Hanson Ho** 11:05 Oh, wait, hold on. No, no, this is… this is just cons… soup.
Okay,
**Jason Plumb (Splunk Inc.)** 11:11 We declare this, right?
But whether or not this is, like, consumable, I guess I'm unclear on what that means.
I do like that, you know, I click on this and I get a 429, that's pretty sweet.
**Hanson Ho** 11:28 That's unexpected.
**Jason Plumb (Splunk Inc.)** 11:29 Yet another thing that's down today… I guess this might be the beginning of the end, probably? Just… Time to go out, walk into the woods for a while.
**Hanson Ho** 11:38 airplanes. Yeah.
I will take a look, I thought we never… published it.
which was what I was depending on,
**Jason Plumb (Splunk Inc.)** 11:54 Yeah, I guess… yeah. So, I mean, the answer is we don't know yet, but it sounds like we might have to also keep them around.
**Hanson Ho** 12:00 Yeah… unless some of them violate… Meetingspace rules, but getting stuff out of… the… so I think… I think there's two things here. One is getting stuff out of the Android namespace, which follows the regular deprecation process that I can do this week.
how we deal with these, conventions that we have living in the nether regions, whether it's considered, public inversioned, I think that's gonna be important, because… I hope no one is using that stuff.
At least not as semantic event in registries and generating, you know, constants based on them.
**Jason Plumb (Splunk Inc.)** 12:43 It does seem unlikely.
**Hanson Ho** 12:46 You can always do it and then restore it if, if someone complains.
Or we carry them forward,
**Jason Plumb (Splunk Inc.)** 12:53 Or we delete it, and when they complain, we say, upgrade.
**Hanson Ho** 12:57 Yeah, there you go.
**Jason Plumb (Splunk Inc.)** 12:58 other ones. I don't… I mean, that seems pragmatic to me, but I know that we like to talk about Stability a lot.
**Hanson Ho** 13:06 Well, I think that project, we never declared that stable, so…
**Jason Plumb (Splunk Inc.)** 13:11 by default.
**Hanson Ho** 13:14 So…
**Jason Plumb (Splunk Inc.)** 13:14 Yeah.
Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 13:22 You're muted, Michael.
**Hanson Ho** 13:23 book.
**Michael Bushe (Mindful Software, LLC)** 13:27 Hi, I think the reason why stability is so important came up in some of these failures that have been happening over the past week. It's amazing how So many well-known failures are due to bad telemetry.
And… the worst… some of the worst failures, and I'm trying to think of what this was this week, it was some kind of an electrical failure, somewhere along the line. And there was some telemetry that the device… that the, whatever was reading it thought it was getting, but it wasn't getting it anymore.
And big, big catastrophe, because, you know, the plane thinks it's at a particular altitude, and it's not, right? You know, that's not quite the best example, right? And so that's why the stability is important, so we do have to respect that.
It's hard.
**Hanson Ho** 14:20 Yeah, no, I mean, I think anything that we say is published and stable and has a version, that has to be kept up, and I think those are the Android namespace conventions, like, we can't get away from that. I think we're trying to kind of be a little bit… a little bit pragmatic is, whether we've declared, the hotel Android internal semantic conventions as something that is public and stable.
I would think that, at most, the instrumentation version and what that records, that relationship probably is something that we may want to kind of upkeep. Like, if we go from version 1.9 to 1.10, and we change the attributes we write, that is probably going to be a problem at the instrumentation level.
But… Nothing in 1.9 says There is some independently consumable semantic invention tied to that instrumentation that will be kept up going forward. So… Stabilization is, in my mind.
at the instrumentation level, and at least for now, and I'm hoping we never, in the hotel Android repository, have semantic conventions that are independent of the instrumentation that we have to declare stable one way or another. I think that stuff should go into the client-side repo.
**Jason Plumb (Splunk Inc.)** 15:41 I'm into that, yeah, I think that's fine. Like, keep… keep the semantic conventions entirely separate from the repo. I mean, yeah, that's kinda… if that's the new home for it, that's great. I'm fine with that.
**Hanson Ho** 15:54 Okay, yeah, I can start picking up.
**Jason Plumb (Splunk Inc.)** 15:56 There's still, like, the specific namespace, so… Yeah.
**Hanson Ho** 15:59 Yeah.
**Jason Plumb (Splunk Inc.)** 16:00 Yeah, okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:05 And you have that schema that you have in your Android.
repo like that, you're not actually sending that schema right now with your telemetry, are you?
**Jason Plumb (Splunk Inc.)** 16:15 I don't think so, no.
I don't think any of the instrumentation is really good about setting schema URL at all.
**Hanson Ho** 16:26 Yeah, and then… Schema UL's also kind of problematic, since we're talking about one set of telemetry, or so one set of instrumentation, that could be potentially depending on several registries, so… how do you set one URL unless that URL… and these are federated by design, so I can't include, like, there is no stable version that is tied to a particular version of Client Side, right? So, we actually probably need, a set of URLs, for instrumentation, if we are…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:00 My set, sorry, my set of URLs.
**Hanson Ho** 17:03 because, say we have some client instrumentation on Android, we depend on client-side version 1.0, and we depend on core version 1.44, what URL do we include when we say, the schema URL is… this URL.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:20 But there's a… there's a… oh, okay.
**Jason Plumb (Splunk Inc.)** 17:22 dependency. Like, I think we only depend on the client side, and the client side has a dependency on core. Isn't that the way that works?
**Hanson Ho** 17:29 No?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:30 What it is, no?
**Hanson Ho** 17:33 a client-side can reference registry, or a client-side event can register… can depend on the, specific version of Core.
and reference those attributes, but the dependency isn't transitive, so if…
**Jason Plumb (Splunk Inc.)** 17:53 Got it, yeah. So, like, a given project could still take two dependencies, is what you're saying?
**Hanson Ho** 18:00 Exactly, exactly.
**Jason Plumb (Splunk Inc.)** 18:01 And we expect Android to also need to do that.
Yeah. Yeah. Okay.
**Hanson Ho** 18:09 So unless Andra publishes… some…
**Jason Plumb (Splunk Inc.)** 18:14 I've showed come up before.
**Hanson Ho** 18:18 I can ask, but, my understanding, and hope to be wrong, is… is… maybe there's a gap in the API.
**Jason Plumb (Splunk Inc.)** 18:31 Are either… are any of you attending the Semantic Convention SIG?
**Hanson Ho** 18:36 I assume.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 18:36 That comes true.
**Hanson Ho** 18:38 plan to, but Mondays are generally… yeah.
**Jason Plumb (Splunk Inc.)** 18:40 Yeah, yeah.
**Hanson Ho** 18:44 I can ask in the, in Slack, and then, you know, basically go and ask if we have instrumentation that has… depends on two registries, what do we put in there? And maybe the answer is no one puts that there right now, so…
**Jason Plumb (Splunk Inc.)** 18:57 I mean, that's definitely a gap in my understanding of the design, the architecture. Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 19:03 And so I'd just like to, like, make sure I understand correctly. So, like, you could have… Are you saying that you could have a dependency, obviously, on client side, because you're pulling in some attributes or some events from there, but you could also, like, be pulling in directly some events from the core that are now referenced in the.
**Jason Plumb (Splunk Inc.)** 19:20 Likewise.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 19:20 That's the case.
**Jason Plumb (Splunk Inc.)** 19:22 Yeah, totally.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 19:23 And you have something like that? Like, because we have… So we have, like, browser-only events right now.
Right. But the…
**Hanson Ho** 19:32 But don't the browser events pull in core attributes, like session ID?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 19:36 Dependency, yeah.
**Hanson Ho** 19:37 Yeah, so, so, but… If you have instrumentation that references an event defined in core that is not in browser, then what does that tracer or that logger report as its schema, right?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 19:55 Yeah, that's… that was… that was what I was thinking. And you have some things like that? Some events that you generate from?
From the car? I mean.
**Jason Plumb (Splunk Inc.)** 20:04 I would anticipate it. I don't know that I can think of one off the top of my head, but it seems like a very likely scenario.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:10 Okay, okay, alright.
**Hanson Ho** 20:12 It is unlikely that all of the attributes or the events that we get will be from one registry.
**Jason Plumb (Splunk Inc.)** 20:18 Right, yeah, that's what I'm thinking, too.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:21 Hmm.
That's interesting, so I… It's not guaranteed that, like, one SDK will use only one registry.
**Jason Plumb (Splunk Inc.)** 20:27 Yeah, exactly, that's… that's what… yeah.
**Hanson Ho** 20:30 Well, I mean, this federated stuff is being retrofitted into something… it means 2.0 for a reason, right? So it's almost like… schemas, need to kind of, you know, be effectively that. I mean, I can take a look. Maybe they've actually changed that. Maybe in the API definition, the schema returns a list, in which case we are able to do that. But I definitely don't think we do it right now, so…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:59 And then there's also the question of, having the dev schema and the stable schema.
**Hanson Ho** 21:05 Yes, that is at least easier to kind of wrap my head around. Those are effectively, different… they're different schemas. So if you depend on the dev schema, you're going to get more attributes. If you depend on the stable schema, you get fewer attributes. And those versions are… I don't think, are even… don't even have to be aligned. Like, there doesn't have to be a stable for a dev, or rather a versionless for a dev. So it's… you can almost consider them, just, you know, string keys that are unique and that follow, follow Semver, in, in, in incrementing, But beyond that, it's… it's… the relationship is, well, Dev probably is a… I can't even say that. Dev is a superset of stable, unless those numbers match. So if you depend on Well, certainly, I think we can say that a version that… for dev, after an older version, is going to be a superset. But the relationship between stable and dev, I think, is undefined. At least if you have two… two schemas.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:19 Okay.
**Jason Plumb (Splunk Inc.)** 22:22 I think it'd be important for us to make sure we understand the design.
**Hanson Ho** 22:28 Yeah, a lot of this stuff is… changing, too. I actually have a change for… for Weaver. I was gonna push up, but yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:39 So I'm looking at the proto, proto for the, And it, yeah, from the OpenTelemmetry Proto, and… The schema is on the scope, yeah, so it's like the instrumentation scope?
**Jason Plumb (Splunk Inc.)** 22:51 Yeah, and there's just one.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:53 Oh, okay.
**Jason Plumb (Splunk Inc.)** 22:58 Alright, I have to drop. I will try and take a look at those SEMCOMF PRs, this morning, but…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 23:06 Alright. Jason, see you.
**Hanson Ho** 23:07 Hey, thanks.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 23:09 Ryan, see you later.
**Hanson Ho** 23:10 Okay, bye.
