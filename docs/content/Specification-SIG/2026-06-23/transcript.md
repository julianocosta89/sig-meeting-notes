SIG: Specification SIG
Date: 2026-06-23
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

jmacdonald 00:05:54 Hi, everybody.
I'm going out… wait a couple minutes. There's nothing on the agenda right now, and I'm trying to figure out if we have anything urgent to discuss.
Also, if you have a topic that you're keen on discussing, maybe now is a great time to put it in the agenda.
Great. A few issues are filling in, glad to see that.
First up, I'm gonna suggest we begin right now.
Looks like Josh Surreth is on the line, and would like… To talk with us about… the telemetry policy OTEP, which is the only OTEP that has fallen off the first page of pull requests, so we should give it some attention.
Josh, would you like to speak?
Josh Suereth 00:07:49 Yeah, so, the SOTEP's been open for a while, we've talked about it a lot. I think Jacob gave a demo previously. What I'm looking for is, I would like to collect any feedback that would be, like, a hard no to it. It has 3 green checkmarks, and it has a bunch of approvals on it from folks who are, like, excited and vamped to, like, you know, start this space. But I heard that there were some concerns, and from… from my point of view when I read through it.
I wasn't aware of open comments that needed to be resolved in the OTEP, but would be resolved as we progress through, like, implementing various things. For example, one of the latest open comments was like, hey, I have concerns about the exact you know, definition of a particular policy, and great, I'm glad you have concerns, that's something we want to resolve as we, like, go into, like, a design phase. What I'm looking for is, for the OTEP, this is supposed to be the general, like, principle, the general direction.
you know, can we… can we get to a point where we can kind of get to the next phase of execution? There's a bunch of us looking to… Kind of ramp up and go on this.
jmacdonald 00:09:01 Yeah, well, I'll take an opportunity to say that I gave it a green checkmark, though I am on the side of thinking this is specified enough to move forward.
Would anyone like to comment?
Josh Suereth 00:09:21 I actually don't… Josh, I don't see you on the green checkmark list.
jmacdonald 00:09:25 Oh, really?
Josh Suereth 00:09:26 Maybe there's a… yeah.
jmacdonald 00:09:28 That's exciting, I thought I've checkmarked that one.
Josh Suereth 00:09:31 Okay.
jmacdonald 00:09:33 Huh.
Josh Suereth 00:09:33 That's kind of the feedback I need to know, is like, I was just assuming people either didn't read it or weren't approving it, you know, like, didn't agree with it.
jmacdonald 00:09:41 Okay.
Somehow I thought I had. You know, Josh, I wanted to put a link in here. There's something that's exciting to me, it's from the OTel Arrow repository. It's not overlapping, except in some sort of, semantic intentions, I think. This is a link to a design document.
That was written from a OTel Aero contributor on the F5 side.
Actually, a fairly famous name in programming language design who has Pitched in some work on a… telemetry processing language specification. It does not interfere with your OTEP at all, but I wanted to throw it out there because, in the direction of specifying policies, I see us moving in the direction of higher-level languages. That's all I wanted to say.
Josh Suereth 00:10:35 Yeah, I've read through that proposal, prior to it being a PR and when it was a PR, and I gotta say, like, there's a lot of really good things in there. I think it's worth folks looking at. It really entertains a lot of the complex issues we've run into.
So I would highly recommend people read that as well.
Yeah. The link is in the notes.
jmacdonald 00:10:55 Yeah, so thank you. Josh, I'm gonna give you a green checkmark later. Anybody else want to speak on this topic?
carlosalberto 00:11:01 I would like to get at least one day to review this. There were some minor concerns from my side on the SDK versus collector approach, so just, if you could give me one day, like, today, it could be great.
Josh Suereth 00:11:16 Cool. I mean, if we… if we get the four check marks and we wait a week, are we okay to merge, I guess is the question, and then continue?
jmacdonald 00:11:25 Does anybody have reservations that would prevent us from doing that?
I think the answer is no. Okay, everybody, you have a day, let's get some more green checkmarks.
For the record, there are at least 6 more OCHAPs open. I looked at them all yesterday. If you haven't looked at them all, please do.
Let's move forward in the agenda, then. Next up we have, Pranav, about an… Issue, which might be… Very old, oh yeah.
Oh, yeah. So we have an issue from 2020 about adding a prefix to metric names. Oh my goodness, I've commented already.
Pranav, are you here? Would you like to speak?
Pranav Sharma 00:12:14 Yes. So, yeah, we recently came across a use case where I think if we had this issue implemented in the spec, like, it would have been easy for us to satisfy the use case. I also went through the previous conversations on the spec, and I think the biggest blocker for why this was not moved why did we not move forward with it 5 years ago, was metrics was in GA. I think that is no longer the case, and so I was wondering, you know, if we could just, See if there were any other objections with it.
I actually came across, with a few certain use cases.
Like, one of them was, you know, it would allow us dynamic namespacing of third-party and shared libraries, and then there was some domain-scoped ingestion and platform alignment.
And then, this would also help with some legacy time series databases, for namespacing with legacy time series databases, which do not actually support any metric labels.
So, I was just want… I just wanted to know if there were any other objections to… to this 5 years ago, other than metrics not being GA.
jmacdonald 00:13:27 That's a good question. I do not have enough memory of exactly what we were doing 5 years ago, 6 years ago, on this topic, to comment right now.
Does anybody else?
So, my understanding is you're asking for a configuration on the metric, let's say it's on the metric SDK at the provider level, or the meter provider, I suppose. So, once you have a meter, would you try to inject a prefix on all the metric names? Is that the idea?
Pranav Sharma 00:14:03 I was thinking more along the lines of adding a metric view, like, you know, you would select instruments, and then you would just add a prefix through the view. I can actually summarize what my proposal is and the use cases in a comment here, but, someone commented here that, you know, maybe I should present this in the spec meeting.
jmacdonald 00:14:22 Yeah.
Pranav Sharma 00:14:24 Yeah.
jmacdonald 00:14:25 Jack's got his hand up, maybe Jack has a comment.
Jack Berg 00:14:29 Just on the views, I say this… somewhat frequently, it feels like, but views are a pretty rough mechanism from a UX standpoint.
The reason being is that when you have multiple views that match an instrument, the configurations don't merge, they produce independent metric streams, and so if you wanted to have a view that said something like, hey, match all metrics, and then append this prefix to their metric name.
You know, that seems like good on paper, but as soon as you wanted to have another view in there, like, hey, match all histogram instruments and adjust their bucket boundaries.
or match one histogram instrument and adjust its bucket boundaries, then those two views, like, coalesce to produce two histogram metrics, one with the prefix and one with the adjusted bucket boundaries.
when what you probably want is one histogram with adjusted bucket boundaries and your desired prefix. So, views are a rough mechanism for this. The… I really, you know.
I guess, easy way to do this that is not, like, built into the SDK itself is to have a delegating metric exporter, a metric exporter that maybe wraps the OTLP exporter, and before calling the OTLP exporter, rewrites all the metric names to include your desired prefix.
you know, there's no built-in exporter to do that, so that's possible to do if you have, like, an extension or, you know, whatever you're doing, wrapping the SDK in some way.
Pranav Sharma 00:16:04 I did think about that, but one issue that I came across, that is, like, if you are exporting to multiple, destinations, then maybe you'd have to do this for all the different exporters, like, you'd have to keep repeating yourself.
So it's trying to avoid that.
I'll think about it a little bit more, though.
Jack Berg 00:16:26 Yeah, like, if you're just trying to just solve, like, a discrete problem for your use case, like, if you're actually, you know, using OpenTelemetry internally or something like that, I think a delegating exporter is a nice solution for this. If you think that this is a problem that, you know, lots of people will see across OpenTelemetry, then it might be more useful to try to adjust this specification.
But obviously adjusting the spec is more work, so…
Pranav Sharma 00:16:57 Okay, I did have some general use cases. I think I'll summarize my findings in a comment there, and we can go from there, but I do think this might be useful to other people as well.
jmacdonald 00:17:13 I mean, let me throw out some other thoughts. You could also wrap the meter provider and prefix the metric name on the way in before you register the metric name, for example. So I'm curious what… why we would prefer the export side than on the input side, potentially.
And also, Jack, this makes me wonder, should we fix views? Is there a way to fix views?
I also am skeptical of views.
Jack Berg 00:17:37 I think there's a way to fix views. I think David's got a decent proposal, and we've talked about this. It's just a matter of feeling the pain enough for us to do something about.
David Ashpole 00:17:46 I, Yeah, I'm happy to, maybe I'll put it at the end of the agenda if we want to talk about that, since today seems light. And if we get to it, then we can chat about it.
jmacdonald 00:18:01 Great. That's also… also good to hear. Thank you, David.
Okay, I'm seeing thumbs up, people agreeing, okay, cool. I think we should move on, then, to the next topic on the agenda. This is either Trask or Lyudmila would like to speak to us, I think, about… Gen AI semantic conventions.
per language, as well as a related OTEP.
Are either of… Great. I try.
Trask Stalnaker 00:18:28 If you can open up that link… So this is primarily for… this is the maintainer meeting side of this meeting. As maintain… as folks have, seen… we've split out the GenAI semantic conventions into a separate repo. We deprecated them in the core, reap semantic convention repo.
And we made a release of the core repo recently, and that's where I think maintainers, became aware, if they weren't already, of this problem, that, when you're codegenning your constants artifact.
Now, all these Gen AI, constants are… Marked as deprecated, and that's confusing. And so, we've… tried to document here what the path forward is, what we see the path forward as, but I think it's still possibly, confusing, understandably confusing to folks, so I just wanted to give a chance for if anyone had questions they wanted to raise here.
Tyler… I don't know if you had a chance to see my response… I don't know if there's something also maybe a little bit different in Go, but anyway… Yeah, just wanted to.
Open in case any maintainers here had kind of questions that we could help talk through for everyone.
Tyler 00:20:13 Yeah, thanks for the response, I saw the response, I just… yeah, I just want to share, like, this is very breaking for the Go ecosystem. This is something that is gonna have to, like.
This is gonna require a lot of work on our part to, like, restructure how we're actually releasing semantic conventions. And from a user standpoint, it's going to be very disruptive.
vary. It's going to be disruptive.
Trask Stalnaker 00:20:41 She's…
Tyler 00:20:41 Boom.
Trask Stalnaker 00:20:42 Could you just brief us on, for folks who aren't familiar with the Go ecosystem, how that's… what's different there than other languages where it's… we haven't seen this problem?
Tyler 00:20:55 Sure, so, like, in Go, first thing to understand is that, like, package names are uniquely identifying, and so, like, the location that code is generated is reflective in that package name.
So that means that, like, changing the location of code and how that gets imported is not, a Ford-compatible change. Somebody has to go into the codebase to actually upgrade to code by changing a package name.
In the sense that, like, it's not breaking, the old one will still work, but it's still, like, you can't do that upgrade with just, managing the… essentially, like, your versioning file.
That means that, to maintain that backwards compatibility and do that upgrade, we'd have to put this exact package into that, or sorry, this exact generation for the gRPC stuff, I'm sorry, the Gen AI stuff into the exact same location.
But that is not really viable, given it's not gonna have the same schema URL, which is a whole host of other issues.
And, like, it doesn't have the same structural, like, representation anymore. Like, the package name would likely change here, just from that fact. In fact, it'd probably want to change it, because it is going to be a breaking schema URL change.
Trask Stalnaker 00:22:10 So that… that's if people upgrade to the new GenAI artifact. If you generate a new GenAI artifact with the new stuff.
Why, like, in other languages, we were ex… we were… from SemConf, we were expecting that people would continue generating the deprecated stuff. Like, when we deprecate something in semantic conventions.
We were expecting that languages would continue… would generate those and just mark them as deprecated. That way, they wouldn't be breaking.
Tyler 00:22:48 Yeah, we don't.
Trask Stalnaker 00:22:48 We're not removing, we're not removing them.
Tyler 00:22:52 We… we don't generate that deprecated semantic conventions. The reason a long… Those lines is because a lot of those deprecations have naming conflicts, with existing semantic conventions, so we've grown into this situation many times where deprecations will actually, like, do a name change, but it generates to be the exact same name, and then we have conflicts, in our generation process.
Liudmila Molkova 00:23:18 We fixed it. It's no longer the case. We have means to validate that we don't produce conflicting names, and we don't.
Trask Stalnaker 00:23:30 There's policies in place now to prevent that.
Tyler 00:23:32 I'm just telling you why we don't do that, though. And that's… that's the reason why. And so, yeah, that… that no longer gets generated.
Trask Stalnaker 00:23:41 Could you… could you go back to generating that in the next version so that it wouldn't then be breaking for users?
Tyler 00:23:53 I mean, we could look into it. Another thing, though, is that, like, the versioning schema in Go is that each specific version is a different package, So that's also how we got around it, is just that, like, they're isolated in that sense.
We could go back to generating the… we could look at generating depicated, values.
It's a little awkward deprecating something without, like, some sort of replacement strategy, I guess?
Is the idea that users aren't supposed to use these GenAI semantic conventions?
Trask Stalnaker 00:24:27 With the next… with the… we haven't really… it is an awkward situation right now, because we haven't released from the new repository yet, so there isn't something they can use that's not deprecated.
But once we do release from the new repo, which, you know, sometime in the next month or so.
Then they would have that path forward.
Tyler 00:24:58 Yeah, I mean, I think from our user standpoint, like, having an artifact in the 142 package, or 144, I don't remember what we're up to.
That just… is it the same as, like, the 141? That just says deprecated, doesn't provide a lot of value to them.
So I don't break.
Trask Stalnaker 00:25:17 Which has value.
Liudmila Molkova 00:25:20 Well, it's not breaking either way, because users who use version 141 will… don't have to ever change the version to 142 for GenAI stuff, because… Like, doing nothing, like, not generating is also not breaking. It's just users cannot change the version, like a wildcard version, for all semantic conventions to 142. They will need to keep the version for 141.
Tyler 00:25:49 Right, correct, yeah.
Yeah, I'm a little bit more inclined to do that, just because there's a lot of linting errors that are going to come in if we start deprecating these things, but… Yeah, exactly like Lubella said, like, just leaving it is also a not-breaking option in the sense that, like, they won't see the other stuff. It's just more about, like, what is… what does the future hold?
And I think that that's kind of, like, the… the problem here, right? Is, like, what, like… Where we're at today, we are planning to release a 142 semantic convention package, we just merged it.
Last week, or something like that. Without the Gen AI stuff.
how we want to restructure that, that's a conversation, but it's more of on the question of, like, what happens for the next iteration, for the next… like, when Gen AI is available, it is released, like, how does that get integrated into, like, where users can access it?
And that's what I was talking about, where this is gonna be a very, like, it's gonna be a different structure, to the point where, like, it's going to be, I think, confusing enough. There's, I think, still an open question around how, like, schema URLs, like, federation works.
I'm also still not 100% sure, like, how diamond dependency issues there are related, or are, resolved, but, like.
I, like… that, I think, is something that is more… Yeah.
Go ahead, Josh.
Josh Suereth 00:27:15 Yeah, great questions. I mean, we're working on them, so if you want, like, you can join the tooling sig to talk about it, or, like, I'm working on the dependency management resolution algorithm, so if you're curious about diamond dependencies, they've… they're a nightmare, and we just don't allow them right now.
To some extent. But the other thing is, we have this… We have a resolution algorithm that can handle, things similar to what you'd expect from a package management thing. So, the idea would be, when you have a diamond dependency in a package manager, right, it picks a latest version in some fashion. There's a conflict resolution algorithm. Semantic Conventions basically has that, and then encodes what it chose in every schema URL.
So, schema URL has a linearization.
of all of the dependencies that are used to validate. But it also includes all the definitions it needs locally.
So, like, the thing that I want to emphasize here for Go is, when you think about a new schema URL, the way you're packaging things, you have a package name.
that represents a schema URL, which is the general SEMCOM one with the version.
You should do the same thing for all of these federated things. There should be a package with a version that represents that thing, and you'll be generally okay. Like, everything should work, everything should resolve appropriately if we've done our job well. That's the intention. So it should work the same way, like, a Go package works, in terms of resolution, dependencies, all that kind of junk.
We are doing a thing where we will kind of encode our dependencies kind of in a vendored way, if that makes sense? Like, it's almost like vending for the local version, so when you write instrumentation, you would use, like, the GenAI schema URL package, right?
You would use that as your schema URL when you instantiate your meter, your tracer, your logger.
And then you can just use that package for all constants, because we vendors everything into it.
It's kind of like the.
Tyler 00:29:12 Yeah, that's… that's my question. Like, that… that doesn't make any sense to me.
So, like, so I'm gonna go generate this Gen AI, like, package for Go. I think that's… I hear you. That's gonna be a little bit of a tough one.
Josh Suereth 00:29:26 You…
Tyler 00:29:27 But just, like, anyways…
Josh Suereth 00:29:28 Defender because of the way you're doing things, and will do resolution to tell you which specific versions to grab if there's a diamond dependency.
So, we might want to take this offline, and I can walk you through it, but when you go to generate code, you will get, here is the current schema that you're resolving, and here are the specific versions that you depend on, and we've already done resolution of diamond dependencies, where there is only one version of any dependency in the entire chain that you have to rely on.
Tyler 00:29:57 Yeah, I'm not getting it, though. So, like, I've got… I've got instrumentation, like, at the end of the day, like, my users, right? I have instrumentation that's writing something for GenAI, and that's, like, capturing it in a span, and that came in through some sort of, like, HTTP request, right? So it's gonna annotate both HTTP using the general, like, OpenTelemetry semantic conventions, as well as GenAI semantic conventions for particular spans, right? Like.
So, but the…
Josh Suereth 00:30:23 Two trainings.
Tyler 00:30:24 or something like that? Is that, like, the idea?
Josh Suereth 00:30:26 You'd have separate tracers, yeah.
Tyler 00:30:29 So I literally… I can't mix them on a span, is what you're saying.
Liudmila Molkova 00:30:33 You cannot mix them on the span, and if you mix, you will define a new span and a different schema URL that covers both.
Josh Suereth 00:30:41 That's basically been true for schema URL for all time. Like, you haven't been able to mix schemas on a spin.
Tyler 00:30:49 Well, sure, but we've never had this actual problem, because, like, there's only ever been, like, one… one grand schema URL. Like, yeah, other people can do schema URLs, but, like, there's really only one OTel schema URL.
Josh Suereth 00:31:01 there are people who have schema URLs, but you're right, it's a small set of people in the OTEL ecosystem, that's fair. And it's probably not apparent to the rest of OTEL that that's happening, because they aren't using semantic conventions in their schemas, the people who have them. But I hear what you're saying. It's, like, we have patterns and things in SEMCOM for how you would… make your own, like, if you need to merge things together. And we have this notion of attribute groups, which is how you add attributes to a span, but… but the reality is, if we're gonna have this, like, the way we think about things, we're not blending together an HTTP span and a GenAI span. You're actually gonna pick one, and you're either gonna have something that is a GenAI span, or you're gonna have something that is an HTTP span. You might actually have both.
this notion of merging, we really don't have that as a concept in no-tel or no-tel instrumentation. Maybe that's a thing we need to talk about and figure out how to do that.
But that's been something that's plagued hotel instrumentation since I've been around, which is, I have all these layers of instrumentation.
And when I turn them all on, I get a bajillion frickin' spans. Like, I'll get the Gen AI span, and the HD span, and the other thing. And we made these span suppression techniques that say, cool, if you see the Gen AI one, turn off the HTTP one, and that kind of crap.
Like, I think that's a problem we need to solve.
But that's kind of an… that's a bit of an independent problem, and it's one we currently have, right? Like, we are, and we've been on this path for a while of… there's a schema URL, there's a span definition, and your span is that particular schema URL.
You can layer in attribute groups to add on additional information that still pass compliance, but you're only one type of span at a time, you're not multiple types.
That's also true for metrics, that's also true for logs.
Tyler 00:32:48 I mean, I don't… Know if that's… true.
Like, I think that… That might just be a worldview.
Like, I don't think there's anything… in OTEL that specifically restricts you from doing that, and our users… even, I think, some of our… instrumentation in Go for some of our libraries mixes these attribute types across these things into a single span.
Josh Suereth 00:33:17 It is okay… It's just that there… Go ahead.
Liudmila Molkova 00:33:21 The resulting span is not defined anywhere, so you probably don't even attach schema URL to it.
Tyler 00:33:28 But, well, I mean, we do, though, right? Because, like, there is only one schema URL that encapsulates database, as well as HTTP, as well as… like, all of them are all under a single schema URL currently, so we do, like, there's a single Tracer for it, right?
Trask Stalnaker 00:33:46 The problem that I see, the, the kind of… I think worldview is a good, phrasing, that, the worldview from the semantic convention, side is that, semantic conventions apply to spans, metrics, log, to the signals.
As a whole, like, they don't apply to individual attributes.
So, and an individual attribute isn't… we're not really considering that a semantic convention.
I think, and Josh and Lamilla can correct me, maybe we don't have our worldview all in sync here. But that's where I think the difference I see is, is the span itself is a semantic convention. The individual attributes are are not… We've been trying to get…
Tyler 00:34:42 So I think at that point.
Trask Stalnaker 00:34:43 that.
Tyler 00:34:44 that's… that's maybe, like, where a lot of this problem and conflict's coming from in, like, the Go world. Not, like, I don't know, conflict's just a technical term here, but no, like, it's more around, like.
we've been there since the beginning, unfortunately, right? So, like, that is… it also means that, like, that idea of, like, having attributes, like.
not being, like, the atom of the semantic conventions was not always the case, right? Like, it used to literally be just attributes, right, that were defined there. And so, like, we've always exported it in that way, right? Like, our packaging right now is literally, like, a set of attributes that you can use, and they're well-defined for you, and then, like, how you want to compose a span.
It's up to you, right? And so I think that this is, like, I think where a lot of the, New World, order and vision is coming in. Like, we're looking at this as, like.
Maybe it's, like, an opportunity, or maybe it's, like, just a pain point, but, like, if we're going to have to go and restructure a lot of our packaging around this, because literally the package names are going to change, and, like, the structure on how they're going to change, our generation tools are going to change, like… It probably also behooves us to maybe look at, like, what we're generating, Which, yeah, I don't know, it's something that I've considered, but it's just like… I do, I do want to maybe bring it up, because, like, this, this may be something that is not resolved in a week. It may not be something that's resolved in a month or two. So… like, I, I do, If we're trying to push this through, like, it may be that Go's gonna start to lag, I guess, is the problem.
Trask Stalnaker 00:36:21 Totally agree, this is not something we're solving in a week. This is part of, the Josh's OTEP that I linked here in the, chat. We've just kind of been… I think we're… so committed on the semantic dimension side, we've felt this pain of this global registry for so long. We are so committed to… we have to federate. We have to support this world. We can't be a single bottleneck for every, you know, domain out there.
So we've been kind of pushing forward on that at the same time that all the, you know, the tooling is… is… mostly there, but still evolving in some places, like Josh was mentioning, the diamond dependency stuff.
Tyler 00:37:11 Yeah, that… that… I'm glad somebody else is thinking about that, because I don't want to think about it.
Trask Stalnaker 00:37:15 We do.
Tyler 00:37:16 Yeah, I, I guess maybe what I would ask is, As if we could keep you all in, like, the loop, or have some sort of feedback from you as we're, like, going through this new development stuff, because, like.
The last thing I really want to do is get to the end of this, and, we've got a solution, and maybe it kind of works, but it doesn't align on, like, that worldview, and, like.
We're broken in another year, or something like that, or we have major changes coming out in a year, or something like that.
Trask Stalnaker 00:37:47 Yeah, and I think, you know, we could definitely clearly do a better job of, you know, communicating. I think this is the right meeting to reach the maintainers who are Dealing with this issue.
And so don't hesitate to, you know, also to add that topic.
to this meeting, I think, for sure, you're not the only maintainer with questions.
Okay, but no.
Liudmila Molkova 00:38:15 Yeah, one last comment around this, Josh has an add-up for the federated semicond that is an excellent place to maybe discuss it. I posted the link in the chat, also added to the docs, to the notes. Yeah.
This one, And one thing, Josh brought up there is the platform release, right? So when a language or Probably a language decides to R… Bundle things relevant to this language together.
And… published as a whole, each of these individual packages could have its own schema URL, And we decide which one you want to use.
But I'm… My memory is vague, so Josh, correct me if I missed something.
Josh Suereth 00:39:14 No, that's… that's, that's correct, yeah.
So this, like, to your points, Tyler, this OTEP is supposed to kind of answer some of those questions, and to the extent that you could ask more questions in here that we could, like, answer would be ideal. Like, all of your questions around how the hell is this going to work for SDKs should be in here.
Tyler 00:39:35 Hmm. Okay. Yeah, I will… I will try to take a look at this, then.
Trask Stalnaker 00:39:42 Josh, there are a lot of open comments on this.
Hooked up.
Josh Suereth 00:39:48 Yes, a lot of them are from Mikyo from Open Inference, because we were talking to them about, like, what this could look like. So I can… I can resolve some of them and go through. I don't think I actually marked a lot of the things as resolved that are answered. I, like, leave them open so people can read them.
Before I just go clean them all up. But if you'd rather me, like, close things that I think are answered, I can absolutely do so.
Trask Stalnaker 00:40:14 Yeah, I mean, if there's a couple that you want to leave open, but right now it's kind of an intimidating PR to review because of the number of open Sure.
Josh Suereth 00:40:24 Okay, I will… I will mark things as resolved. I was leaving them… I… any question I thought was good, I left there for people to see the question, even if I think my answer resolved it.
But I can change my behavior there, that's fine.
Trask Stalnaker 00:40:38 I don't know, also don't know if other people… that… that's just my… my worldview.
Jack Berg 00:40:44 I, I typically leave potentially controversial comments open for a couple of days after I respond, but you can't leave them open indefinitely. At some point, you have to say, this is resolved, and count on reviewers to open, you know, resolved conversations if they want to see the whole history.
jmacdonald 00:41:03 Yeah, I agree, no more than 7 days.
Okay, we don't have time bounds on these topics, but we went over on that one, I'll say.
Trask Stalnaker 00:41:12 Thank you all, though, that was a great discussion.
jmacdonald 00:41:15 Thank you, Trask. Thank you, Lyudmila. Thank you, Josh. Thank you, everybody.
And please open the Federated Semantic Convention's PR, and maybe ignore some of the very long comments, and read it for yourself.
And now we have a topic from Ted to talk about the post-graduation roadmap. Please, Ted.
Ted Young 00:41:37 Yeah, I want to leave time for the system packages demo, but basically, just to sum up, you know, we've been discussing this roadmap for a while. Seems like comments have… have died down.
I'm interpreting that as, like, general agreement that this is, you know, the right roadmap. One question I had is just around approvals, right? This is… something the GC could approve and get merged, but something that was proposed in there was maybe, like, just going around and trying to get an approval from someone from each part of the roadmap.
Just to double check, that people are… are interested in this. The next step would be, Taking each item in this roadmap that's owned by a different group and fleshing that out as its own project.
In some way, either at a SIG level or a global level. So that's what I plan on moving on to next, with this… this work.
I think my main question, though, the one piece that we don't have, like, clear ownership for, or, like, a clear plan on, is instrumentation.
That's something I think we need to discuss more. Like, we know that we want to stabilize instrumentation and move it up To, the latest version of the semantic conventions across the board, but, we don't have, outside of, like, some pockets in OpenTelemetry, like, instrumentation's generally been considered, like, community stuff.
So, I'm curious what people think about, like, next steps at chewing through that. Most everything else on this roadmap has, like, clear ownership, and we can just sort of, like, get rolling with it by starting a project and getting it into people's backlogs. But that's the one thing where… I feel like we still need some discussion about what we want to be trying to do there.
So, I don't know, if people have thoughts, for the next, like, 5 to 10 minutes, like, what would be a good thread to pull on in terms of… moving instrumentation away from the Wild West and towards something that we're managing more directly.
Michele Mancioppi 00:44:09 I, think that there are… At least two tiers of instrumentations.
Those that are, table stakes.
And, they vary to some extent across different languages, but the major HTTP languages, major database drivers, gRPC implementations, and a few other things.
I have always seen them as table stakes, and then there is a very long tail of other instrumentations that Have, probably less adoption.
And I feel that… We should move some of the instrumentations that are table stakes.
to be, with the same kind of maintainers and maintenance as the SDKs themselves.
Because in this day and age.
An SDK without auto-instrumentation is only half the fun.
I feel that, historically, we made ourselves a disservice by lamping all instrumentations into the same category and following the same rules.
And maybe it would be less daunting for all of us.
To say that we do not need to support at the same level all instrumentations in each country package, but maybe we start supporting very well Based on some technologies and adoption metrics per language, a limited subset.
Ted Young 00:45:41 Yeah.
Thoughts, from maintainers on the call?
But one of the reasons why, you know, we haven't done it is, currently we, you know, we have, like, you say a long tail, let's call them community maintainers or contrib maintainers, and then we have, like.
for each language, a set of core maintainers who work on the SDK and APIs. In most languages, those maintainers have felt they don't have enough staffing in that SIG to also take on this work. Certainly, if we're talking about managing all of Contrib, like, that's not… Like you said, that's crazy, but… One option could be going SIG to SIG and seeing if there's any interest in taking on a subset of this. My feeling is that maintainers are going to say, well, we need more staffing if we're going to do that, but… I know we've got maintainers from Node.js, Go, and other languages here. I'm curious, what your thoughts are on how Contrib currently feels in your language.
Daniel Dyla (Dynatrace) 00:46:50 Yeah, I can…
Tyler 00:46:50 speak… Go…
Daniel Dyla (Dynatrace) 00:46:52 Go for it, Tyler.
Tyler 00:46:54 Sorry.
Yeah, I would just say that, like, what was just described is kind of the antithesis of, how we maintain instrumentation.
And it will be as we go forward.
we're in an open source community. Open source communities are driven by people that are actually doing things. So, yeah, sitting here telling people that they should do things.
is not how we're gonna get things done. And it won't be going forward. So, yeah, just a heads up, like, if you expect this from the Go community.
That's great. Join the community and start maintaining it.
Ted Young 00:47:27 Yep.
So, I think, like, to that end, it's, you know, and I want to completely understand, like, that there's not going to be any attempt to just declare everyone needs to deal with some unfunded mandate. This is more about just recognizing that, that, it feels like, we improve the semantic conventions, but we don't then move those out to maintaining instrumentation, even core, and it feels like we need to find some way to boot up that effort better. Not… that isn't just putting more work on the existing maintainers who didn't sign up for that.
And so, I think part of it is just figuring out, like, how would we go back to the community and be like, like, is there a way we can package this up?
That… would get… net us more contributors, basically. Like, rather than having, I don't know, like, having, like, a group of maintainers for a group of core stuff, sort of like Java instrumentation. Ludmila, I see you got your hand up.
Liudmila Molkova 00:48:33 I'm thinking we have examples of, country slash instrumentation that are managed well.
And, I would imagine that this work stream implies that We go across the community, and we try to ask maintainers what works today, what doesn't, and create some… Idea of how this is… could be run best.
And we'll leave it as a guidance for maintainers, and for the community who want to drive it. So, for example, I hope… I don't want to speak, on behalf of, Python maintainers, but I'm not sure if anybody's here. What they hear in Python SIG meetings is that People are… oh, Diego is here, so maybe, Diego, you will keep me honest. the meetings… in the meeting, in the financing meetings, people are discussing how to stabilize certain common parts, how to stabilize instrumentations.
How to manage this together, how to bundle things together. And if we have a prescription, some sort of a prescription, that would be helpful to derive the efforts maintainers are interested in and ready to support already.
And for SIGs like Genii, it would also be a good source of information on how to do things.
Right, like, the default.
jmacdonald 00:50:01 So…
Liudmila Molkova 00:50:01 Story.
Diego Hurtado Pimentel 00:50:04 Just to be clear, I'm not a maintainer, but…
Liudmila Molkova 00:50:08 You… he was. You were.
Diego Hurtado Pimentel 00:50:11 Are you sweet.
Ted Young 00:50:15 Daniel, I know you were, speaking up earlier, do you have thoughts, you know, from a Node.js perspective on, like, like, the state there and, you know.
you know, ways we could maybe, like, port something like Java instrumentation over to Node.js?
Daniel Dyla (Dynatrace) 00:50:32 I mean, something like Java instrumentation, unlikely, without… staffing up.
Yay.
I was gonna say, we have a couple of, and I think I mean literally a couple, there might just be two.
Possibly three. Instrumentations that we maintain in the core repository instead of the contrib repository that we take on the burden as maintainers.
It's like… HTTP, and, like, a couple of the ones that we know literally every single user probably needs these.
And, I mean, we find that people… People do step in to maintain the things that get used a lot.
And the things that don't get used as often don't get maintained as often. I mean, we get millions of downloads a week. Somebody is finding value in it and using it, and if it wasn't useful, then, we wouldn't see that. So I… I… I don't think the current situation is as broken as some people, Feel like it is.
Ted Young 00:51:39 Okay, maybe that.
Daniel Dyla (Dynatrace) 00:51:40 Yes, it could be improved, but…
Ted Young 00:51:43 Yeah, my feeling is if we wanted, you know, more active maintenance that we could keep track of, like, just saying, hey, waving our hands and being like, hey, could people become more contribib maintainers?
it's, like, hard to keep track of what's going on over there, but maybe part of it is finding a way to just keep track of contribib in different languages a little bit better, like, gain a better understanding of, like, like, how… like, what is our maintainership coverage in different languages of this… of Contrib, especially from the perspective of what we might consider, you know, table stakes instrumentation. Because like you're saying, it's probably, you know, lumpy and uneven. There's some places where everything's actually maintained just fine, other places where there are gaps. So maybe just understanding the landscape a bit more accurately is a good next step here.
Cool.
Okay.
That was helpful for me. I will keep trying to push on this.
And we've got 10 minutes left, so I'd like to turn it over to McKelly, for a demo of, packaging.
Michele Mancioppi 00:53:00 Alright, give me a second to move stuff around. If you have seen… already a demo of the OpenTelemetry injector and the system packaging that was part of that you see long ago, this may not have much news for you.
What you're seeing on screen is, I booted up a Ubuntu in a container. If I… if, in this day and age, if I want to start a virtual machine, the experience would be very much the same. I have added a locally built repository with a bunch of packages that I'm going to talk about.
Now I can run apt install OpenTelemetry.
This will result in a bunch of packages being installed. The OpenTelemetry is the main meta package, kind of the entry point.
One package for the injector, and one package each for .NET, Java, and Node.js.
These languages are selected because they're already supported in the injector.
And now, APT is gonna do a bunch of file installations.
And then I can start a JVM, and you will see that the OpenTelemptry Java agent starts doing its very business.
If this were a Tomcat application, Spring Boot, anything else that the OpenTender Java agent can instrument, it would just work as any other JVM.
the same kind of experience, here it was trying to report data to a collector that doesn't exist, so this is definitely proof the Java agent was set up and running correctly.
the same kind of experience, it's already there for .NET and JS. Other languages, like Python, are… have experimental support in the injector, and I'm waiting to add them to the system packages.
effectively to have, for Python, it's a matter of dependencies that, the built-in OTLP exporters have, which are toxic, their PCM protobuf, and Diego is actually working on that.
It would be possible to do something similar with Ruby, and Matt Ware is actually, writing a POC for that.
And other languages that could have the same treatment are PHP and Elixir.
So, languages where an SDK can be injected at startup in a language.
And then it works.
there are… A few things to work out. Some are, for example, where do we deploy the packages? What is the build chain? This is all things we're working out in the injector, in the packaging SIG.
But I think it's time for also the language Sikhs to start thinking about how they want their SDKs to be supported this way, and if they want. And this dovetails in the discussion about instrumentations, because injecting just an SDK without instrumentations does effectively no good.
There are a few things that a language should have to have a good support in system packages.
One is to support the declarative configuration.
So, what we, the current PC and the specifications that, you find in, in the PR and the packaging SIG, they are, installing, Language configurations in here.
And these are, are going to be declarative configurations which are going to be activated in the, in the SDKs.
Not all the languages have, support for declarative configuration.
And some that do, do not, for example, have support for, things like language-specific overrides.
There is a possibility with the model of the declarative configurations to specify configurations just for your language.
As overrides, and if we had those supported across the board.
They will provide a much better experience, where there is, by default, one configuration file that the user needs to edit, for example, to set resource attributes or additional environment variables, and then having per-language overrides is something the user could decide to do on their own.
Something that I… it's very important and dovetails in the discussion that we were having before about instrumentations is that The usefulness of this lives and dies by the quality and consistency of the instrumentations we inject.
having… that's why I was talking also about table-stake instrument… instrumentations, so something like this system package is going to be useful the moment we can inject high-quality, well-maintained, semantic convention-compliant instrumentations, resource detections.
And, have an agreement among SDKs about what is the default exporter.
So that there is ideally less work.
For the user to do via configuration.
Something that I do not consider as critical, but in my experimentations is very inconsistent and confusing for end users, is the support of out-of-the-box semantic convention metrics. For example, HTTP.
metrics that are collected by… inconsistently across languages and HTTP instrumentations.
And to be able to rely on those being collected.
Makes it easier for users, for example, to do tail sampling without losing much information from what the application would do.
the current scope that you find documented in this PR, So the package in Pool 10 has some caveats that we left out. For example, we want to bring in OBI, as a system package, and we'll work with the SIG, the OBS SIG to do that, because having GoBI also installable as part of APT, install open telemetry, would give us out-of-the-box support for most of the other languages you could run on a server.
So go RAST C++.
The collector packages are not part of the design yet.
I would love nothing better than to build automation in the system packages so that if there is a collector installed with a system package, then automatically the configurations of the SDKs we inject are going to talk to it right away. It would be a very nice experience.
I have a lot of open questions about how to integrate OpAMP in this.
I actually opened an issue earlier today with, with, some ideas.
And, eBPF Profiler is also something I would love to have eventually, something that would feel very interesting as an idea. I don't… I do not understand currently whether we're gonna have it as part of a system package Or it's a built in the collector, I do not know.
Last but not least, the specification that you find for the meta packages.
actually has built-ins, by design, support for vendor-out instrumentations. So, for example, the Zero Java package is something that it's easier for users by… but easier to add to the system, and, the user adds the vendor-specific, repository above the auto one, intending to preferentially use the vendor distress.
If you're interested, please go and have a look at the specification.
for the system package, metapackage architecture. The POC that I've shown you is live, In, at, this link.
And, yeah.
We're looking forward to posting back.
jmacdonald 01:01:34 Very good. Braden has a question.
Braydon Kains (Google) 01:01:38 I just wanted to make sure that, I'm understanding correctly that this is implemented with, like, a… like, a virtual package type of architecture, like a… like an app… in dev packages, there's like a provides virtual package? Yes.
Michele Mancioppi 01:01:51 Yes.
Braydon Kains (Google) 01:01:52 Because I think what you described is feasible if, like, OpenTelemetry Collector was a virtual package, then, like, if something is already providing that package, the rest of the installation could do something different in the pre-install?
Michele Mancioppi 01:02:04 It's, there is a little twist about interfaces.
So, for example, would be, probably OpenTerritory-collector1, but then, the, the OpenTerritory Collector package itself needs to declare that it satisfies the dependency.
Braydon Kains (Google) 01:02:19 Right, that's the.
Michele Mancioppi 01:02:20 I think most of… so the OpenTech collector packages, I work with them a lot, and they're very healthy. They need a little tweaking, and ideally being part of the same repository for it to just work, and then a few tweaks in the default configurations we will give out of the box.
I think we have an opportunity there with limited work to give a really good experience out of the box.
Braydon Kains (Google) 01:02:43 Yep, makes sense. I'm mostly following this because, like, we have our hotel collector, and, like, if we just needed to, like, satisfy a virtual package and have our config work a certain way, you know, we would happily do that to make it work, so I'm keeping an eye on it.
Michele Mancioppi 01:02:56 Yeah, I would love for somebody from the Collector SIG to actually interact on the… On the, on this… on this, issue.
I, yeah, I'm very passionate about this topic.
jmacdonald 01:03:12 All right, thank you all. You have made it to the end of another meeting. Appreciate the update on system packaging. That looks really good to me.
I think we have time for one last word, if anybody has one, but maybe not.
Alright, thank you all. See you next time.
