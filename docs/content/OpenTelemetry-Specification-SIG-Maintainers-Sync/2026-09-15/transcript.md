SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-09-15
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Reiley Yang (Microsoft Corporation)** 00:23 Hey, Florian.
Gosh.
Tony?
**Florian Lehner** 00:28 Hello, my name.
**Josh Suereth (Google LLC)** 00:30 Woman.
**Reiley Yang (Microsoft Corporation)** 00:30 Whoa.
Okay, I'm sharing. You see my screen?
**Florian Lehner** 00:46 Yep, looks fine.
**Reiley Yang (Microsoft Corporation)** 00:48 Thank you.
Hey everyone, thanks for joining. While we're still, like, having folks joining the meeting, please take the time to put your name on the attendees list, and if you have any item, add to the agenda.
Thank you.
I guess we'll start probably in 2-3 minutes.
Hey everyone, thanks for joining. We'll start in less than a minute. If you haven't put your name on the attendees list, please do so.
And any, like, discussion topics, please add to the agenda. Thank you.
Okay, let's get started.
But we're.
**Robert Pająk (Splunk Inc.)** 03:45 Hello, hello.
You can share.
So, this is just a reminder. So, there is a section about attribute and attribute collection representation for non-OTL protocols. This section has been up for… a pretty long time, and nobody said that it was… nobody objected that it… there was nothing controversial here. The only ask for stabilizing it so far was just to have prototypes for more than one language, because before it was only Go, so I… I just kind of just a… or a feasibility, like, a feasibility VPR for Java, and Jack repeated that it's not, like, idiomatic for Java, but Jack approved that it doesn't… it is not a blocker, and yeah, it's implementable, and I think Jack sees no reason to block stabilizing it, and we want just to have it stable, just to make sure that it's nothing controversial, and the package is stable, and it's the only way, so we can, have it in go. And then other languages may, but don't have to also follow the same… the same, principles.
Yeah, and it already has four approvals, I think we can just wait for one a week, and I'll just merge it afterwards, if nobody will object.
That's everything from my site, unless someone has questions for this one.
**Reiley Yang (Microsoft Corporation)** 05:23 Okay, I'll add a comment here.
And I'll check by end of the week. If there's no outstanding comment, we'll just merge it.
Thank you.
And for Maintainers, if you haven't… Take a look, please.
Okay,
**Robert Pająk (Splunk Inc.)** 05:41 Next one, I put 10 minutes, just if… because I have no idea if it will be… how long will discussion take, maybe between 2 minutes, maybe it will be 15, but I… but let's timebox it at, maybe for 10 minutes, preferably.
So, we have been talking about, kind of, having limits, or… quite a long time, and I just… it's a little bit kind of worms, in my opinion, because we, there were some specifications which is stable, and says that metrics and resource attributes are exem… are, like, are kind of exceptions for these limits, but I am not sure if changing this, we should not change it to just be more defensive and more secure by default, and I'm kind of leaning that changing this, I don't know, kind of specification could be seen as a bug fix, more or less. Just make sure that it will not break the users in a standard way, so I'm here just trying to get feedback what are, especially the language SIG Maintainers, what are… what language SIG MA turnners think about it, because I think that if people will be affected, then, the language SIGMA Tainers will be the first line who will be, be blamed for any… any kind of changes in this area. So, yeah, I… I kind of think that… The change here impact… like, the default limits are pretty high.
So, I think if people are hitting those limits, probably will be… will be aware even before, even… I think we'll have even issues, saying… I think that even before the traces and logs, if people complain about the limits, the defaults, I think we'll have issues even before people asking what's going on, and I never heard about any issues so far, that even something disappears And that's why I think that even if we retain the defaults for metrics and resources.
No, maybe not for… I think even for resources, I think that the chances that it will be a problem are pretty low.
But, yeah, let's double check, maybe… maybe we'll need to check with the collector, with the… with the telemetry, what is… what is the length of some attributes, but yeah, if you have any feedback here, I'll… yeah, I think it's worth… Trying to progress this one.
Any feedback?
Do you, any feedback, anyone?
**Liudmila Molkova** 08:31 Robert, if I understand correctly, that the most concerns come from the resource and metric attributes?
This is the current…
**Robert Pająk (Splunk Inc.)** 08:41 Yeah, this is the only thing in the specification which says that the limit attributes are not, kind of.
are, are not subject to these two signals. This is the specification, what it says right now.
the reason for resources is that initially the authors thought, probably, that the telemetry, even if it will be big, it will not be repeated in… it will be only, like, repeated in each request of OTLP, but it doesn't mean that it can be just too big.
you know, as a principle that we should not have unbalted data. For metrics, the reason was, I think, the identity of the measurements.
But if we have so many attributes, we have already the cardinality limits, so I was thinking about having some precedence and trying to have similar mechanisms to the cardinality limits for metrics.
But I have no strong opinion. I think that others here, which were working on metrics, may have better, better suggestions and answers here.
**Liudmila Molkova** 09:50 Yeah, so the… the… it sounds like it's the… the… We should compare the experience of somebody who receives an ginormous metric or a source attribute Versus potential breaking change by having a limit.
And… The experience is probably awful anyway.
**Reiley Yang (Microsoft Corporation)** 10:17 I can see different principles. I think the first question is, do we agree that everything in software should have a limit?
I think, yes. The fact we never thought about a certain limit is going to cause us problems. I remember, like, we added the OTLP request and response limit, because initially the response didn't have a limit, and then people worry about, hey, what if people give you a response that destroyed your caller?
could be a security issue. So, I guess I would prefer to say all the software designs should have limits in place. If we don't have a limit, that's a bug.
I want to see if people have different opinions here.
**Robert Pająk (Splunk Inc.)** 11:00 I think Tigran and everyone agreed with this. It's just about finding a way how we progress, what… how we want, you know, go forward.
**Reiley Yang (Microsoft Corporation)** 11:09 Okay, then the second question is, if we agree every software design should have, like, limits, then do we want to put a default limit, or we should say, by default, there's no limit, but we gave you the necessary tooling, so if you want a limit, you can specify the limit. And things can get tricky.
If initially we don't come with the default limit, then it could be a… maybe breaking change for people who use the extreme case. So I… I can… I can share what I learned from .NET. So, when we were implementing some of the OpenTelemetry stuff in the .NET runtime. I joined their architecture, like, forum. I think one principle they have is .NET runtime doesn't give you any defaults.
limit when it comes to, like, the telemetry scope. Like, if you can… you can add millions of attributes to a SPAT, and that will naturally become very slow. Of course, they will do something making sure it's, like, log N, or maybe, like, linear, or n log n, whatever. That's reasonable. They're not going to punish you.
But they don't put an artificial limit, because they're saying, depending on which area you're coming from, your expectation of the default could be very different.
And whatever default we put there, we believe 50% of our folks would find it reasonable, and 50% folks would find it, like, very ridiculous. So we'd rather not put the default and have a natural, like, way to give you this performance feedback. And we want to enforce limit or something. In the OpenTelemetry.NET SDK, people can do that, but the .NET runtime won't do it, so… I think that's one philosophy. Do we want to take the same philosophy here?
I'm curious, like, one approach I can imagine is OpenTelemetry won't give you any of this limit by default, but it gives you this configuration where you can enforce the limit, versus we try to dictate what should be the default.
Because I think if you have a… a big spectrum of users, the expectation. Like, if they're on mobile, they will think, oh, your limit is too big, if they're working on big machines. And also, over time, the limit might change. If you look at, like, the software 40 years ago, maybe people think, like, 64 should be the default limit.
But later, with AI, like, that number will change, so do we want OpenTelemetry to be in that game of, like, 10 years later, we just realized, oh, we have to change the limit because the world has changed.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:31 I think… I think, You know, there's sort of an emerging consensus that we made a mistake by having resource attributes, metric attributes, and scope attributes exempt from these limits.
And now we're trying to figure out what to do. And we can talk about, like, what would reasonable limits be, but, like, the more tricky question is navigating from, like, having no limits as the default to having limits, regardless of what those values are as the default.
And what further complicates it is, like, not only are there no limits applied to resource metric and scope attributes, but there is no way to apply limits. So, like, even if a user wants to apply limits, they can't.
That is pretty awful.
**Robert Pająk (Splunk Inc.)** 14:41 So, my thoughts on this are currently that, I haven't seen any concerns so far for the default limits, so I would probably… this will be probably what I would start. And I also thought about adding some special attributes that will indicate that these limits have been reached.
at least for… for sure for metrics, maybe for resources as well. I have no strong opinion here. Like, some marker attribute.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:14 So, when the metric, limits are reached, I think we have… sort of a concept to deal with that. That's sort of like a runtime level limit, so, you know, you don't encounter it once at startup. You encounter it potentially many times at runtime, and we have the overflow concept, and I think there's probably a nice way for metric attribute limits to sort of coalesce into that, so that we just kind of co-opt that mechanism instead of inventing a new one.
And,
**Robert Pająk (Splunk Inc.)** 15:42 That's what I described, yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:44 Yeah, yeah. You know, scope attributes are somewhat in between. Like, you can initialize scopes at runtime, but many, many are initialized sort of statically, or maybe not statically, but at initialization time.
And then resource attributes are obviously mostly, like, at initialization time. And I'm wondering, just, like, just off the top of my head, if we can take a lesson from what we did with, with complex attributes.
You know how complex attributes, we're like, hey, we're never gonna do this. And then we're like, hey, we're gonna do this, because we don't think that it's breaking, actually. And we… we set, like, a date on the calendar, where we said, at this point in the future, we're gonna start doing this thing. We are gonna start, like, emitting complex attributes.
I wonder if, like, that's a way to sort of navigate this, like, this question of, is it a breaking change? It's like.
we sort of do some research and say, it's probably not a breaking change for most people, but we can't guarantee it's not a breaking change for all people. But we couple that with, like, a date on the calendar. So 6 or 12 months in the future, we say, like, we're gonna switch this.
**Robert Pająk (Splunk Inc.)** 16:52 Specification, yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:54 Yeah.
**Liudmila Molkova** 16:55 I think the tipping point was when we realized Like, 90% of backends handle it gracefully already.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:05 Yeah, and I think this will be a little bit different from complex attributes, in that, like, there will be some… real users that, like, that have resources that exceed the default limits, or have metrics that exceed the default limits, because the default limit is… has a count limit of 128, and so, like, while it's unlikely that you'll have a resource with more than 128 attributes, it's non-zero. And the same goes for, like, metric attributes as well. So, like, it will affect some people, but I think the case that we would need to make is that It's… it's a really small proportion of users, and that there's fair warning, something like that.
**Reiley Yang (Microsoft Corporation)** 17:50 Okay, we have one minute left.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:54 I would love to see this happen. I don't know how we make it happen. It seems like kind of a tricky coordination problem, where somebody has to kind of champion it. You know, Robert, I don't want to volunteer you to champion it.
**Robert Pająk (Splunk Inc.)** 18:05 I will try. I'll do my best.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:08 Yeah, like, and if you do, like, I'll be supportive along the way, because I would love to see this happen. I view it as a mistake that we let metrics, scopes, and resource attributes be exempt from these attribute limits. That was, like, sort of a mistake we made in the past, and we're gonna have to pay for it now, I think.
**Reiley Yang (Microsoft Corporation)** 18:30 Yeah, same here, I'm supportive.
like, I keep saying, like, if we don't have limit in the first place, we'll regret and we'll fix that as a bug later.
Okay, so, let's move to the next summary.
**Severin Neumann (Bronto)** 18:45 Yeah, hi, everyone.
So I thought we, as SIGCOMS, bring this topic, to the Maintainers meeting. I mean, I shared it in the Slack channels.
But you might have seen or heard that, that, like, we started to stop taking in There are some issues for the registry and a few of the ecosystem pages.
Because we currently struggle a little bit to keep up with them.
Now it looks like, well, we know that, like, some SIGs take dependency on it.
And we're just figuring out how to move forward with that, right? I mean, as you know, we have the Ecosystem Explorer as an additional project right now.
But it's far, far away from Replacing the registry, and we also don't want to put the burden On doing that, on the project that soon.
So yeah, right now we're just seeing, like, okay, what's… what's the way forward? So… I don't know, the one thing I'm really asking for is, like, any… any feedback on that, anybody who says, like, hey, we are just fine to… to let it go, or if there's anything where we say, like, hey.
This is something crucial we need to think about a different way, how to… how to move forward with it.
**Reiley Yang (Microsoft Corporation)** 19:57 I have a question. Is this purely driven by the lack of, like, enough energy to maintain this, or this is, like, we don't see much value there?
**Severin Neumann (Bronto)** 20:09 I mean, it's a mix of both, so to speak. I mean, the main driver is that, I mean, we have two Maintainers stepping down recently, we have a few other ones that have personal reasons for drastically reducing their time in contributing right now, but if you look into that issue.
That are linked there.
Patrice also did a quick look into… into the Google Analytics numbers.
So if you scroll down a little bit… So there is… No, it's more up, I think it was, like, one of the first or second comments, maybe it's hidden already.
Oh, it's somewhere there still.
Oh yeah, met a lot of… conversation going on. There it is, yeah, this table. You see, like… Like, in a month.
from across, like, 700,000 views, Right about 10,000 went into the registry.
So it feels neglectable.
But at the same time, we also think that, like, for some people, it's very important.
So yeah, we, we just… try to figure out where to go from here, right? So… Yeah.
**Liudmila Molkova** 21:25 Severin, I'm curious, what type of registry, requests are the most common? What people add? Is it instrumentations, backends? You don't know what?
**Severin Neumann (Bronto)** 21:37 Yeah, so, I mean, one thing is, like.
For, like, everything that lives in our own repositories, we kind of semi-automate it, like, taking that in, so if there's a new collector, receiver, or whatever, like, in the core repositories, we take this in.
But what we also see is an uptick of, like, external… Tools, instrumentation libraries, of course, vendors that want to get listed.
There's a long, long list of vendors. As you might know, there's, like, a hundred-something entries right now.
Yeah, so I think there's a bunch of, like, other people that say, like, hey, I built something around OpenTelemetry, I want to have that be added to the registry, right?
And we, like, looked at the things that we maintain right now, and are just, like, looking at the things that we want to stop doing to win more time for other things, right, that are a little bit more important for the SIG to take care of.
**Reiley Yang (Microsoft Corporation)** 22:38 I'm curious about the bar. If someone reach out saying, like, I have this OpenTelemetry XYZ plugin I want to add.
do you see the Maintainers trying to evaluate or something? Or maybe, like, later they'll come and say, no, we realize you're trying to inject some virus here, we're going to remove.
**Severin Neumann (Bronto)** 22:55 Yeah, that's maybe, that's maybe, like, I think you're touching upon another very important thing, like, of course, like, the one thing we do is, like, the moment someone, something, hands something in, we follow their GitHub.
link, and it looked like, hey, is this… is this legit? But… but we are not, like, doing any… let's say, proper maintenance on it, right? So we could not even say, like, hey, someone submitted something, and then waited for 3 months, and then turned that thing into something malicious.
It's not something we really are really doing, right, with anything third-party right now.
**Reiley Yang (Microsoft Corporation)** 23:30 And you probably don't have the necessary, like, tools and support to be able to even do this job.
**Severin Neumann (Bronto)** 23:36 Yeah, yeah, the thing is, like, the registry, if you look at, like, how it is built, since the website is just a static static page generated from Hugu, it's a bunch of YAML files that we're just parsing and pushing in.
So we build a bunch of tooling around it, but it's not really like… let's say, very sophisticated, right? And that was one of the ideas why we also kicked off the Ecosystem Explorer because we wanted to have something separate, but at the same time, this thing is more around the things, and Jay probably can speak better to that. But this is more, right now, focused on the things that we have in our own repositories, right? Everything that that OTEL provides, as a project, and not, like, have a place where people can drop off the stuff that they're doing.
**Reiley Yang (Microsoft Corporation)** 24:30 Yeah, and any Maintainers found it, like, very useful for your… Like, company or something.
Any, like, major concern if we're going to take this down?
**Jason Plumb** 24:43 I wouldn't say major, but I do find it useful. I refer to it, I don't know, probably a few times a month, when responding to questions from, like, sales and support folks, who are looking for support for a specific Library, the ecosystem has been very helpful in that regard… for me.
Also, Severin, I thought it was interesting that 10,000 views a month was not a big number for you.
**Severin Neumann (Bronto)** 25:09 Compared to the 700,000.
**Jason Plumb** 25:11 Well, yeah, well, compared to the front page of Google, it's nothing, but…
**Severin Neumann (Bronto)** 25:16 Yeah, no, but I think that's what I tried to express when I said, like, it's from those 700,000, only 10,000, but I assume that maybe some of them are very fond about it, and you just… Like, gave me that evidence that there's, like, maybe people in every… in every vendor, they'd say, like, hey, let me check if library X, Y and Z has support for that, so… So this is the kind of evidence that we're looking for, because, like, from those 10,000, we cannot say, like, hey, is this just bots and crawlers? Which is probably also, like, a big chunk, but if we have evidence that there's, like, people in different Vendors that say, like, hey, we use this to check, like, if we go to a customer to check, like, if we support the stack that they have.
That's definitely an important piece of information.
**Jason Plumb** 26:06 Well, I'm glad to add my one data point of using it a few times a month.
**Marylia Gutierrez** 26:10 But even, like, on your example, that is kind of, like, one of the points. You're going there.
trusting that the information there is 100% accurate. So that is kind of like the point, like, if people are opening, saying, like, hey, this component I'm adding there, and it's compatible, we are not really, like.
going deep and checking if there is really compatible. So, that is the point, like, we are creating something, and people are assuming, like, oh, I can really trust this vendor is, or I can really trust this plugin, and they might change, and we don't have anyone who's actually providing this actual check. So, it is a hard one.
**Michele Mancioppi (Dash0 Inc.)** 26:45 I also used the registry like Tyler, I think, said, but I don't take it at face value. It's more like a list of pointers, and then I go deeper into… into double-checking what the thing is doing, right?
**Severin Neumann (Bronto)** 27:01 Yeah, no, that's… that's… but yeah, what Marylia said, right? I mean, we… and that's why we also want to have, like, something for the things that we provide out of the project.
in the ecosystem explorer, because those are the things that we can… that we can validate and build checks around it, right? But it gets much, much harder with the wider ecosystem.
But yeah, I think that's definitely a fair data point.
**Liudmila Molkova** 27:33 I don't have a super strong opinion whether we need to have it right now, keep it, and… or… or… keep it frozen, but I think we should think how we solve it in the long run.
And I think the… we need to find ways to offload the verification.
And the effort to, like, comply with something to the people who submit for requests?
And… We can do this for instrumentation libraries to a certain extent with the conformance repo we have now.
It's relatively easy to send a PR to add a conformance test. We need to add some policy on what conformance means for instrumentation library.
And, like, the… the lack of violations in this test.
Can be a signal that this library Should be in the registry.
Or some certain score.
This is not a lot of work to do.
But it's definitely something that… that needs some work from… from… us in the conformance repo from OpTele.io.
develop this policy. But in the long run, How can we afford this?
to people who send PRs.
**Reiley Yang (Microsoft Corporation)** 28:57 Or alternatively, I wonder, like, something like Wikipedia might also work. You could put whatever information there, then people can use AI to process the data and evaluate that. Or maybe we can even have a scoring system. Each component can be sponsored by someone, and if it's sponsored by a product maintainer or TC member, GC member that has established a reputation in OpenTelemetry, then you got a higher score.
Then people kind of, like, understand where this component is coming from and who's behind that.
**Severin Neumann (Bronto)** 29:32 I mean, I'm all open to that, but that brings me back to the initial thing, why we started to… to freeze it for now, right? I mean, retirement is still the thing that we're, like, debating.
I mean, someone has to take care of that, right? So one option that we put out is like, hey, should we move the registry into a dedicated repository and see if there's people that want to take care of it independently of the website, and then, like, give it, like, its own place to live?
but yeah, I mean, I'm very open, or we are very open to ideas here.
But at the end, it's more like about doing it in a sustainable way.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 30:20 Am I correct in saying that the Ecosystem Explorer is the, you know, is the natural successor to the registry? That's the idea in my mind. Is that how you think about it, Severin?
**Severin Neumann (Bronto)** 30:33 To some extent, yes. I mean, eventually we want to have it that way, but the thing is, like.
We don't want to put that pressure on that project right now.
Because the moment we say, like, hey, you need to be open to accept whatever language, whatever thing anybody's, like, dumping right now into the registry, into the ecosystem explorer, I'm… I'm… I'm… I'm very, very worried that this would break the whole project, right? Because, like, I think they should… the Ecosystem Explorer project should focus on doing good work now for the things that we have inside OTEL, and then later we can take a look into that.
And it's the same problem right now, right? I mean, there's, like.
a handful of people taking care of that, and the other thing is, like, yeah, it's a big question of capacity and bandwidth that someone says, like, hey, I'm… I'm taking care of that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:32 But what the Ecosystem Explorer has going for it is that it's a blank sheet of paper, and so we can use the lessons from the registry to, you know, in the first draft of whatever the Ecosystem Explorer does. Like, you know, for example, this idea Liudmila was talking about, which is, like, using conformance as a gatekeeping or an automation mechanism for controlling, you know, which entries show up in a registry.
where I'm saying, like, it could be the registry, or the Ecosystem Explorer, which is, like, you know.
successor to it. And so, yeah, I'm not saying, like, you know, just, you know, point the fire hose at the Ecosystem Explorer. I'm saying, like, can you… can we, like, you know, build in this gatekeeping slash automation mechanism into the ecosystem Explorer today?
**Severin Neumann (Bronto)** 32:21 Jane.
**Jay DeLuca** 32:23 Yeah, so, The establishment of the conformance project really, just ties in really nicely with where we're going with it, so… Yeah, just to step back, the ultimate goal is for this to be kind of the ultimate replacement for the registry, but yeah, as Severin mentioned, due to just bandwidth and capacity issues, we're focused on kind of native OTEL components first, and we want to expand outward. That's saying that, you know, if some… group of people came, and they were like, hey, we want to help push this forward, like, by all means, we just don't have the hands, to kind of focus on it right now. But yeah, the kind of marrying the data of kind of the metadata layer of the various components with The semantic convention's conformance data is certainly completely feasible, and we will be doing it with the Java libraries very soon. So, That will be great for all of the existing stuff that we have, and it will also provide a roadmap to onboard these other things. For example, the Conformance Project already has all these non-OpenTelemetry native GenAI libraries that are already being tested.
And we will pull those into the Explorer. So that will kind of be the first foray into potentially exposing non… Native hotel things, but… Yeah, so just to summarize, absolutely, we want to, incorporate the conformance stuff into this, and we will automate as much as possible, and set up these gates so that it should set up for longer term, being able to onboard whatever, so as long as they pass the tests.
**Reiley Yang (Microsoft Corporation)** 34:06 Okay, so I'll take the last question from Tad, or comment.
**Ted Young (Raintank, Inc. – Grafana Labs)** 34:11 Yeah, just a quick comment that, you know, we… I hear some reluctance to make an official plan around this, but mostly due to a lack of resources. But conformance and especially something like the Ecosystem Explorer, these are actually the kind of projects that end users tend to be more interested in getting involved in, in my experience.
If we actually put together, like, a roadmap and a plan and a proposal and, like, get it out there on the blog, that could actually help to get, more people involved in helping out with this stuff.
So, maybe it's just a suggestion to maybe, like, reverse the flow there, and not say we're promising anything on a timeline, but, you know, just that if we actually have a coherent plan, that could lead to getting more help.
And it sounds like Jay's already on this, so awesome.
**Reiley Yang (Microsoft Corporation)** 35:10 Yeah, thank you. Okay, let's move to Carlos.
**Carlos Alberto Cortez** 35:14 Yeah, just a smaller one.
Sorry, sorry for that, sorry. Yeah, so I'm just trying to bring attention to this PR, just trying to clarify the expectations regarding SDK and application, and we don't have to go over that, but I would like Maintainers to take a look, especially that there's a point, an important remark that Chuck did.
Regarding that some… currently, some auto-instrumentation, implementations may actually fail completely, like, not failsafe, but completely fail if there's something that doesn't work well.
I don't know whether we actually have many Maintainers here. I know that some maintainers Don comas softenos.
they wish.
**Reiley Yang (Microsoft Corporation)** 36:04 For this type of broadcast, do we have a way to tag the Maintainers, like, if they don't join this meeting?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 36:12 I did tag them in the comment that is linked to there. I haven't heard back from any yet, but it was a relatively recent comment just yesterday, so…
**Trask Stalnaker (Microsoft Corporation)** 36:21 Slack channel, is generally the best that I've found.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 36:27 The Maintainers channel, or going to the individual language ones?
**Trask Stalnaker (Microsoft Corporation)** 36:30 No, the… just the hotel Maintainers channel. It feels like we get pretty good, response there.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 36:42 Yeah, so I'll do that. I'll repost this comment to there, but I guess to elaborate on this problem a little bit.
This PR is not from me, it's from Michele. He's a co-maintainer in the injector project, and what we're trying to do is we're trying to create a set of normative requirements for what it means for a particular language to be auto-injectable. And the reason that this matters is because projects like the injector and the operator, they need a contract like this that they can rely on. They need the behavior of languages to have, you know, some set of normative requirements, some semblance of coherence and consistency that all languages could, you know, perform.
And, you know, probably the most controversial requirement in here is the one that I call attention to, which is that an auto instrumentation should under no circumstances crash the application.
It doesn't seem controversial, but it is controversial, because many of our auto instrumentations don't do that. Instead, when you install them, they're guess and check. And what I mean by that is you install them, and you turn on your application, and you see if it breaks.
And if it doesn't break, then great, you can continue with it. But if it breaks, like, you have to investigate the compatibility issue. So, I think that's a problem. And, you know, I know other people do as well. And so, you know, what we're trying to do, amongst other things with this, is, like, sort of codify at the OpenTelemetry project level.
That, you know, auto-instrumentation should not break applications.
**Michele Mancioppi (Dash0 Inc.)** 38:32 Thanks, Jack, for bringing the PR to the round.
It's, I cannot stress enough how important it is for Automatic injection, not to break applications, because it is a massive loss of trust.
Doing automatic injection is the best way to get people to a nice baseline of observability without much work.
But if stuff breaks, then, the OpenTeentry brand.
is affected, not only the bad experience of the individual. This is why it is so important That we err on the side of caution, and that we take safety of instrumentations As a non-negotiable.
**Reiley Yang (Microsoft Corporation)** 39:19 Jason?
**Jason Plumb** 39:21 Yeah, I think that in concept, this is great stuff, I think we need to be careful and make explicit the distinction between auto-instrumentation and auto-injection. I don't know if that's been made clear enough in some of this, pros, but I also, question whether or not we need to consider build time auto-instrumentation.
So this is something we have in Android, where we inject instrumentation into application code at build time, and… I think we've gone out of our way to try and not break apps, but I cannot guarantee it, and there might be some cases where we want to fail a build, and failing a build is probably very different than failing runtime. So, those distinctions might be helpful. That's all.
**Trask Stalnaker (Microsoft Corporation)** 40:09 Just a little, historical context. I think the… I mean, I kind of understand why some of the languages wanted to do FailFast, like, there's a nice quality about FailFast, when you're thinking about, you know, you add the auto instrumentation locally, or to, you know, your one app, and, you know, you find out, you know, you're… you're in the dev cycle, you find out right away. But I think the… the auto-injector stuff, and the helm chart, and those things.
are a whole… bring a whole different perspective there, that these are things that are, you know, the flag is set at, like, a fleet level, and, like, all of us, you know, it… it cannot fail at that point.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 41:05 Exactly. You know, think about the operator. You're saying, install OTEL instrumentation across my entire cluster. And, like, you know, what we, the vendor that I work for, Grafana, have been, you know, doing is we've been trying to develop mechanisms that, like.
detect that an application crashed because OTEL instrumentation was installed, and revert it.
And you have to do all this complicated bookkeeping, and the experience still sucks for the user because their production app still broke. But it's, like, I guess it's better than not reverting and, like, crashing continuously.
But it's a bad situation, and that's how we should be thinking. That's what… that's what, that's what's gonna take OpenTelemetry Mainstream, is when there's simple tools to be able to install cluster-wide.
**Reiley Yang (Microsoft Corporation)** 41:54 Thank you. Okay, Robert, I'll take your comment as the last one. I have to move on.
**Robert Pająk (Splunk Inc.)** 42:01 Yeah, I think that's really… you can also, correct me if I'm wrong, but for instance, for .NET automatic instrumentation, it's not nearly possible to do the must-not, because you're changing the .NET runtime, the .NET runtime, very, like, settings, and if you just do it wrong, or by mistake, or whatever, then it will just crash. Or if you also add some unsupported thing on some unsupported system, it will break as well. So putting must not is impossible, in my opinion, to enforce.
**Michele Mancioppi (Dash0 Inc.)** 42:34 So…
**Robert Pająk (Splunk Inc.)** 42:34 And I think it should be listened to Mr. Shouldn't.
**Reiley Yang (Microsoft Corporation)** 42:41 Yeah, this is why I put it, should not. Okay, let's move on. Stephanie?
**Liudmila Molkova** 42:46 W-wait, I think this… I think must not.
is valid. It's a bug if you don't follow it, and if you can… you cannot prevent it from happening, ever. But if you notice it.
You should fix it, even if it's a breaking change.
**Robert Pająk (Splunk Inc.)** 43:10 I mean, sometimes we cannot control it. Sometimes it's… we cannot change the runtime, Boten's runtime, right?
**Liudmila Molkova** 43:18 All you can not to break.
**Robert Pająk (Splunk Inc.)** 43:23 Yes, but then it should not, because we cannot enforce it.
**Michele Mancioppi (Dash0 Inc.)** 43:27 For example, something… sorry, something that the .NET instrumentation, to the best of my knowledge, doesn't do is to have a two-stage loading, where first validates the assumptions, and then it activates.
That kind of two-stage loading saves… it effectively makes most things.
catchable in languages like Python, and we did it in the packaging SIG.
**Robert Pająk (Splunk Inc.)** 43:50 I'm 90% sure that you're not right. There's a configuration setting, which is, like, fail-safe or something like that, and you can configure it.
**Michele Mancioppi (Dash0 Inc.)** 43:59 I think…
**Robert Pająk (Splunk Inc.)** 43:59 by default. Right now, if you make, like, an auto, not proper, I think it will crash by default, but right now, I think you can alter this default, or maybe it was the other one, but I'm pretty sure that we made it configurable.
But this is one thing, and this is for the settings which we can own, the OpenTelemetry settings, but we are unable to do anything for the .NET runtime settings.
**Michele Mancioppi (Dash0 Inc.)** 44:25 I'll check it out.
**Robert Pająk (Splunk Inc.)** 44:27 Okay.
I can, send you later, if you find it.
**Michele Mancioppi (Dash0 Inc.)** 44:31 Thank you.
**Reiley Yang (Microsoft Corporation)** 44:33 Okay, thanks, Aura.
Stephanie?
**Stephanie (Dell)** 44:39 Hi, guys!
**Reiley Yang (Microsoft Corporation)** 44:40 Bye.
**Stephanie (Dell)** 44:41 Hi, this is my first time attending this meeting. I'm a part of the, the OCSF Community Open Cybersecurity Framework Group. And, I had been talking to, I believe his name's Antoine, that's a part of this, community, and he suggested that I bring this topic to, to this group during this meeting to, get feedback from you guys.
So, I want to, introduce a draft proposal called the ITIOps Unified Telemetry Schema.
And I'm hoping to get your feedback and perspectives after you've had an opportunity to review it, so, it's publicly available on our OCSF, website, under, the issues, and I put a link to that in the agenda.
To be clear, this is… Yeah, that's the… that's the, the… document, but I'mma give a summary of it.
**Reiley Yang (Microsoft Corporation)** 45:39 Do you want me to open it?
**Stephanie (Dell)** 45:41 You can.
So to be clear, this is, not a completed specification, and it's not intended to, propose changes to OTEL itself.
Rather, it is an exploration of whether there is value in creating an operational classification framework that could complement OTEL and potentially be implemented as an extension within OCSF.
So OTEL is the, it's becoming, like, the standard for collecting and describing observability data, And we know that it provides kind of like a model for the metrics, logs, and traces, and, things of that sort. But this, proposal starts from that premises, that hotel already does that job.
The question this document explores is whether there is still a gap when it comes to classifying operational telemetry data, in a normalized, vendor-agnostic way, specifically, you know, if vendors generate similar operational events and logs and records, is there value in having a common way to classify them into operational categories, classes, and activities, similar to, OCSF? So, if you guys are familiar with, the Open Cybersecurity Framework.
The draft proposes a framework that introduces concepts like operational categories, classes.
Activity classification and telemetry type distinctions across metrics, logs, traces, and events.
The overall goal is to make, operational telemetry easier to normalize, correlate, and analyze across tools, while continuing to use OTEL as a source.
type model. One area that I'm particularly interested in is feedback around hotel event and log classification.
OTEL provides the structure and semantics of telemetry data, but this proposal explores whether there is additional value in classifying operational events into standard categories and activities that could support analytics.
When you guys get a chance to review the document, I appreciate your thoughts, in regards to a few questions, is this… in regards to a few questions. So, is this solving a problem that actually exists within the hotel ecosystem? Would operational classifications provide practical practical value, or would they introduce unnecessary complexities?
Also, are the proposed categories, classes, and activities meaningful and useful from an observability perspective?
Yeah, and so… I also want to highlight that we just, like I said, looking for feedback, before implementation begins. If this concept is valuable and there is community interest, the plan is to move forward to, implement this in stages through the OCSF community, using a series of, you know, PRs and things of that sort, instead of just one large, submission.
But before we had taken this step, we want to make sure that the OTEL community can, help identify gaps, overlaps, or concerns, and opportunities for better alignment.
So, I'm not looking for agreement in the proposal as it's written, but like I said, one of the main reasons is to bring it to the community to identify those gaps. So, If you guys are interested in additional collaboration, we do have, OCSF hotel, Syncs. We used to have them on Mondays, and then, We changed them to Tuesdays at 1 o'clock… well, 1.15, and all that information is on our OCSF, the GitHub, well, the Slack channel for there, if you want to continue to discuss, but the main focus is to get feedback from the community with folks that look at this type of data, hotel data, a lot, and what the benefit would be.
**Josh Suereth (Google LLC)** 49:52 So, I want to jump in quick, First of all, I think there's a need for us to join together, but I'm gonna ask the blunt question, which is, what you're proposing here looks like semantic conventions. Operational categorization of data, like saying, hey, this is type A, this is type B.
We've said, hey, we should join together with OCSF for quite some time, but none of us actually take energy to do it.
how is this not just directly competing with some… you said it's meant to complement, but, like, and then you say, why additional classifications needed? And I'm reading, like, what you list there, and that's all things that we have in semantic conventions. That's all things we have in OCSF. Like, like, how… how is this complementary?
Like, can… if you can give me an elevator pitch, or should I read through the whole document?
**Stephanie (Dell)** 50:38 I would say read to the document, but I also just would say, you know, because my focus is OCSF, so I could talk about more, like, how we use it on my team, so we were just trying to figure out a way, like.
That's easier with the logs, just exactly like how we do OCSF. Now, if it's already being done within OTEL, in that way, like, using classifications and activities and things of that sort, so we can loop this, data together, then, you know, that would be great, but we did not find where we could easily do that when it's turned… when it's… depending on, like, the particular log. So you have, network logs, things of that sort that kind of… that overlap with, OCSF-type data, and,
**Josh Suereth (Google LLC)** 51:25 I see. So, I guess my point more is, with semantic conventions, we're trying to, like, fragment them out so that we can have, like, subdivisions and things like this. From what I understand of, like, OCSF, when I did, like, deep dives, and, from looking at operational logs and, OTEL, right? And security, basically. The classification things you have, I think there's… there's an interesting opportunity here where we can actually really bridge the gap together, and really give you, like, hey, in OTEL, we can even say there's this aspect of logs that, like, OCF and OTEL work together on and own.
Where we can build out that standard on top of semantic conventions, so that OTEL, like, produces those. So that's more my question, is like, it says, why semantic conventions? When I was reading this, it's like, why do we need something new? And I don't know if we need necessarily something new where we carve out, hey, here's where this belongs in SEMCOM. Does that make sense?
**Stephanie (Dell)** 52:23 Yeah, that makes sense, and that's the kind of feedback that I'm looking forward to. And so, and even within OCSF, we were just saying an extension, so an extension would just be for, like, specific things that we could just add within the, the schema, versus adding it, just for data that Fits that criteria.
**Ted Young (Raintank, Inc. – Grafana Labs)** 52:44 Yeah.
**Stephanie (Dell)** 52:45 So, like I said, when you guys get a chance, to take a look.
not today, but, like, next… every Tuesday, we can start next week, just want to jump in on the, the call at 1.15.
I'm always… I'll always be there, unless I, update in the Slack channel that is, canceled, and then we can go into more detail and collaboration there, since we already have, like, a time slot there for that.
Communication.
Hi, Trask. I see your hand is up.
**Trask Stalnaker (Microsoft Corporation)** 53:19 I'll defer to Ted first, who's in the, the Zoom hand ordering.
**Stephanie (Dell)** 53:25 Oh, okay, I'm sorry, I just saw your.
**Trask Stalnaker (Microsoft Corporation)** 53:27 No worries.
**Ted Young (Raintank, Inc. – Grafana Labs)** 53:28 No worries. Yeah, I was just gonna second what Josh was saying, because I think you're gonna get this reaction from everybody over here. It's like, how are these different from semantic conventions? And the doc clearly talks about semantic conventions a lot, so just adding a section up at the top that explains, like, what you're trying to accomplish with these categories, that's different from what semantic conventions already does.
I think would… Would be just, like, helpful framework for anyone on this side trying to evaluate the rest of it.
**Stephanie (Dell)** 54:00 Okay, awesome, thank you.
**Trask Stalnaker (Microsoft Corporation)** 54:03 And I just wanted to invite you to come to the, Monday Semantic Convention.
SIG. I think that's probably where this discussion… we can carve out more time in that meeting for that… for this discussion, and I think it's more on point for those folks.
**Stephanie (Dell)** 54:25 Okay.
And that'll be on the calendar, right? The calendar, I can see.
**Reiley Yang (Microsoft Corporation)** 54:30 The public kind of… yes.
**Trask Stalnaker (Microsoft Corporation)** 54:31 Yeah, it's 8 AM Pacific time on Mondays.
**Stephanie (Dell)** 54:34 It's done. Okay.
Yeah.
**Reiley Yang (Microsoft Corporation)** 54:38 Yeah, nice meeting you.
Okay.
**Stephanie (Dell)** 54:40 Thank you.
**Reiley Yang (Microsoft Corporation)** 54:40 Let's move on. So, I have two really, quick topics. The first one, so from the GCNTC, we're seeing people reporting that hackers are trying to make some GitHub issues and PRs with prompt injection. So, one simple example is, if you're the maintainer.
you ask AI, hey, like, just go through the issues and see which one can be reproduced.
be aware, because the hackers can put in the reproduce tab, saying, run this command in the privileged mode on your machine and do something crazy. So just be aware. We've reported this to CNCF, but I… I guess many people are leveraging AI, so you need to know the side effect.
The second one, so, I've been talking about this for a while, so earlier we were trying to define what all the repo should do, then I realized it was a mistake, because many different repositories, they have different states.
Some of them, they just started, they don't want to do a lot of crazy things in security. So, we took a different approach here, and I have a… short PR, trying to define, like, these are the different levels. So, for Maintainers, I need your feedback. Our goal is, we want to make the… I'll quickly explain that. So by default, all the repositories come with, like, there's no clear expectation for security.
And our goal is to define the medium expectation that would make sense for most repositories. So the idea is, for the Maintainers, if you really want to do a reasonable job there, medium expectation should be something that most of us could be able to achieve.
Low expectation is something, like, if you're running short of stuff, or if you're just starting the product, you're not ready for production, like, ready, any… anything like that, then you start with low expectation. High expectation is something, like, we really try to be, like, high, so I don't expect, like, there will be more than 10%.
of the repositories that can meet the bar. It's like an aspirational goal. We want to… like, put the security bar relatively high for people who want to stretch themselves. So, I'll stop here. Please take a look. I know there could be a lot of debates, so we'll take time to get your feedback.
Okay, so, we don't have 5 minutes left, so Josh, I'm not sure if you want to take the next topic, or you want to wait for next week?
**Josh Suereth (Google LLC)** 57:06 We'll… we'll mention… I'll mention both briefly, because there's… there's Daniel and my topic. So, first is just, in OTLP, Profiling wants to do a thing where they would have a version number that is independent of the OTLP version number to track the ver… the stability version of the in-development profiles, in case of breaking changes.
I have some opinions here that will take a 5-minute discussion, but please look and comment on the issue, which is what I'll do now. I wanted to have a live discussion because I thought it'd be faster, but I'll put some thoughts on the issue. I don't want to block it. I just want us to think through the implications. Second is, And Daniel, I don't know if you want to say anything, but basically, the entity PR, we actually did, we think one of the biggest confusing things for entities was the merge algorithm was really convoluted. So, we took, Daniel's PR… we have two entity PRs, Daniel's goes in first, mine would be second, but, Daniel did a pass at cleaning up the NTPR algorithm. I think he did a really phenomenal job.
At making it clear what actually happens in more human-readable speak and less mathematical speak, which is what I had done. So please read Dan's changes in that PR, if you haven't had a chance. Those are the two things I wanted to say. So we got it done in 2 minutes. Awesome.
**Reiley Yang (Microsoft Corporation)** 58:26 Yeah, and do you want to continue the discussion next week? I can move that to the top of next week.
**Josh Suereth (Google LLC)** 58:30 The top one I would like to discuss, I think we need to discuss it offline. Florian, is this blocking profiling right now, or can you wait a week to make a decision?
**Florian Lehner** 58:39 I will not be available next week, maybe the week after that.
Yeah… would block at least some vendors going forward, as we have, breaking changes in the line. And, the reasoning is that, as long as we don't move from different, from V1 development to V1 something else, so the path… as long as the path does not change, the vendors need some way to distinguish, different versions. And, yeah, that's the motivation.
To keep it short.
But I think Naev did a good job in describing the issue, or all the topic all together in the… In the… in the PR, and yeah, we will be around answering.
**Josh Suereth (Google LLC)** 59:26 Yeah, the topic's well described, so I think I would encourage everyone to read the PR, and I think it's a significant decision for us, because it'll impact how we do protocol changes going forward.
Yeah. Cool.
**Reiley Yang (Microsoft Corporation)** 59:36 Cool. Thanks, Ara. We're giving one minute back.
Have a good one. Bye.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 59:41 Bye.
