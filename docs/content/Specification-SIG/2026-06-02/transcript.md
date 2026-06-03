SIG: Specification SIG
Date: 2026-06-02
Duration: 113 minutes
============================================================

## Zoom Recording Transcript

**Reiley** 00:34 Hey, Tiger. Morning.
**Tigran Najaryan** 00:38 Oh, okay.
**Reiley** 01:49 Hey, everyone, thanks for joining.
Let's give another one or two minutes for folks to join.
I'm gonna share my screen, let me know if you can see it.
**Tigran Najaryan** 02:14 Yep.
**Reiley** 02:16 Okay, thanks.
We'll wait for one more minute.
Yeah, meanwhile, if you haven't put your name on the attendees, please do so.
Okay, hey everyone, thanks for joining. Let's get started.
So the first topic is just one-minute quick, FYI. We've made the update in the community repo about the maintainer responsibility for security advisories, and in return, we're giving maintainers additional support, like, when they need GitHub admin access on the repositories. So I put a couple links there. If you haven't seen this, please take a look.
That's all.
Let's move to the next topic, the stable by default.
Hi, are you here?
**Ted Young** 03:53 Yeah, I'm here. Sorry, I didn't see it was already on, the agenda, so I was just putting it down at the bottom. But, yeah, so we're not calling this stable by default anymore, because no one knew what that meant. The, general availability roadmap is… the language we're using right now. As I've mentioned before, if someone comes up with a better term that everyone likes, I'm happy to change the words on this.
I did make an update to this doc to clean up the language to hopefully clarify what GA means, and also, you know, removed any talk of, like, versioning other than to mention some components are 1.0 already, and we're not talking about the versions of specific components.
Except for the specific places where we're trying to push things, out of, experimental and into stable or 1.0, which is a specific section on the roadmap.
Based on some feedback, did expand the roadmap to include a couple of different things. One is performance and benchmarking.
In the past, trying to come up with universal benchmarks has been, like, a bike shed that maintainers haven't been super interested in, but it seems like There's a lot more prior art at this point, and some interest from some maintainers around defining what that might look like, so added that back onto the roadmap.
the other things we added, where did it go?
Self-observability, actually, like, open telemetry is surprisingly, you know, unobservable from the perspective of operators trying to deal with things like drop spans and the like.
And we should actually be… be kind of best in class, especially moving into a new phase where we want to be encouraging, a lot of, like, native instrumentation and things of that nature. It's actually a good time to be kind of, like, dogfooding.
some of our own stuff, so I thought there was a good case to be made that as part of saying OTEL is GA, it should have sufficient self-observability, to be, you know, manageable.
Helm, in addition to OpenTelemetry Operator, we have a number of Helm charts that should also go 1.0 in the process of the things that they control going 1.0, so that was added.
And then last but not least, long-term support.
And what that means. Actually, what we have written in this spec is pretty old and limited.
So, I don't want to have a huge amount of time spent on this, but certainly having a spec project where we look at just reviewing what we've written down about long-term support.
And… and doing another pass at that to reflect our current reality and our current intentions around that, seems worthwhile.
So I added all of that to the roadmap. We just have a look at it.
If people have any comments here, that's great, but it seems like we have a pretty full agenda.
**Tigran Najaryan** 07:18 But I know we talked about this, but I want to bring it up one more time. I think calling it general availability is, It's going to pose… A lot of confusion.
We have a ton of customers who use OpenTelemetry. We have a ton of OpenTelemetry components which are already at 1.0, some are even 2.0.
So, I think that's sending the wrong message.
To everyone involved. So let's really, really try to find whatever is another name for the project. I don't really care about the name, I care about the message it sends. I think it's a problem, if we call it that way.
So, let's really try to find something else here.
**Daniel Dyla (Dynatrace)** 08:01 Yeah, I think the term general availability kind of implies that it was limited availability before, which also makes no sense.
**Ted Young** 08:12 Yeah, I have a feeling there's no, like, perfect name here, but certainly switching to something that's maybe vaguer, and more for our purposes might be… might be better.
Does anyone…
**Tigran Najaryan** 08:28 We could do… we could do it completely differently. We could… we're doing this… this was… initially triggered by what we needed to do for the CNCF graduation, right?
could we call this graduation follow-ups, or anything like that? Completely avoid the topic of whether this is about stability, or GA-ing, or anything like that, right? We're… I think it's fair to say that essentially graduating is what triggered it, so let's name it that way. Would that work?
**Ted Young** 09:05 Graduation? Maturity? Yeah.
**Tigran Najaryan** 09:07 Yeah, yeah, maybe something but good, yeah.
**Ted Young** 09:09 like that, yeah.
I've liked using graduation as kind of, like, a motivating, frame for this, and so, I mean, I'm happy we graduated, but I was, like.
Mildly disappointed that, like.
you know, I didn't get to say, like, in order to graduate, we need to… to do these things. I didn't want to block it, but… I still think using that as a framing could be good.
**Tigran Najaryan** 09:33 Yeah, graduation, follow-ups, or whatever, right? Anything. Anything works, I just… I don't want to send the wrong message there. That's all.
**Ted Young** 09:42 Great.
Another thing, you know, as part of this roadmap is figuring out, What should our new approach be to roadmapping and project management?
Because it feels like we need to… to shake things up on that front. So that's actually part of this roadmap, is to figure that out in a way where there's more community involvement, right? The maintainers are more directly involved, we're having more discussions like this.
And it does almost feel like, with this roadmap, like, you wouldn't have to add too many other things to it.
To have it be sort of a complete roadmap for… For what we're up to.
I'm a little reluctant to go all the way there, because I don't want us to lose focus, but… As sort of, like, a prototype for what that process… might look like. This at least feels like a step… a strong step in the right direction, in that we're having these conversations here, in these meetings, and getting good discussion, On the pull request about what our roadmap should be.
So, in some sense.
you know, just food for thought. Think about this as, like, a prototype for, like, what a roadmapping process could look like in general that we're maybe doing.
Every quarter, or something like that, or once a year, to figure out a roadmap.
saw productization get proposed, but I feel like any term like that… I think I like graduation, because the problem with any other kind of generalized term is that it's, like, too open for people to come up with their own interpretation of what it means.
**Tigran Najaryan** 11:33 Right. Graduation is very specific, it's about the thing that has happened, and it's neutral in that sense, right? It's a fact, it's not an opinion.
**Ted Young** 11:43 Yeah, and it's sort of, like, implying, like, a time frame for right now, which is more what we're trying to talk about.
Okay.
Thanks. I will do that.
**Reiley** 11:59 Any other questions, comments?
Tad, do you want something to be added, or you're okay as moving to the next one?
**Ted Young** 12:09 Nope, let's go.
**Reiley** 12:12 Okay, then we saved 15 minutes. Jack?
**Jack Berg** 12:17 Yeah, so, Marillia opened an issue about this a couple of weeks ago, and I wanted to promote it more broadly here. This is following up some of the other deprecation work that we have been doing in recent months, in recent years, to do things like deprecate Jaeger exporter, deprecate the Zipkin exporter, and, you know, one of the things that we could consider doing, and I think open tracing as well, the open tracing shim was deprecated as well recently, so, should we consider doing the same thing for the Open Census compatibility document and the shim that it discusses?
You know, anecdotally, as a maintainer of OpenTelemetry Java, where we have one of these shims.
I don't have numbers about usage, but I don't have numbers about usage about any of our components, unfortunately, but I haven't heard any issues or PRs or discussions about OpenCensus in years.
So, you know, for what that's worth, I'm not sure, as just, like, a data point, I'm not sure how much it's being used actively right now. So, I would like to reduce the maintenance burden by getting rid of unused components.
**Reiley** 13:37 Okay, so I…
**Liudmila Molkova** 13:38 Sorry.
**Reiley** 13:39 Sorry to go ahead, Daniel.
**Liudmila Molkova** 13:41 So for Zipkin, I think we've done some analysis based on other languages where the download stats are public.
And maybe we can do the same here.
**Jack Berg** 13:53 Sounds good. Do you remember which languages had publicly available stats? Probably… probably MPM, right?
**Liudmila Molkova** 13:59 yeah, NPM, PyPi, NuGet.
**Jack Berg** 14:04 Yeah, so most languages.
**Trask Stalnaker** 14:10 Chuck, I think.
I finally fixed that, so we can get JavaS dots again.
**Jack Berg** 14:16 I was looking at that, Trask. I saw some positive signal that that would be the case, but I tried to actually do that last week, and I was not able to get statistics again, so maybe we should take another look at it together, Trask.
**Daniel Dyla (Dynatrace)** 14:31 the JavaScript Open Census shim… gets 31 weekly downloads, so I don't know if we can deprecate it.
**Jack Berg** 14:41 I hope that was some sarcasm.
**Daniel Dyla (Dynatrace)** 14:43 That one.
**Reiley** 14:48 Yeah, I have one question. So, depending on the language, there could be a case where one language is still eating it heavily, while the other language might not be eating it at all.
And do we want to have this consistency by forcing all the languages to be either, like, deprecating it, or just keep supporting that, or we can allow certain language to deprecate that by saying, we don't have users here?
**Jack Berg** 15:16 Yeah, like, the thing that I would want to achieve is I would want to achieve, sort of, like, explicit permission from the spec, to say, like, hey, it's okay to stop publishing this thing.
And, you know, as a spec maintainer, I would be interested in, like, you know, somehow marking the document to say, hey, this is here for archival purposes and historic purposes, but, like, we're not actively maintaining this document. We don't need to actively keep it up to date as the other parts of the spec that might reference it continue to evolve.
So, I don't want the maintenance burden in code, I don't want the maintenance burden in the spec.
But, you know, if, if, you know, that's not a problem, I don't see any way to force people, any reason to force maintainers to get rid of their components.
**Liudmila Molkova** 16:08 Yeah, and I think the download stats only help us understand they are not the… the blocker.
**Jack Berg** 16:23 All right, so, if you support, please indicate so on the issue. If you have… if you're a maintainer and you have access to some download statistics, please share those as well. And yeah, Lun Milla, I interrupted you, so I'm sorry if you had an additional comment.
**Liudmila Molkova** 16:41 No worries, the Python is also very little download that I'll post on the issue.
**Jack Berg** 16:47 Thank you.
Can we move on?
**Reiley** 17:10 Yeah, let's move on. Robert.
**Pellared** 17:16 Can you share your screen? I'll also be thankful if someone helps me talking, because I have a sore throat today. But yeah, I have two PRs which have been open for quite some time, and have probably enough amount of approvals, I think… oh, merged, sorry.
Maybe same for other one, then.
Sure.
Yeah, I think this one can be merged as well. This is mostly copy-paste and also have enough approvals.
**Reiley** 17:57 Yeah, looks like so. I've been told Click Merge mid-ride it, unless someone has concern.
**Carlos Alberto Cortez** 18:04 No, I think it's okay. It's just a recommendation here, and it's for non-LTLP protocols, which I think it's totally fine.
**Reiley** 18:15 Okay.
Thank you, Robar.
Thank you, Carl.
**Pellared** 18:19 Okay, let's go for words.
Yeah. So, next PRs, I created fully today, one I didn't even mention, it was early, verily speaking, and it has enough approvals, and I already can, I will merge it myself, because I'm already a maintainer of the protot. This is, this one is about mainly consistency. We had, proposed some limits, and when we were talking, and this just changes, made too short.
So that configurability is more like a recommendation than allowance, and we did it already for other limits, which were done after this PR, which we introduced May, was merged.
And we also discussed that it is better to have this configuration, also for sake of the configuration, declarative configuration, so it's also mostly about having the specification consistent.
So, mainly a clean-up stuff.
So, this didn't want these approvals.
Or… Or not.
or requesting changes. The next one is more complex, server response limit, yeah, this one.
This one, I did… I explicitly didn't want… I explicitly have not added in the initial PR, because this is mostly about server behavior. So, for instance, the OpenTelemy collector, and I did… I preferred having baby steps.
And this has the, this has the recommendation about response size limits for the server. And I'm mostly asking the collector folks to take a look here. And I think we should not rush, with this PR.
And, yeah, there was one thing which we have been discussing before, which I want to call out, that this, the response, which is… which the server, like, sends.
It's mostly, the biggest… Payload?
It's for partial success.
And currently, the spec says that only… I do not remember, there's one integer, which says how many data points or something like this, needs to be, have not been processed successfully. This is the only thing which the OTLP says that is required. There's also something called error message, which is optional.
So, I tried to say something like, if we hit the limit, we can just omit the error message.
because I think that it's better to omit this, diagnostic information.
Then, just getting rid of, getting, like, dropping the request, which is about, you know, sending the telemetry to the collector.
But if you have any other opinions, or… or, I don't know.
opinions, or maybe other approaches that you want to pursue, then yeah, I'm open to it, and I think the collector guys will for sure have the best opinion and feedback I've heard.
Any questions or feedback that you have?
**Tigran Najaryan** 21:44 Robert, I think the question I had was around how do you shorten their message to still ensure it's something meaningful.
If you mean that, I guess you mechanically truncate it.
then, I don't know if it's a great idea. Maybe omitting is a better thing to do there. And the other question I have is, how do you even decide what to emit to omit that Results in the desirable, desirable limits on the wire.
It's going to be a complex calculation if you want to actually hit the limit on the… because the limits are the wire size, right?
**Pellared** 22:26 Yes.
**Tigran Najaryan** 22:26 So, Implementation-wise, it's a bit unclear to me. How do you… how do you end up doing what the spec says you need to do there?
**Pellared** 22:36 If I remember correctly, I think even the specification around what's around error message is also not very specific.
Which it doesn't… I don't think it explicitly says what the error message needs to contain. Carlos, could you maybe just, add a preview for the file, for the whole file?
Maybe you can just quickly… Which one?
**Tigran Najaryan** 23:04 No, I get it.
**Pellared** 23:05 Israeli, Israeli.
**Tigran Najaryan** 23:07 The point is more about… you're asking implementations to do something that is… I don't know how to do. If I were to write this code.
Like, I have an arbitrary limit that I need to hit. How do I do that? There's a bunch of fields which I can decide to either truncate.
or omit, and how do I do that? To end up within the limit, but… try to not lose too much information. It's a bit vague. It's not very, very well defined. What do I do as an implementer there?
**Pellared** 23:41 I will try to refine it, I will double-check it. I think that collector guys can also, advise something. I think there's some notation of verbosity of the error message, how much details you want to emit with the error message, and I think that you should, if, for instance, the collector or something is contribute to some, I don't know, high verbosity, then probably just, you know, trying to, decrease the amount of verbosity in this message, and you know, just go lower and lower until the limit is fulfilled, but just my idea, and I think we can follow up on the PR. It doesn't work for you, Tigran?
And thanks for your feedback.
**Tigran Najaryan** 24:21 Yeah, yeah, if you can make it clear for implementations to know what exactly to do in that situation, that would be great. That's my only concern.
**Pellared** 24:31 Thank you.
**Reiley** 24:36 Robert, anything you want to mention here?
**Pellared** 24:40 Only the fact that I remember about this. What I want to do is post this once, not to do too much at once. Thank you.
**Reiley** 24:50 Okay.
Let's move to the next. Braden?
**Arthur (ca-wat-brt3)** 24:57 Yeah, so this should be relatively quick, I just want to announce to the broader group that I'm working on a project, to essentially properly specify and unify the behavior of batching in the collector and batching in the SDK.
This started because in the collector.
We've already dealt with a little bit of, like, thrashing around, where we wanted to move people off of the batch processor and onto the exporter helper sending queue batch, if you're familiar with that. And then we already, as I wanted to introduce a new, a new piece of functionality, a new way of treating the limits.
our config there was essentially broken, like, not going to allow it to work. And then at the same time, there was, discussions in the SDK side to introduce similar types of configs in the declarative configuration, and that was when I decided we should just merge forces, and that sort of ballooned into… it's not very well specified right now, and the collector is… the collector batching process is well thought out, but not written down front to back, necessarily. So essentially, we're trying to, catch that up. That's what I want to do with this project. I've got some people for, Go, Rust, and Python now. I need to write down the Python one that just happened. But the… I'm still looking for… people in other languages, or just people who are interested in batching in general, who want to be part of the initial discussions for the shape of it. So, if you are interested, you can send me a DM on the CNCF Slack, or you can comment your support on the issue.
**Tigran Najaryan** 26:48 One comment I have on this is this likely means Some sort of breaking changes to how the batching is configured today.
And, I think the batch processor is better in the collector, so I guess formally, you can make those breaking changes, but I don't know if that's… it's a great idea, so… because it's… it's going to be in use by many people now.
Anyway, I guess I would like to see what's the thinking here with regards to whether you're doing breaking changes, or you're doing additional settings that can override the others. What's… what's the plan there?
When you… when you have that design, it would be great to take a look at it, and, that… that would be the important piece of it. What do you plan to do?
And also for the SDKs as well.
Do we maintain backwards compatibility, design new settings, or we break stuff?
**Arthur (ca-wat-brt3)** 27:43 The… a good… a good reference for this would be the initial issue that I opened in the collector that sort of spawned all of this, which I linked in the project.
It was essentially to introduce a new a new functionality to the sending queue batch, which would consider two limits at once. So, you want to make sure your request is not larger than a certain byte limit, but also not larger than a certain item limit.
And that… I tried to come up with ways to… Introduced that into the config in non-breaking ways, and that led to discussions about various ways that it would look better if we just decided to break it, decided to break it and then stabilize a new, like, final version that we've agreed on. I don't know quite where I stand yet. I want to be delicate about making changes to those.
I think we can be delicate and make breaking changes at the same time.
like, through deprecation of old surface and new surface. Like, I feel like there might be a way to do that. I wanted to… I don't have a… personal opinion yet. I wanted to get more feedback from more people in the project, too.
I see Josh has his hand up.
**Tigran Najaryan** 28:58 Yep.
**jmacdonald** 29:00 Hi, thank you. Yeah, there's sort of two questions that are happening here at once, and I think Tigran's concern is super valid. The batching configuration changes that Braden is proposing sort of lined up with other requests happening in the SDK, and lined up with a multi-year effort in the collector to change how batching was configured.
By putting it in a new place.
meaning to… what we call the exporter helper, as opposed to the batch processor. I've been involved in this effort for similar… for different reasons, mainly trying to get error propagation options to work for a few years now, and that's essentially separate from what Braden's talking about. We have these features called wait for result, and we have a feature called block on overflow, and we're trying to figure out how to take out the batch processor deprecate it, remove it, and switch to the exporter helper at the same time. So, Tigran, there's already some breaking stuff happening that's, like, motivating this sort of convergence here, that we do this at the same time. We only break batching once if we have to break it. And meanwhile, we're planning to introduce a new processor that has all the new batch functionality as an option under a new name, new implementation, new behavior that has all these new options available as well for the corner cases where we need a processor. That's all underway, and I have a document on the retiring batch processor project.
**Tigran Najaryan** 30:22 Yeah, yeah, makes sense. When you know, when you have the opinion, when you have the plan, it would be great to take a look at it.
So you… I guess you're saying you're planning to keep the old processor around for a while?
And very…
**jmacdonald** 30:38 Yeah…
**Tigran Najaryan** 30:38 We'll see when we remove that at some point.
**jmacdonald** 30:40 So I'll post that this week, like, later today, even. I have a second draft of it, and yes, the answer… the proposal is to have 6 months of life left on the batch processor or so.
And to introduce the new behavior, and eventually to switch the defaults. So the defaults right now are sort of in a state where they were left after years of development and change. So now we're at a place where it's basically stable, and the exporter helper should have In our opinion, at least the recommendation is to set block on overflow by default, and to set batching by default, so that when we take away batch processor, like, users get blocking batching behavior by default.
But not this wait on overflow, which turns the collector… sorry, wait on result, which turns the collector into a synchronous proxy, effectively, which is not what we want.
**Tigran Najaryan** 31:25 Yeah.
Okay, thank you.
**Reiley** 31:29 Josh, do you already have a link, or you will share the link later?
**jmacdonald** 31:33 I have a link, and I will share it in the chat. It's under revision right now, so I'd prefer people read it later in the day.
**Reiley** 31:40 Okay.
Cool, thank you.
Anything else to add here?
**Arthur (ca-wat-brt3)** 31:47 No, I don't think so. Let me know if you… if you have any interest in it. I guess, actually, one question I thought of is that, should we… Were you okay to… merge the project proposal before, like, the initial design is finished. I am still refining a little bit, like, the exact goals, like, clarifying the goals in the project proposal.
But I was not going to start things like provisioning a Slack channel or organizing meetings until the project proposal was merged. I figured that was more the process. Does that… sound right?
**Tigran Najaryan** 32:21 Yeah, I think that's fine.
**Reiley** 32:22 Boom.
**Tigran Najaryan** 32:23 Yeah.
**Reiley** 32:23 Yeah.
**Tigran Najaryan** 32:24 as long.
**Reiley** 32:25 We have the lock.
**Tigran Najaryan** 32:25 Understanding that if the design Doesn't work, it doesn't get accepted, then you'll have to rethink the subsequent steps, maybe.
**Arthur (ca-wat-brt3)** 32:34 Yep.
I'll call that out specifically in the proposal, too.
**Reiley** 32:44 Okay.
**Arthur (ca-wat-brt3)** 32:45 That's everything then, thank you.
**Reiley** 32:47 Okay, let's move on. CJ.
**Cijo Thomas (Microsoft)** 32:52 This was discussed a few weeks ago, and unfortunately I was not able to join that time. And between the time I added this to agenda, and now it looks like it has already been approved by multiple Spec maintainer, so probably won't need much, discussion.
But I just wanted to use the time to explain what I'm trying to do here. Ted already mentioned, like, self-observability is part of the… post-GA, stable by default effort, so this is more like a companion or a subsection to that, specifically targeting the client's SDKs.
So the PR, which was linked here is just the first step, which is… Telling the… or modifying the specification to include a normative guidance, should All SDKs should emit self-absorbability.
And it's intentionally, like, one-liner, it just points to a self-observability dog.
Which, again, intentionally does not list anything other than pointing to the semantic conventions. So, this is just one step which is instructing all language maintainers to care about self-telemetry or self-observability. Bulk of the work, is actually going to be in the actual semantic conventions and languages.
I already realized that, like, Java and Go, implement this. Probably I can get, like, one more language to implement, and… Move the semantic convention itself to stable, and then come back.
to the specification and mark, this also a staple. So that's the overall idea, and I also put Probably I got removed. Oh, yeah, there is something I put which is more like an ambitious thing. So Ted already mentioned that, like, we as Open Elementary should be setting, good examples.
The whole world on how to instrument and how to monitor yourself.
And part of that is… To not only instrument ourselves and emit logs, metrics, and traces.
But also prove that we indeed, do that.
And Weaver is the official tool in OpenTelemetry. So my plan is to use Weaver in all reports, too.
enforce at CA time that, whatever.
internal metrics we are supposed to produce, we'll always produce it, and CA will get it, and we'll use Weaver to, prove that it's the case. A lot of things has to happen before this becomes reality, so I've already started, like, small improvements to Weaver, semantic conventions, in multiple languages as well. To make that happen, it'll probably be a relatively long effort, but first step is just, getting the spec to officially expect every languages to implement self-observability metrics.
Jack had some comments about lifetime concerns.
And since I didn't have a perfect answer, I kind of put a simple wording saying that metrics or logs, anything at early stages of application and the late stage, like, in the shutdown phase, they're, like, best effort, because the… the thing which can transport those telemetry may itself be shut down already. So, depending on that ordering issue, you… it's more like a best effort. So I put a simple sentence, just to, codify or explain to people that it's not perfect at these two phases.
Yeah, and all other things which were, having debates, I moved it out from the spec ripper, because, like, semantic invention is the right place to… document all those things. It should be, like, relatively small now.
That's pretty much it, and it looks like all the multiple languages are already supporting it, so we are in good shape to… At least mark some of the metrics in semantic conventions as stable.
Anyone else to discuss… Yeah, Jack, you are here already. Okay, go ahead.
**Jack Berg** 36:35 I saw you responded to my comment, and I'll re-review the PR and properly approve it today.
And, as a follow-up, after it's merged, somebody should open a tracking issue for stability around these things, because as you… as you mentioned, there's two in almost three languages, at least, that have implementations of this, so… We're in good shape, to… to proceed with this out of development.
I… when we were implementing this in Java, there was, like.
there's… there's a few sharp edges to look out for, and I was reading your PR, and I think it's good, because it just… it doesn't try to do too much. It just, like, establishes the linkage between the specification and semantic conventions. But there's some sharp edges to watch out for, and I'm wondering if we should provide some… some guidance to… to maintainers, maybe supplementary guidance, which is not normative or something like that.
Just to avoid the foot guns. Like, here's a foot gun. You know, when you're configuring, right now, the semantic conventions only have metrics.
What if someday the semantic inventions also add, like, like, logs slash events, or traces? It's already in progress?
**Cijo Thomas (Microsoft)** 37:53 I'm adding it in a draft PR already, so we will have events as well.
**Jack Berg** 37:57 Right, so if we… if that's, like, part of the scope, then, like, when you're exposing APIs for your tracer provider to have internal telemetry, then that API shouldn't be called, like, setMeterProvider. It should expose should accept all the providers, meter provider, logger provider, maybe tracer provider, anything that we expect telemetry. And as soon as you get, like, out of just, like, accepting a meter provider, then you get in, like, you get into a real, like, quagmire in terms of, like, ordering. Because, like, it's kind of simple when it's restricted just to metrics. You just, like, initialize your meter provider last. And so when you initialize your tracer provider, or you initialize your meter provider first. And then when you're initializing tracer provider and logger provider, you pass in your meter provider as an argument, and it's like, that all makes sort of sense. But, like, if they're all dependent on each other, it gets, like… it gets really messy really fast. You need, like, lazy loading semantics and things like that. So that's something maybe we could provide some guidance on. And the… the… The last thing was, like, versioning around this stuff.
So in Java, we already had internal telemetry long before the semantic conventions existed, and when we… and people depend on those. People built dashboards around those, and when the semantic conventions were introduced, it's like, you know, that's a breaking change to our contract, and so we have, like, APIs that allow you to say, hey, enable internal telemetry and set this version of internal telemetry.
Whether it's, like, you know, our old version or the new semantic conventions version.
And, like.
if you're gonna introduce APIs for this as a maintainer, like, I don't think what we have in semantic conventions is the last version we'll have, so maybe we should think ahead to that and have, like, some sort of capability for selecting, like, the version, and maybe there's only one to start, and just kind of see around that corner, because, yeah, things will probably change at some point.
**Cijo Thomas (Microsoft)** 39:56 We already have ways to evolve semantic conventions, so I'll just assume that we'll just piggyback on whatever we tell our customers or users to do when they're… when they bump semantic versions from one version to another. Maybe I'll let Lyudmila speak first, and then I'll come back.
**Liudmila Molkova** 40:13 To your point, we… we have the… this… approach to… Moving from… specific version of semantic conventions to the new. This is the stability opt-in flag, right? And it can include the, the internal metrics. It would also… we also have the configuration define the generic one that can be applicable. So, as a part of the stabilization effort for semantic conventions.
We would, add the blurb saying, okay, this is how you approach moving on from the previous de facto stable, if you had it.
And also, we should document there that Even though it's only metrics now, later on there will be more signals, so yes, you would have to figure out how to have all the providers initialized together.
**Jack Berg** 41:09 Yeah.
So we didn't do some of these things in Java initially, because we added internal telemetry, like, a long time ago, like, 5 years ago, and… or maybe 6. And so now we're kind of paying the price, and our API just, like, isn't as clean as I would, like, like it to be. And so, what I'm just saying is, like, if we can kind of collect some of our learnings from people that have implemented this, and provide a short supplementary guideline, then I think, you know, they could avoid some of these same mistakes.
**Cijo Thomas (Microsoft)** 41:37 Yeah, and… okay, maybe trust, go ahead.
**Trask Stalnaker** 41:40 Yeah, just part of the problem with Java, and just for… for others to learn from, is that we had it enabled by default.
Which makes, then we can't have a breaking change, right? Like, I mean, it's confusing whether we don't want to take a major version bump in the SDK, And so, how do we deal with… changing the default value. If we change the default, it's going to be a breaking change, and we may decide to do that under, you know.
or not.
But it's… it's good.
Not as simple as instrumentation.
**Jack Berg** 42:26 Yeah, so then the guidance to other languages would be, like, while the… especially while the semantic conventions are still experimental, like, make this opt-in.
And, like, only consider turning this on by default once the semantic conventions are stable. And until then, like, you know, make it opt-in. That's how you protect yourself from the situation we got.
**Cijo Thomas (Microsoft)** 42:46 I can add something like that to the supplementary guidelines, yeah. And regarding the stability, I think we should keep it same bar as any other things we call it stable. So once we call internal telemetry as stable, then breaking that is not acceptable, just like our public AP. It has to be a contract, because that's what we tell our instrumentations and other people in the world, right? You should not break your telemetry.
So we should set example by proving that we also don't do that. If at all we break, we follow the standard guidelines, like pumping somewhere, or emitting schema URL, offering migration. Like, all the things which we tell other instrumentations to follow, we'll just follow it in our own SDK.
And to the other question, Jack, I kind of hinted at, we're starting with metrics.
I expect… Events, not logs, because we generally decided we'll be only doing structured things, so it'll be all events.
I have… try to add one event, just to test the water, like, how it would look like, and it's still in draft, because I'm trying to implement that in, like, at least two languages to see if it's feasible. And also, like, I want the tools to be better, because right now it's a lot of manual work and manual validation.
So once the tooling, when I say tooling, I mean we work.
It can do, like, a lot more, To help reduce the border plate needed by each languages to validate.
So yeah, next is events. I won't try to add, like, a thousand events in one shot, I'll just add, like, one, maybe two events, just to prove that we can document events, and we can call it stable, and people can depend on those events being fired, because sometimes people don't want metrics, they just want events, or they want it to route to their… Looking back, and so, yeah. Events are… In flight, may come, like, pretty soon.
Oh, yep.
**Jack Berg** 44:36 Sounds good.
**Cijo Thomas (Microsoft)** 44:36 Yeah, and for the ordering problem, I have one question. I don't know why we would need an API, because my assumption was that the providers, whenever it needs The other provider, they'll just grab it from the global, so if the global provider wants to get emit metrics, it'll just grab the meter parameter from global. So I don't know if we actually need an API change, it can just work just like any other instrumentation. Is that your understanding, or you have a different idea on that?
**Jack Berg** 45:07 We discourage using the global in Java for reasons, and so, like, we have programmatic APIs that… that you use to sort of In the absence of the global, right? So, like, if we discourage use of the global, then we have to provide these APIs.
**Cijo Thomas (Microsoft)** 45:27 In your language.
**Jack Berg** 45:28 it's common and recommended to use the global, then I guess this isn't as much of a problem.
**Cijo Thomas (Microsoft)** 45:33 Okay.
Got it, so in this… Only through Mr. Water.
**Jack Berg** 45:37 I mean, I don't want to go on a tangent too much, but, like, if… in languages where using the global is common and recommended, how do you… how do you have, like, multiple providers?
**Cijo Thomas (Microsoft)** 45:47 Yeah, that's the same challenge I faced already, like, it's very hard to sequence it in any way. If you start meter first, then you lose logs about meter initialization. If you start logs first.
you lose metrics about logs, installation. So there is always a challenge, which is why I put that escape hatch in the latest commit, which says, like, it's best effort in the startup and shutdown phase. We cannot really… easily solve it. We have solved it in, at least in Rust, what we do is we create a… Throwaway provider?
Which doesn't do any, detailed configuration or any sophistication. It just, like, create a very plain.
provider and writes, it's specifically done for logs, so we create a throwaway logging provider, write things to STD out, and trash it at the end of initialization phase, and then do our normal business. This is because we don't really have an option, because if the… if something has to be there before we can start emitting telemetry.
So again, I didn't put it in the spec because it's very language-specific. Even in .NET, we have a guideline about logger provider. If you want to do logging in much earlier stage of your application, you create a simple throwaway provider at the beginning, and use that during that lifetime, and then your actual things get kicked in. But it felt like too much for the specs, so that's why I put a very simple wedding, to allow that wiggle room, and moved on. But, like, if there is anything better we can do, I'll be happy to work on that.
**Jack Berg** 47:17 Let's let the better, like, emerge from the prototypes. So let's just keep it… everything in development, and keep the spec brief for now, and then as we add things like events, which makes ordering more important, you know, we'll all take a look at the prototypes and how the languages are achieving this, and use that to evolve the spec.
**Cijo Thomas (Microsoft)** 47:36 Okay, Ted, you have hands up.
**Ted Young** 47:40 Yeah, I think, you know, something that we've left out of, like, our current roadmap is, you know, having a review of, like, our general SDK architecture, because that is very much next generation.
But I do wonder if there is, like, value in starting to write down in the spec or somewhere the various limitations and challenges that we're running into with our existing architecture.
Right? Because there's a number of things that come up. This is one example, right? Like, you know, startup sequencing. There's other things maybe around sampling and other things where We've just noted it's a challenge to do things, either figure out how to do things, or to do them efficiently, because… specifically because of the architecture we currently have.
I don't want to open a can of worms and say we should, like, go fix all those problems right now or do an overhaul, but… Maybe, like, starting to keep track of these things somewhere could be useful.
**Cijo Thomas (Microsoft)** 48:45 Yeah, I'll create an issue in… to at least write the supplementary guidelines, maybe use that place to guide or document, like, other challenges. Another thing which I've faced from almost, like, day one is how to prevent the infinite loop, because if you're instrumenting our own.
internal, then we have this infinite loop, right? At least many languages have sold it.
So I'll just write it in supplementary guidelines, because previous attempts to solve that at spec level reached nowhere. So I think I'll keep it, like, somewhat lightweight, keep it in supplementary guidelines, because otherwise I'll be in the boiling the ocean format, where, like, we achieve nothing. So I'll keep it intentionally, like, very slim.
To begin with, and use the supplementary guidelines to at least talk about some of these things.
Yeah, so… Thank you.
**Reiley** 49:38 Thank you.
So, sounds like we've finished all the topics. Still have 10 minutes left.
Any other topics?
Okay.
**Liudmila Molkova** 49:50 What's next on our project review. Do we have a schedule? Does anybody want to present on the next call?
**Jack Berg** 50:00 There is a topic on the agenda for next week. Josh, I saw you scrambling to unmute your microphone. I just slightly beat you to it, so maybe you can jump in.
**jmacdonald** 50:08 Yeah, yeah, I've been wanting to get Laurent to come present, Progress in the Hotel Arrow project for a while. He's agreed to come next week at this time. I will introduce him, and he's going to give a rundown of our performance results, our current state, and so on, which I think will be, quite exciting.
**Reiley** 50:30 Yeah, looking forward to it.
Okay, then we can give 10 minutes back to everyone. Thank you. We'll see you next week. Bye.
**Trask Stalnaker** 50:40 by…
