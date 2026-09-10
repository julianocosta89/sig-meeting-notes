SIG: JavaScript SIG
Date: 2026-09-09
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:00:36 Hello?
Trent Mick 00:00:38 Inc.
Jared Freeze (Palo Alto Networks) 00:00:45 Amazing poster, Mike.
Marc Pichler (Dynatrace) 00:00:48 Thank you.
Alright, I'd say let's get started.
Welcome, everyone.
The first topic here is… from… Amuno?
As opposed to a person who's not on the card yet.
We can… jump ahead a little bit, and then get back to this, I… or… maybe just have a look, we'll just have a look at this one. They opened the PR to add support for Nest.js 12, Component owner already revealed this one.
This is just missing approval from one approver, I'll get back to this PR after the meeting, and we'll review it.
In case anybody else has time, please feel free and also go ahead and review it, then we can merge this in.
we had the component owner map out of sync, and Marylia fixed it, so, no.
everything should be working again here. As I said, we just need to… Oh.
We just need to merge this in. I think this is what they are… what they were looking for when they wrote the clarify the unmaintained or close status. It's mostly the… Comments that were popping up here.
Alright, moving on to the next topic, I have a question about the plans for instrumentation Restify.
we had actually considered dropping the instrumentation, but, following the thread here on the issue, rest if I had a new release.
It was… I think there were no commits since 2023.
Before that, and the new release now supports also latest Node.js versions. I promised to bring this up for discussion today, if we want to keep it around or not. The person that commented here also reached out to me on Slack saying that they would be Open to becoming a component owner, because their company is… Using that instrumentation to provide support for Restify.
Trent Mick 00:04:12 I think I'm probably fine keeping it, then we could… consider dropping… Support for anything but 12?
I guess, but that would be… I guess a breaking change for older people.
Marc Pichler (Dynatrace) 00:04:27 Oh.
But so…
Trent Mick 00:04:29 people aren't using earlier versions of Restify.
And open telemetry.
Marc Pichler (Dynatrace) 00:04:37 I wasn't sure, I think I saw your, profile as one of the contributors on the Restified package. Is that… Yeah. Are you still involved with the community there, or…
Trent Mick 00:04:50 I think I may actually still be a maintainer, but I haven't touched it in… 5 plus years. Restfi came out of the company that I was working at.
break this to elastic.
So yeah.
I know it fairly well, but, I was surprised that there was another release, so I guess Netflix is still using it, because the release guy, this guy works at Netflix.
So… I don't know. We'll see what kind of life it has. But, I don't know. We're feeling out these rules, right? It's not like we had hard rules and a process to decide when we drop instrumentation or anything.
If we have an offer from someone to be a maintainer, that sounds pretty cool. I don't think the instrumentation's that complex.
And if we can drop support for old versions, then we get rid of some of the problems of, like.
Really old versions of packages, causing headaches and shared package lock and stuff like that, but… open to other people's opinions, too. I suppose we could also kick it to the curb and say, like.
Sorry, not enough users. Please write your own.
instrumentation.
Marc Pichler (Dynatrace) 00:05:56 Yeah, I looked at the package, and I think it was right now at 100,000 downloads a week.
That's not a super… Niche package, but, Close to being rather niche now.
Trent Mick 00:06:15 Yeah.
Marc Pichler (Dynatrace) 00:06:16 So what I will do is I will, let them know that… we would be looking to drop support for older versions of the package, and we'll let them know that we'd be definitely interested to have them as a component owner, and then we can figure it out from there. Does that sound okay?
Trent Mick 00:06:41 Sure, yeah.
And if you don't have bandwidth, but you notice it's sitting lagging, and I haven't gone on it, you can… You can throw it at me.
Because I've, I guess, some comfort with the Restify project that I should.
Theoretically be at a better starting point.
For reviewing changes for it.
Marc Pichler (Dynatrace) 00:07:02 Thank you.
Alright, yeah, and if we need to drop a package, we can always do that out of band, not in the SDK major version, so, F.
Trent Mick 00:07:17 Yep.
Marc Pichler (Dynatrace) 00:07:17 We aren't locking ourselves out.
Doing the change.
Alright, moving on, we have… Review request for the… Chen AI utils… I'm not sure… did we agree last week to, have Jackson, be the… taking the lead on reviewing that PR?
Pranav Sharma (Google LLC) 00:08:00 I don't think there was any, decision on who should be taking the.
Marc Pichler (Dynatrace) 00:08:05 named.
Pranav Sharma (Google LLC) 00:08:06 On reviewing, but I do have a certain amount of approvals here, I'd see a green checkmark as well. I think Ludmila approved it.
Marc Pichler (Dynatrace) 00:08:18 Yeah, I think it's, Luna is part of the TC, so, That's go ahead and checkmark our screen here.
Pranav Sharma (Google LLC) 00:08:29 if, I can, I can reach out to Jackson, and so if he approves, can this PR be merged? Because I have, yes.
like, can it be merged immediately? Because, like, I have a bunch of other PRs that are treating this as base. So, the second PR that I linked there is also based on top of this, but because, you know, we had a discussion around stacked PRs.
Because stacked PRs are not possible right now, so the diff this shows is 20 files, whereas it is actually only 2 files.
Because all the other 18 are in the previous PR.
So…
Marc Pichler (Dynatrace) 00:09:10 Yeah.
So… if you reach out to Jackson, you can also let him know that he can just click the merge button once he has approved it. He should have access to it. If not, then feel free to reach out in the OtherJS dev channel, and one of the maintainers will get to it.
If… you get it, if you get the approval today, and it's not merged by tomorrow morning, I will, merge it in then.
Pranav Sharma (Google LLC) 00:09:48 Sounds good. Thank you so much, Mark.
And again, please feel free to review if anyone, wants to. Yeah. Thank you.
Marc Pichler (Dynatrace) 00:09:58 Thank you.
Trent Mick 00:10:03 Did this one… I saw some reference in one of the PRs, I'm not sure if it was this one or one of the ones built on top of it.
wanting… Complex types for span attributes.
Before… needing dependence on that?
Pranav Sharma (Google LLC) 00:10:20 Yeah, I, I think, yeah, I opened that issue, yes, Yeah, I came across this, basically because there was no, support for complex attributes, I had to, like, manually put some parsing functionality in this PR, so I just raised a request. It's not blocking As of right now. But it would be great if this could go in. I see that,
Trent Mick 00:10:47 That's the next discussion point, yeah.
Pranav Sharma (Google LLC) 00:10:49 Okay, sounds good. Thank you.
Marc Pichler (Dynatrace) 00:10:58 Should we jump right into the widening attributes discussion?
Trent Mick 00:11:04 So, yeah, maybe I could share, because it's, like, a long doc.
walk through it, and then I can highlight stuff.
And… this is not, like, a practiced thing or anything like that. So, okay.
This is kind of a… I'll try to give an overview of what the idea for this PR is, and we've had some previous discussions about widening attributes and some of the questions around that, but then I have some open questions toward the end that I'd like other people's opinions on before we make decisions on what to do. And, like, stop me if I blow over something and you think that there's a big problem, or something like this. But, okay, so basically this comes down to supporting this OTEP. There's a blog post about it There is some argument for at least some usages of attributes in OpenTelemetry, supporting complex types.
From the language in there, it says that the OTEL API must support complex attributes on spans logs, span links, and… discriminate… yeah, well, we don't have entities yet, but basically that means resource attributes. Oh, no, actually, it doesn't quite mean resource attributes yet, but something comes down the pipe, but mostly we're talking spans, logs, and span links.
And then, for other usages, the API may support, so it's up to the implementation.
Similarly, for the SDK, it must support for the same ones we're talking about, and then may support for… the remaining types. So, in metrics exemplars, which I'm not sure we have support for yet, resource attributes, instrumentation scope attributes, and span events. The reason span events are here separate than span links is because there's a process to deprecate span events.
In favor of blog events, so kind of a less important thing.
There's another thing from the spec that I thought was a little bit interesting, and maybe… helps argue for some of the changes I'm suggesting, is that The reason that there's differences split between must and may is that the must cases are the ones where there are demonstrated use cases where we want to support complex attributes, and all the mays are like, well, we can't think of a use case for it yet, but, the SDK, if it makes sense for a particular language to just have the same attribute type support for everything, then you can do that, but… so it's a split between must and may. But one of the things said there is that if we come up with a use case, the requirement level in the spec might change from may to must, so something to think forward towards.
So, okay, the plan… As had been discussed before, and there was an early PR that was doing this slightly different, was to expand type attributes in the API to allow these types, and there are different ways you can do that.
We'll get to what I'm doing here. And then improve utilities in the core package to make it easier for SDK packages to… to cope.
There is an existing core utility called Sanitize Attributes that the SDK Trace is using, but none of the other SDK components are currently using.
And then, here's where I'm going to have some open questions when we get to .3 on what we want to do for each of those cases. Some of these cases are, like, let's talk about performance concerns, because there are some performance concerns going over all attributes coming in, and some of them are, do we want to do… For the ones that are May, do we want to support complex attributes or not? We have a… We can decide and then change later if we want to.
Okay, so mostly this is something that's been discussed before. The idea for widening attributes is to just set it to unknown, which basically, from the API point of view, is saying, send in whatever, we're fine with that, and it's up to the SDK components then to cope.
And document what they support. And by cope, that means they need to filter out attributes that they can't deal with.
And… and probably warn on them, which is basically what we've been doing right now. So there are some discussion points in there, pros and cons, but mostly that's been hashed out before. Definitely happy to have that discussion again at some point, but I don't want to blow this whole meeting on that.
One con of doing this… And probably the main one, though, in my opinion, the benefits outweigh, is that, obviously, a user Using the attributes type.
in TypeScript doesn't get any benefit of saying, so, like, if they try to send in an attribute that's a big num, they don't get a warning in.
Carlos?
Carlos Alberto Cortez 00:15:33 Yeah, by the way, something that I was… observing in other SIGs is that when they want to make a change like this, they often… Put together a blog post so people can, especially users, can come and say, you know.
whatever they want to say, in case there's a problem from their side. I don't know whether this could be helpful, and it's up to you and the maintainer, the other maintainers, but that's something to consider, in case your concern regarding breaking users is big, if you are feeling confident that It's not happening, probably not.
Trent Mick 00:16:12 Okay, one, I'm happy to do blog posts. Well, I'm super happy, I don't love writing blog posts, but, happy to do so.
I don't think there's a big concern for breaking users. Like, given, in the end, we're running JavaScript code.
JavaScript users can already pass in whatever they want through these API endpoints that accept attributes, and the SDK has already had to either cope or blow up. There are a couple of cases where the current SDK will blow up if, like, an attributes object with circular references is thrown in.
And we can talk about some of those and whether we get better at doing that. So, like, I don't think that there are breaking changes there. There was that mention of the possible breaking change towards TypeScript users, which you'd added a question of on the PR when you reviewed last week, but I haven't replied to yet.
That's something that we discussed before, and I think, in fairness, the same Marc's the dissenting vote there, but he wasn't gonna block unless he has some scar tissue from this kind of breakage before, but, The idea was to push forward with that. So, Carlos, I can… I can outline when I do finally reply, Here, comment what… what that breakage is.
happy to get other opinions, but I don't think that there's a big potential for Users seeing breaking changes from this.
Carlos Alberto Cortez 00:17:38 Yeah, and I also mentioned that I was checking any alternative SDK implementation, but I found none, so…
Trent Mick 00:17:46 No, the alternative SDK implementations are like, Datadog has… I mean, so this is referring to the scar tissue case before.
We made a change that we wouldn't have expected to be a breaking change in… our API to add… I think it was but adding an optional parameter to one of the methods on span.
Which broke Datadog's SDK, because they have an implementation of the OpenTelemetry API in their agent.
And the rule that came out of that, in which we've documented, is that SDK implementations must set, an upper bound on the minor version of the API that they support.
And the expectation is when… if and when we come out with new minor versions of the API, which is what this will be.
that they need to validate that they support that thing, make changes if they need to, and then bump the minor version in their dependencies. So, that's meant to be a gating system so that there isn't a breaking change for users.
The… the only downside that's not perfect there is that SDK implementers are meant to keep up, so relatively soon after we do a point release of the API SDK implementations, and there aren't a whole lot of them out there.
Should update.
And I think we're talking about, like, a handful of implementations, I'm guessing, like, Sentry has one as well, and…
Carlos Alberto Cortez 00:19:15 Oh, I didn't know that. Yeah, I didn't remember briefly the Datadog stuff, yeah, the Sentry one, I didn't know.
Trent Mick 00:19:23 I am not sure on that one. The Century 1 might just be a light wrapper around the, like.
Dude.
disk groups provided SDKs, so… Might be misspeaking there.
I'm sorry, their chat's been coming through, I haven't been monitoring, I don't know if I missed.
Details.
Marc Pichler (Dynatrace) 00:19:39 This was a follow-up topic.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:19:42 If you do…
Marc Pichler (Dynatrace) 00:19:42 decides…
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:19:43 On the blog post, feel free to tag me, because I'm a maintainer there, so I can help out if you decide.
Trent Mick 00:19:50 be asking you, yeah, yeah. Thanks, thank you.
Do you guys… Well, think, like other maintainers people here, do you think we should have a blog post ahead of time on this one? I expected to have a section of, like, you know we had the upgrading to SDK 2.0 guide?
there's already a start at one for 3.x. I wanted to have a section in there on this, or at least some documentation somewhere, but I hadn't thought about doing a blog post ahead of time to prepare the space for it, I don't know.
Do you think we want to be doing that?
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:20:21 This is… I don't know, I don't see it, like, as a lot of breaking changes. Might be just, like, one part of the… if anyone planning like a… blog post for the 3.0?
And that could be part of it?
Trent Mick 00:20:37 Yeah, sure, I mean, I think maybe I could. As part of I intended to beef up the migrating… migration doc, but yeah, we could get a blog post for that.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:20:48 Yeah, I can help, well, if you do, like, if you're working on the migration, I can help out with the blog post itself.
Trent Mick 00:20:55 Yeah, that'd be great, maybe we could work together on that.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:20:57 Yeah, sounds good.
Trent Mick 00:20:59 Okay, sorry, taking too much time for you to think, so… Step two was improving the core utilities, so there was an existing sanitize attribute, which was just working with the simple type, so it didn't support objects or nesting or anything like that. I have a few new methods in there. Mostly clean was to pick a different name than sanitize, so I could have a deprecated, non-breaking version and have a different name. That happened to be the same name that the Python equivalent is using in the Python SDK.
And then… these implementations, Mark will probably recognize them, add attribute, is that… basically… a slightly changed version of the one that you added to… for instrumentation scope attributes in SDK logs.
And so mostly these implementations are the same. There are some subtle differences.
Which I don't really want to get into now. So then, I also have simple versions in there, so say there's an SDK implementation, or some… one of our SDK components that doesn't want to support the complex attributes, these simple versions will accept attributes and do, basically, mostly the equivalent of what happens now, and they'll filter out.
attributes that aren't supported, and they can move on from there. So, these could be useful to external SDK implementers, or they could be useful to some of our implementations, depending on the questions below that I was going to ask.
And then I was gonna deprecate the existing ones, they won't change their behavior.
With it mostly there's a minor thing in that it actually does apply The 128 attribute limit, where it wasn't doing that before.
But I don't think that's considered a breaking change. Okay, so the questions that I have is here… here are the different places in the API where attributes come in, and for… Some of these, how we want to handle them, handle things are different.
So… In the order of, I think, interesting to discuss. So, span attributes, obviously, we want support for, and it can be a hot pass, so the ones that are hot pass there, we do have to consider performance a little bit, maybe?
And then these guys are not really hot pass, and then this is kind of a special case in that log.body is any type, it's not attributes, but it supports any type.
Okay, so Spanish Putes… Currently, just simple types. Spec says we must support So I'm proposing using this new clean attributes thing, which supports the complex types.
I'm gonna fly through this and then have a summary at the end, but if you have a question or disagree at any point, then pop in.
To do, I haven't done yet. We do have some microbenchmarks on… like, adding a span or 10 spans with 100 attributes, that kind of thing, I want to give the numbers and have a comparison there.
But I haven't done that before, except for the next step in metrics attributes below.
Okay, so currently, metric attributes, which is added when you do something like counter.record. Currently, it only supports simple types, but there are no guards on it. So, for example, if you pass in an attributes thing that has a circular reference, it crashes the SDK.
Spec says we don't have to support right now, and frankly, supporting really complex attributes and metrics is crazy, but I suppose people can do it.
I had a question if someone knows right now, was having no filtering on the metrics intentional, or is that just… a matter of history. It feels like guarding against weird attributes was added into SDK Trace, and then the other SDK components came along, and we didn't really…
Marc Pichler (Dynatrace) 00:24:39 I'm not sure if it was a conscious decision, I seem to remember that at some point we decided that, It's the user's responsibility to adhere to the types, and the performance Benefit of not validating was… helping that case somehow. Yep, yep, okay, so… But I don't… require any, written-down discussion on that decision.
Trent Mick 00:25:13 Okay.
So there is a counter-add benchmark for basically this, this kind of case.
And currently, with no filtering, We get, like.
40 million ops per second, so… What is that?
So, like, 2.5 nanoseconds or something like that. I might have to be off… off by one. So, naively just doing clean attributes, that does cycle checking, which is actually pretty expensive, it's about 10 times slower.
I did play around with a, you know, a guard that doesn't bother doing cycle checks, because… maybe we just say that that's Caesar's responsibility, basically the current state, and I could get it back up to 15 million per second, so maybe that's something that we want to consider or not.
Then, there's a question of whether, like, 10 times worse seems awful, but maybe that's… Micro… optimization that doesn't relate, or premature optimization is the word, because we're still talking sub-microsecond for counter.add, but I don't really have a good real world.
Since then.
Marc Pichler (Dynatrace) 00:26:18 I was at the Node.js Collaboration Summit, this year.
earlier this year, and one of the discussions, or some of the discussions that I had was around the metrics SDK.
And… Some of like, many opinions were around… So… performance of, counter-ed, and, like, or the other… Or the other methods, so, yeah, other instrument types, and people said that the way that it is right now is already Not good enough, and it should be quicker.
So… The same precise there is, from people that are very concerned about performance, so I don't know if that also applies to everybody, but there's definitely people out there that would say that it's… That's a big hit.
Trent Mick 00:27:22 Okay. So, I mean, I would be cool as a path in this change, if we're okay with going forward with this change, in not changing anything there. So, we would document that metric attributes only support simple, and you really should only do simple, and the OTEP actually has some suggested language.
As does the… the blog post that was… OpenTelemetry blog posts done at the same time, basically saying, like, don't use complex attributes. There are specific cases where we want to support it. For complex things, doing AI, some representation is one of them, but you're crazy to do them in metrics. And then not add any guards, and we could explicitly say this is for performance reasons, and that we That is performance sensitive, so we don't want to do it. And if it blows up, then it's up to the user to… To deal with that, that's considered a programming bug.
Marc Pichler (Dynatrace) 00:28:10 Yeah, I think what we can do with this is also start supporting complex attributes once we have bound instruments.
Because with bound instruments, you'll do the cycle checking once on instrument creation, essentially.
And then once you add something to a counter, for example, you don't add attributes anymore.
Which, makes the whole case a bit easier to say we support complex attributes there.
It forces a down instrument.
Trent Mick 00:28:44 The value of the… Attribute doesn't change either.
Marc Pichler (Dynatrace) 00:28:51 Independent.
Instruments.
Trent Mick 00:28:53 I have a separate bound instrument for… so if I have a, like, an HP… response time metric, Instagram, and I have one for when it's a 404, one for when it's a 500, and one for it's a 200. That's 3 different bound instruments, then, is it?
Marc Pichler (Dynatrace) 00:29:09 Yeah, exactly. You would have, one attribute set would equal one instrument, and.
Trent Mick 00:29:16 Okay, so then it's no longer a hot pass, so we're good.
Marc Pichler (Dynatrace) 00:29:18 Yeah, exactly.
Trent Mick 00:29:20 Okay. Okay, that sounds great. So, could reference bound instruments. Do you happen to know if there's an issue open for that? You're gonna have to go look, I can find it.
Marc Pichler (Dynatrace) 00:29:28 Don't think there is… specification is merged already, I think.
Trent Mick 00:29:33 Okay.
Okay.
Okay, next one, log record attributes. I'm suggesting not changing anything other than changing over to the newer shared implementation of… basically, clean attributes is moving functionality that was in SDK logs over to core, so it can be shared by other components.
I did have a thing about us approving our log stuff, in that I have a guess that the… Guarding that we do for cycle checking on attributes?
means that logging through the logs bridge with the OpenTelemetry SDK logs thing is probably much lower than it is for just the logging frameworks on their own, but I don't know that anyone's done A performance comparison on that, so… I don't know if… might… my vague understanding, only from people's comments, not from looking at code, is that some of the other languages, for example, Go, have decided to be skirting the… some of the spec.
things, some of the spec language to make sure that their logging bridges can be fast, so I think there are things about Maybe not enforcing the… Read-only log record or something like that, so they can avoid copying attributes and things like that, so… I don't know. But anyway, I'm… in this PR, I'm not proposing changing behavior at all, other than where the implementation is.
K… link attributes, I think we should… treat exactly the same as span attributes.
Event attributes, so here's a question. Do we want to take… we have an opportunity here to say… the spec says May. We have an opportunity here to not.
Increase the behavior of what you can put on span event attributes.
If we do this change, and if we use… This clean attributes, that means that we're supporting complex attributes on spend, event attributes. Do people particularly care one way or the other?
Marc Pichler (Dynatrace) 00:31:48 Slight preference towards not, supporting it, but, no strong preference either way.
Trent Mick 00:31:56 It's easy to add later rather than take away, so we could do that.
Okay, cool.
That's what I wanted to hear.
Same question for instrumentation scope attributes. That's a May.
the only place we support instrumentation scope attributes right now is in SDK logs, because that's where… Marc, you did the guinea pig implementation of this. You supported complex attributes there, because we were in just key logs.
We could go simple, we could back off on that.
Because I can't imagine there's a user out there of instruments scope attributes, so… breaking change to an experimental package, but, like, no one's going to be broken by it.
Do you have an opinion?
Marc Pichler (Dynatrace) 00:32:38 Like, the simpler ones, I think that should be okay.
Trent Mick 00:32:46 Going back to Simple?
Yeah, okay, cool.
Resource attributes. So right now, there's no guarding on resource attributes, you can shove whatever you want through there. There's an argument to be made that… resources… From code, or from custom detectors.
Should be intelligent enough to not be passing in weird stuff, so that maybe there isn't as much of a need for guards on that.
And so I was proposing not changing the current behavior. There's a little bit of complexity in this. The resource package can't share the current implementations in core, because resource attributes have these Maybe promise things for async attributes, so, there's a little bit of complexity there, and the easy out was to just not guard behavior at all and just document.
that it's the user responsibility for passing in. If people are doing config from NVARs or declarative config, there's no way to pass in silly attribute types, so basically for people using that path, it's… everything's fine.
It's only someone doing something crazy in code.
Okay… Go ahead.
Marc Pichler (Dynatrace) 00:33:57 That one will throw, red, or will, Will it?
Throw something that's, actually crashing the app.
Yeah. Because the promise is not… So there's no, exception handled on the promise.
Trent Mick 00:34:23 Well, there's no exception, Heller, in the metrics one, either.
This one… actually, okay, so, sorry. There's a crasher in metrics, because it doesn't do guard. If you have a circular reference in your thing, it will… Actually, there are two crashes there. One, a circular reference will… get the maximum recursion depth error. We'll crash the app.
The Prometheus exporter, when it's trying to JSON.stringify the attributes, will blow up on something like a big num, because JSON.stringify and a bigum blows up.
That's where we had a potential, if we cared about that, to have some kind of… guard there. We could either do no guarding at all, or we could do this clean, simple attributes, which will remove big nums and objects and things like that, and you don't need to do cycle checking, because none of the types in simple attributes can recurse, so… I don't have to have that. Back to resource attributes, there are two crashers here. One is, it'll crash if you do circular reference in this thing. It'll also crash if you have a I think he crashes on a big numb as well.
I can't remember, I have to check that one again.
Marc Pichler (Dynatrace) 00:35:34 I think, validating in… Resources from attributes is a good idea.
And do you think we should, like, the full validation.
Because it's not the month of birth. Yeah, yeah.
Trent Mick 00:35:49 Okay, cool. So, I'll change that recommendation. I'm cool with that.
Klog record body, I just wanted to mention a special case, because it touches on any type, but I don't want to change this behavior for… for it. Right now, it does no filtering at all, so you can crash. It passes through whatever garbage, and then it's up to the exporter to cope.
I need… exporter serializers don't currently guard against circular references. I suppose that's a separate discussion if we wanted to do that.
The equivalent in, like, logging frameworks, like Pino or something, is they all use some, third-party JSON package that does do circular reference carding.
Okay. So, here's a summary. I think we had… we were gonna go… Everything as described here, except we're gonna change resource attributes to do the full guard.
Simple for these two cases.
If that sounds… Reasonable to people.
Marc Pichler (Dynatrace) 00:36:48 Freeze number to me here.
Trent Mick 00:36:51 Cool.
And then there was one final thing that I wanted to point out, one I referenced above a little bit, that there are subtle differences.
One of them is that… I wanted to change the, like, is any type to say false for undefined. Right now, undefined is passed through as allowed, but… It's sometimes later code and sometimes not that deals with that. So right now.
I guess, before I give an answer, if you guys want to think quickly what you expect these things to do.
Okay, so right now the behavior is that in set attributes, not in the… not in the guarding of the attributes type, in set attributes, it'll ignore this one. So the only attribute that gets set here is foo.
In here… Actually, I can't remember what happens, but what I want to change it to is so that any of the gardening that we do will drop these out. And that allows… We already have a number of instrumentations that, when they're setting span attributes, they will be passing some values with undefined, because it just… it's easier in the code to build up an attributes thing, that some of the values come back as undefined from the helpers, and then they just get thrown away by said attributes. If I want to do that in the filtering so that we consistently, in all these cases, will do the same thing.
It's just that we have way more instrumentations dealing with span attributes than we do with log events or with counteratt.
This does mean changing a side reference in the spec that talks about undefined as the JavaScript empty type, where really null is the empty type.
So I was gonna have an update to spec for doing that.
If you have spidey scents, tingling, going off, that kind of thing, then please review my PR when I actually pull it out of draft.
Okay, that's it. Sorry, I've taken too much time.
Marc Pichler (Dynatrace) 00:38:51 I think about the last part might be worth talking to Dan.
I think he… was talking about that part of the spec at some previous SIG meeting, so it might be good to think with him.
Trent Mick 00:39:08 Okay, cool.
Okay, yeah, Jared noted, so… I haven't tried out the… my changes with any of the browser instrumentations, but I don't expect anything to break there.
I guess on to the next…
Marc Pichler (Dynatrace) 00:39:32 Yes, I'll share again.
Trent Mick 00:39:35 Thanks.
Marc Pichler (Dynatrace) 00:39:38 Right.
The next one, also… Question, or, like,
Trent Mick 00:39:48 As ever, this is…
Marc Pichler (Dynatrace) 00:39:49 Previous.
Trent Mick 00:39:50 Nothing new on this one, nothing's happened there. Marylia and I are having an arm wrestle on that one, just to quiet on the side thing.
Other people's opinions would be welcome.
Marc Pichler (Dynatrace) 00:40:00 Yeah, unfortunately, didn't have time to look into that, but it's definitely my list.
Trent Mick 00:40:06 Thanks.
Marc Pichler (Dynatrace) 00:40:13 Alright, does anybody have any… opinions about the previous PR.
If not, please review and comment on the PR.
Alright, moving on to Jared's topic.
Jared Freeze (Palo Alto Networks) 00:40:29 Yeah, quick question. Maybe better on Slack, but… I want to make sure that if we have big changes, they make it into the new release.
Even if we're not totally ready.
So, two questions. One, do we care? Like, is it okay for, you know, in… two months from now, to deprecate when we do have a replacement for any given package that's sitting in Core or Contrib.
Or, yeah, because it's experimental, like, is there, is there any rush?
Right? So the option would be wait, kind of do it the right way, which is deprecate on the day, and then give guidance to go to browser, or deprecate now, just so There's a bit of a warning, you know, but then we don't have guidance to provide.
You know.
Marc Pichler (Dynatrace) 00:41:25 So, I suppose we're talking about the instrumentation packages here, right? Or is, that also SDK Trace Web?
Jared Freeze (Palo Alto Networks) 00:41:35 Yeah, Trace Webb. Also, there's, like, Browser Detector. Like, there's a few things.
Marc Pichler (Dynatrace) 00:41:39 So I think…
Jared Freeze (Palo Alto Networks) 00:41:39 core, I think that do need deprecation, but we haven't, like, for that one, it's really utility, but I'm not even sure we really decided what to do with it.
But the idea is that we know they're gonna be deprecated, we just don't know where they're edited necessarily, like, there's some open questions. Also, they're not one-to-one, right? So, like, browser fetch is a completely different shape.
And so, I don't know, there's a lot more docs that need to be there, but I guess really what my question is, is there any urgency to depregate these before the release goes out?
Trent Mick 00:42:19 I don't think so.
It would be… I don't think we get blocked on the… I mean, you know, it'd be nice if we could drop SK TraceWeb now, but I don't think we get stuck.
Do we have… Yeah, I don't know.
So I think… so I think we could get away with deprecating those things later, if we're not ready to provide a pointer, like… Here's what you replace it with, or a migration guide.
Because it sounds like you might even want a separate, like.
okay, the browser SIG feels like we're at a point now where we're ready, and you have a focused, kind of, here's the migration story for everything.
And it doesn't have to be perfect, right? This is… Open source project with maintainers with limited time, so, like, if the fetch isn't one-to-one, then so be it.
Do you agree with that, Marc? Do you…
Marc Pichler (Dynatrace) 00:43:16 Yeah, I think there's… So if we know that we're gonna drop something, I think it would be fine to just put the deprecate, annotation on there.
And that in itself will already… Send users our way that are interested in keeping it around, and we can use that for further discussions as well.
So… I'd say there's no rush to deprecate the browser packages, but if we do, then, Earlier is better.
But you'd be completely different.
Trent Mick 00:43:55 aggregate them now, even if there's not a…
Marc Pichler (Dynatrace) 00:43:57 Even if there's no replacement for it, it, like, at least gets the word out.
Trent Mick 00:44:04 Jared, is there a, like, a landing spot in the browser repo docs that we could point to? Like, here's the plan. We know it's not ready yet, but deprecated, and here's what to expect.
Jared Freeze (Palo Alto Networks) 00:44:15 Yeah, there… there is a… there is a holding ticket for… the list, there's, like, a status list. We've got a table going of all the packages, I just realized, I really like that idea, Mark, of sort of poking people to be like, hey, comment, comment. But I will say, I think there's a few vendors that are using auto-instrumentation web.
Which is a mix of things that are deprecated and not deprecated.
So we'd have to make a decision on what exactly the content of that is, and what the status would be, because I think it's kind of, you know, it's mixed, right? So, I don't think we should say, like, hey, don't use auto-instrumentation web, because there's still some bits left in it.
That definitely needs more discussion. I don't… we don't have to go over that now, but, that's just something I thought of. But I do like your idea of just following it out now with a comment that's like.
You know, browsers moving in a different direction, something like that.
For the link.
I can take that back to the SIG. I mean, I know David's here, too. Like, I don't want to step on anybody's toes. David will just tell us. But, I just wanted to get some feedback.
Marc Pichler (Dynatrace) 00:45:35 Alright, yeah, thank you.
Maybe while we're at the topic of the browser packages, so… looking through the milestone, the current plan is to keep the instrumentation fetch and XHR packages around, right? So they will go into the… 0.300 line of experimental packages, and we're still continue.
maintaining them.
And the SDK Trace Web we're gonna drop, and move the utilities over to the Web Common package. That's the proposal that, David put up.
Other than that, I don't think we're dropping any browser-specific things, right?
Trent Mick 00:46:30 I hadn't thought of the browser detector, I don't know. I haven't looked at anything there.
Can we… if we move the instrumentation utilities to Webcommon.
Can we drop SK Choice Web yet, or is it… Premature.
Marc Pichler (Dynatrace) 00:46:44 Yeah, that's… I think mostly a question for, Jared and David.
I think the stack context manager…
Trent Mick 00:46:57 Right.
Marc Pichler (Dynatrace) 00:46:58 Was the one thing that was in… Yeah, I think the Web Tracer provider didn't do anything more, anymore. It had the register function, or the register method, but that one can be easily replicate replicated by, Fantastic.
Trent Mick 00:47:17 docs, yeah, users.
Marc Pichler (Dynatrace) 00:47:18 about.
Trent Mick 00:47:19 this stuff yourself, yeah, yeah.
Marc Pichler (Dynatrace) 00:47:21 And the instrumentation utilities were the main thing why we kept it around still, which is kind of an anti-pattern, reading the specifications, so…
Trent Mick 00:47:32 So, Stack Contact Manager, can we just point people to the thing that's in the browser web SDK?
If you need to use it, just use that one.
David Luna Bistuer 00:47:41 The context manager is the default in the SDK.
So, unless you pass anything else, the stack context manager is… is the default one. So that component is already moved.
All from the… from the SDK3 as well.
There is a PR, sorry, I'll put here in the document, there is a PR about… that moves the… add span network events, so DC 3D functions to add network events to the spans, and actually querying the resources.
Those were in the ZK3s web, I created the PR to move to the common web common package.
If that lands, then I think we are in good shape to… to remove the indicator as well.
Perfect. We're good.
Trent Mick 00:48:29 Okay, another question, then, is docs in OpenTelemetry.io still talk about using SDK Choice Web? Do you think we'd be… or the browser group would be in a position soon to update those docs to use the browser SDK, or is that, like… well, that's hard, because we're not totally ready, and it's certainly not.
And apples to apples change, because the instrumentations are quite different.
David Luna Bistuer 00:48:53 Yeah.
Yeah. It's not quite different.
Trent Mick 00:48:55 See the smile.
David Luna Bistuer 00:48:56 People are different in, well, basically, as Jared pointed in the chat.
Browser now, it logs, logs and logs.
So it changes a lot on the data model.
So yeah, you can rewrite the computation for that, but then… The outcome is that they will get a different type of data.
So maybe, I don't know, maybe we should add some kind of a… Well, maybe extend the documentation.
Saying that we are moving to a logs-based SDK.
And there's an experimental, and then maybe, you know.
Marc Pichler (Dynatrace) 00:49:36 I'll update the issue to make sure that we think about that first before dropping it, because it seems to be a larger topic, and then we can discuss on the respective PRs.
David Luna Bistuer 00:49:49 Yep.
Marc Pichler (Dynatrace) 00:49:53 Right.
Thank you.
Western's comments.
Thoughts on this?
If not, then I guess we can move on to Marylia's topic.
Yeah.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:50:13 This one is just an FYI, more fun things on the word of people using AI is that we got a few repos, mostly Collector, that we had… contributors opening issue, but the issue is, like, very simple, but they use, like, the hidden comments on HTML, and it's just, like, a bunch of curl with scripts to, like, scrape all your information, environment variables from your action and stuff like that. Yeah, we are, like, banning those users whenever they come along, but just an FYI to keep an eye when you're… if you're using agents to just, like, read issues and fix things for me. A lot of them are actually able to cut this type of thing up, but just… Just an, yeah, an alert there.
Marc Pichler (Dynatrace) 00:51:00 Yeah, thank you for letting us know. I've seen a co-worker of mine send us a screenshot of like, how that looks like, and it's very difficult to spot, because, as you mentioned, these are hidden comments, so it's not even… you don't see it in the text, it's just a comment in the markdown, so…
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:51:22 Yeah, I think, like, one of the users were easy to spot, because I think they accidentally also put on the title of the issue the command, so, like, why they're putting this, and then you look at all the things that they are open, like, okay, then close all of them, like, yeah.
Marc Pichler (Dynatrace) 00:51:39 Yeah, thank you for, the warning.
Matthew Wear (Dash0) 00:51:42 I'm just curious if this is something that can be, like, automated, checking this?
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:51:50 So yeah, I'm thinking if I can do, like, Put something on the shared workflows repo that is just, like.
basically see if there are any, like, hidden comments on issues, and then alerts, like, hey, pay attention, something is there, but…
Trent Mick 00:52:06 Our PR and issue templates use comments, so… Yes, we do.
away from that. So I'm assuming there's a huge body of ones that do have them already.
Not ones that say… Well, maybe we can, like…
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:52:20 One of the parameters can be, like, ignore those things, because usually we have, like, the text of…
Trent Mick 00:52:28 You can allow list certain ones, yep.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:52:32 But still, not an… not an easy thing. It's just, like, pay attention, I guess. No.
Fun things, yay!
Marc Pichler (Dynatrace) 00:52:45 Alright, guess we can move on to the next topic, This was raised in chat earlier, there's a question about the… JSON file exporter, and I think the answer is we haven't, looked into that one, or adding that one yet.
It's definitely on the to-do list, I'm not sure, how far along the spec for it is, if it's already stable or not.
I think there's still an issue around for it somewhere.
Trent Mick 00:53:20 Bhaskar, I was on that other call when you brought this up in the spec, or maintainers.
You're proposing adding an implementation for this, right?
I, I think that would be… I… Mark, correct me if I'm wrong, I think that would be totally acceptable for us to take an experimental implementation of That, exporter type, because it's in the spec.
Marc Pichler (Dynatrace) 00:53:43 Yeah.
Trent Mick 00:53:44 I haven't looked.
Marc Pichler (Dynatrace) 00:53:44 I think that makes no sense.
Trent Mick 00:53:45 I think it's still in development status in the spec, but it's only because it just hasn't moved forward.
Marc Pichler (Dynatrace) 00:53:51 Yeah, huh.
Trent Mick 00:53:51 But yeah.
except Piercelyn.
Marc Pichler (Dynatrace) 00:53:54 Yep.
And I think in terms of how we should design it, we should… maybe have one, package that's just the OTRP file exporter.
Instead of one per signal, to keep things a bit more simpler this time around.
And we've tried all the different ways of structuring exporters. Hoping this one will stick.
Trent Mick 00:54:25 Yeah, next year?
We'll fix all that.
There's so many pairs that keep coming in for exporters, too.
Marc Pichler (Dynatrace) 00:54:34 Yeah.
But I think having it at one separate package that does logs, metrics, traces, and having it be tree-shakable, would be… Would be good enough.
That's…
Bhaskar Banerjee 00:54:48 posted.
Marc Pichler (Dynatrace) 00:54:48 seated up per signal.
Bhaskar Banerjee 00:54:50 Yeah, that's how it is in Java and Python as well. If you see the link I shared, Marc.
The one for Python is also in a single package.
I don't… I don't have the link for Java handy with me right now.
But as I've worked on it in the past, I know that's also a single package.
Marc Pichler (Dynatrace) 00:55:16 Yeah, exactly, so I think that's also what I would prefer, to just have the single package, and not have it, depend a lot on What we've already done with the exporters.
Ideally, it would also not, have, any reference to mvarconfig, but mvarconfig would be handled by the, configuration package and the declarative config things. Because that's also one of the troubles that we've had with the exporters, is that they read environment variables by default now.
And apply the config, so merging it together with file config is difficult.
So initial implementation would be great if it would just omit all of that.
And… Just take a plain config.
And then we can still decide on, like, if we need to have an environment Weber config in the package, we could.
just add that later, but in an initial implementation, I think, would be good to, not have any M4 config yet.
Bhaskar Banerjee 00:56:23 Okay, sure.
Point taken. So, the committee would be open to accept an issue followed by a PR on this, right?
Marc Pichler (Dynatrace) 00:56:32 Yes.
Bhaskar Banerjee 00:56:34 Boom.
Thank you so much.
We'll be on it. Thank you. And come back to you guys.
Marc Pichler (Dynatrace) 00:56:40 Yeah, thanks for bringing that to the SIG here.
Trent Mick 00:56:46 Relatedly, because you brought it up, Marc, on the environment variables in the exporters, there is a PR that someone submitted from that.
Which I think was… AI-assisted, but, it was so big, it scared me away, because there's so many packages in there, it had to be big, but I don't know.
If… If someone has a chance to go through that, it's a slog.
Marc Pichler (Dynatrace) 00:57:11 Probably that one, right?
Trent Mick 00:57:13 I think so, probably.
Yeah.
Marc Pichler (Dynatrace) 00:57:20 It's,
Trent Mick 00:57:22 partially, I think it builds on it. Like, somewhat design-wise, it's adding band-aids.
To the… because, like, they're the band-aids of the… Functions that are being used that have the word legacy in them, and this one's adding a Similar kind of stuff.
Marc Pichler (Dynatrace) 00:57:40 Yeah, I think it's trying to… Keep this shape of config.
I think it would be easier to not keep This config shape, and just use the underlying config shape, of the different components.
And merge these together.
Because then you don't need the translation from… This, legacy thing to the underlying config.
So my plan when I was working on this was to then eventually get rid of this legacy config.
And have a separate constructor, or a separate, Factory function that just creates an exporter based on the underlying shape, rather than… The old one.
would be, the big breaking change, essentially, in the end.
Because when I did the refactoring, I, spend a lot of time trying to minimize breaking changes to users that would use an exporter normally, which is just instantiating it and then adding it to a span processor or a metric reader or something.
Trent Mick 00:58:59 Do you think it's unavoidable that we have breaking changes in that?
Rehash?
Meaning, it's not gonna happen September, so… meaning next year.
Marc Pichler (Dynatrace) 00:59:11 Things.
Trent Mick 00:59:12 We could do it.
And these are all solicitor.
Marc Pichler (Dynatrace) 00:59:14 We can't avoid it.
Trent Mick 00:59:15 everyone.
Marc Pichler (Dynatrace) 00:59:15 Yeah. I think we can avoid it. But… We're at the point where there's so much code needed to make that happen.
That it would just be better to have one New entry point of creating an exporter.
Probably end.
Trent Mick 00:59:36 field.
Marc Pichler (Dynatrace) 00:59:37 And deprecate the old one, and then eventually forward it all, or… In the future, remove the old ones.
And in the meantime, then declarative config can also use that new, way of creating things.
Trent Mick 00:59:53 Yeah, absolutely. That's what I expect.
Okay.
Marc Pichler (Dynatrace) 00:59:59 If I find some time, I will also have a look at that PR, it's… fairly large, but I guess it's just doing the same thing.
Multiple times.
Trent Mick 01:00:07 time.
Marc Pichler (Dynatrace) 01:00:08 Yeah. Yeah.
Alright, looks like we're out of time already. I think we got through.
For the topics… So, thank you everybody for joining.
Have a nice week, and see you next week.
Trent Mick 01:00:26 Thanks, Trevor.
