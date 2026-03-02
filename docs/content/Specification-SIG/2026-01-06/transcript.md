SIG: Specification SIG
Date: 2026-01-06
Duration: 66 minutes
============================================================

## Zoom Recording Transcript

unknown 00:04:47 Okay, can you hear me?
unknown 00:04:50 Yes.
unknown 00:04:52 Wonderful.
Yeah, welcome to 2026! I am going to run the call today.
Give me a second.
Here we go. So add your name to the attendees list. If you have anything to discuss, please add the topic to the agenda.
And… Let's see, do we have people? We have… Quite a few folks here.
So maybe before we go to the agenda, we are due for release, right? And
We should probably merge the complex any value type
Before that, and then release. Carlos, do you want to release, or should I… I can release as well?
Carlos Alberto Cortez 00:05:55 You can release that. I think that's your, this week is your rotation, so, yeah, you can do that.
unknown 00:06:02 Cool, yeah, I'm glad you're… Letting somebody else do it.
Cool.
Okay, so let's talk about the complex NU value type.
We have the… approvals, but just a few, I would love.
to see… more? Do people hold back their approvals, or they just didn't rubber stamp it?
Okay, I'll, I'll, I'll pink.
TC folks in the chat, but I'd like to merge it.
Tomorrow.
unknown 00:07:03 Yeah, I think we should merge it, but yeah, ping… it would be nice to have another…
Let me just double check with TC folks.
unknown 00:07:13 Yeah.
Jack Berg 00:07:14 And remember that approvals are meaningful, even if they're not green.
unknown 00:07:21 Right.
Anything we need to discuss here, beyond purchase things?
Doesn't seem so.
Okay.
Wonderful. Moving on to the next slide.
Topics, table, by default, ATAP.
Carlos Alberto Cortez 00:08:16 Yeah, this is…
unknown 00:08:16 What's…
Carlos Alberto Cortez 00:08:17 I put this one here, Austin created that one. Please review that one. I think the summary, I can just read that, you know, the first line, DOTEP proposes open telemetry distributions.
only use stable components. That would apply mostly, it seems, initially, to the Java agent and the collector.
Basically just changing, you know, the paradigm in that regard.
I think Austin is not here, so we don't have to discuss that one, but please take a look. It's not in draft.
unknown 00:08:48 So I think people should be reviewing that already.
Okay, does anybody want to bring anything up from the top? Any particular topic? I'd like to bring one, but it's in the…
In… in Mayo.
Okay.
Then moving on to…
Carlos Alberto Cortez 00:09:19 Yeah, likewise, there are approved metrics, PRs, please take a look. The first one, well, both of them are from Baby Dashboard, I think.
The first one is to add a new advisory.
Parameter called opt-in.
It's in development.
So it could be fine, but still, we need more eyes on that one. It has some approvals,
So that's great, but we need more eyes.
Jack Berg 00:09:51 I haven't read this yet. I think this is a good idea. At least I like the idea of having things turned off by default.
It kind of reminds me of, like, a severity number for logs.
And we've talked about severity as a concept for traces, and I don't think that's gone anywhere.
like, you know, I guess my only thought on this opt-in metric advisory parameter would be, like, is this an opportunity to have some sort of unified concept across signals?
Versus something metric-specific.
That's a very hot take, though.
Carlos Alberto Cortez 00:10:30 Well, this is a development, on development items, so it could be a good timing to try out something for tracing. Like, it's probably now the best time.
David Ashpole (dashpole) 00:10:44 I do actually also list, metric levels as an alternative.
In the… in the PR description.
Jack Berg 00:10:55 Just read the issue, Jack.
unknown 00:10:59 Levels are challenging, like, like, what do you… like, picking a level becomes very challenging, is my only…
Where I like… I mean, I like the simplicity of…
Off by default, and people can opt in.
Jack Berg 00:11:17 Yeah, like, especially when you go in the logs direction and have 24 levels.
unknown 00:11:27 I did leave just a comment a few minutes ago, David, I don't know if you want to
discuss it.
which is that, so the, the way…
David Ashpole (dashpole) 00:11:44 I was trying to understand the way that…
unknown 00:11:47 Users opt-in to this, once we've marked it as… Off by default.
And it looks like the approach is they need to add the aggregation, like, in the view, they need to add an aggregation.
David Ashpole (dashpole) 00:12:04 So, in… I was trying to figure out if there was a way to make your request work,
You can specify default aggregation, But that will also give you the default histogram buckets? Like, so…
In your view config.
One of the things you can specify for the aggregation is, I believe, default aggregation?
So there is a way to just… Turn a thing on?
Without providing an aggregation, or, like, without, you know, writing out all the buckets or whatever.
But…
unknown 00:12:41 And that default there means whatever the instrument
that was used, like, if I use a counter, or I use a… Histogram… It'll be that.
David Ashpole (dashpole) 00:12:55 Yes, but I think… Let's see, where's… yeah, default aggregation says…
Oh yeah, yeah, and it says histogram explicit bucket histogram aggregation with the explicit bucket boundaries advisory parameter, if provided.
Jack Berg 00:13:11 So that's good. That means that, like, the recommendation here would be to choose the default aggregation if you want to enable this instrument, and you will… it will play nice with the explicit bucket histogram advisory parameter.
David Ashpole (dashpole) 00:13:26 Yeah, which is actually pretty insane that that works out that way.
I'm happy with it.
unknown 00:13:34 Yeah.
David Ashpole (dashpole) 00:13:36 It's good to document it somewhere.
unknown 00:13:37 Yeah, I'll leave a comment. I'll follow up on my comment and ask to add, like, mention that in there, that how users can opt in.
Or the recommended way for users to opt into it.
David Ashpole (dashpole) 00:13:49 Yep.
unknown 00:13:54 I really like Jack's suggestion to consider extending it to other signals, probably not in the SPR, but in general, but I'm… it would be difficult.
His… it wouldn't apply to a tracer, it would apply to a span, right? And we would need to pick a tracer
To make it opt-in.
Jack Berg 00:14:15 Yeah, exactly. It's not the right granularity.
Exactly, that's the tough part about this, is like, you know, we want to have concepts that are signal agnostic, so there's more in common across the signals.
That's the argument to generalize this. The argument to keep this metrics focused is, like, metrics already has this advisory parameter feature, and we're just adding to the set of advisory parameters, and there's good tools and metrics around, like, configuring things that are, you know, related to advisory parameters via views. And so the other signals don't have that.
Right? So, like, if you wanted to bring an advisory parameter type concept to spans, you'd need an advisory parameter-like configuration, concept as well in traces.
And that's just missing, so it becomes sort of like a boil the ocean thing.
David Ashpole (dashpole) 00:15:05 I mean The advisory parameter concept just means, like.
we want to add things to the API without requiring SDKs. It just means that, like, they're kind of optional for SDKs to implement.
Of course, our SDKs implement them, so, like, we can add…
we can add more options to start span, right? I think we have, in fact, added, like, extended…
the span.start API in the past, so we could add an opt-in flag there. I think the…
the harder question is, like, what's the mechanism for turning it back on? Because that will not be consistent if we use views here. So if the view is the mechanism for turning something on.
then, like, what does it mean in the Tracerland, or…
unknown 00:15:53 It hurts us again that we don't have identifiable spans. For metrics, we identify them by name. For spans, we have no means.
unknown 00:16:03 Does it tie… can it be tied into the,
The enabled flag we have already in development on meters, loggers, tracers…
David Ashpole (dashpole) 00:16:19 So that's a good, I think… that's the best idea I can come up with as well, which is, like.
We could use that to turn off The entire tracer by default?
If people wanted, and then use the enabled flag as a way to turn it back on. I do feel like, for metrics, having a per-metric
Opt-in, opt-out is… necessary for a lot of instrumentation, that, like, meter level would be… Maybe not granular enough.
Jack Berg 00:16:52 Yeah, that's actually, like, an interesting observation there, that tracers
All the spans that a given tracer records are probably at, like, the same level of the hierarchy, and they all look very similar, but, like, the metrics within a meter can be very different things, like.
You know, when you're collecting metrics about an HTTP server, like, some are essential, some are non-essential, but they're all part of the same logical meter. And…
you know, So what does that mean in terms of…
like, having this type of capability in Traces. It means we might already be there with Tracer Configurator, right? So if you implement that.
then, you know, you already have control as a user to turn off an entire tracer in all of its spans. And, like, do you need more granularity than that?
Maybe not.
unknown 00:17:43 The only example that's jumping to me is,
like, HTTP, we have, some, like, connection level spans that we capture in Java, at least, that are off by default.
But the main, you know, the normal HTTP spans are captured by default.
Jack Berg 00:18:05 You could, of course, have those in a different scope, but, like, you know… Yeah.
Maybe…
unknown 00:18:10 the bad option.
Jack Berg 00:18:12 Yeah, like, but that's kind of going in the direction of, like, you know, when all you have is a hammer, everything looks like a nail.
Right? So, like, you know, is that actually the appropriate vision for how to use scopes? Like, what would we rather see? Like, a unique scope for each distinct class of spans? Or, like, you know, all of those spans for connection and the actual, you know, more important
You know, server spans or client spans under the same… under the same scope.
unknown 00:18:46 The idea of, Advisory… hints on…
spans has come up before, trying to think, I think for, like… Oh, what?
But Mila, maybe… If you can… maybe…
HTTP request method around that, we were…
unknown 00:19:21 the enrichment.
So you would provide… Enrichment from somewhere else.
I, I don't, I don't remember those params, but the spend type is the…
ability to identify spans, and then… advisory params and spends are cool, but how do you…
configure them on the user side. We need span identity.
And we'll get back to you on this, for sure.
Jack Berg 00:19:53 Well, maybe you don't need an identity luteamela, maybe there's, like, a stand-in. So, like, if we already have Tracer Configurator that allows you to identify, you know, groups of spans by their scope, and enable them or disable them, maybe you just need, like, some other small distinction between the spans in a scope.
Because, you know, we talked about how there's, you know, this HTTP case. There's two classes of spans that an HTTP's client scope might want to record. The connection spans, and then the, you know, the actual request spans. So, like, you just need some way to distinguish between those two classes of spans.
And then you can have, extend tracer config to, you know, be able to select those and enable or disable.
unknown 00:20:35 Yeah, so, so far we are relying on, like, some heuristics that are very inconsistent across different spans.
And I think it's, it's…
it has limitations, and, like, for example, I can automatically validate
that certain instrumentation emits compliant metrics. I cannot do this for SPENS.
So as long as this heuristic is reliable, and it does not depend on the user, let's say, accidentally using the wrong API and not providing the identity.
And, it wouldn't work. Josh, you are… you have your hand raised?
Joshua MacDonald 00:21:17 Hi, everybody. I'm not sure I'm…
in the right point in the conversation here, but it seems like we've diverged into two conversations, am I right? There's one about making tracing consistent with what we're talking about for logs, right? I want to remind us that, I mean, years ago, Yuri made a proposal
Called compiled spans, and the question was, you know, we have metric instruments where you declare them with names, and they have identities, and you have tracers where you just start a span with any old string, and it seems like something's missing there, and you could actually optimize your tracing interface quite a lot if you would compile the span, meaning to declare it with…
properties, names, it has a scope fixed every… you could, like, pre-encode half of it. Like, there's a lot of work you could do if we just would declare the spans before we start them.
And I think that that would bring us much closer to having consistency between metrics and logs.
You know, when someone says, this is a little bit of loose, a loose, dialogue here. When someone says that they wish they had view, you know, that metrics are special because they have views, I'd like to remind us that we should have views for spans. We should be able to configure tracing, attribute filtering.
all the same things that we want for metrics. Like, there's an equivalent functionality for spans, and just have a little bit of a prototype someone's working on for me based on KQL. I'm not sure that's what anybody wants, but you could imagine a filtering query language being your view definition for logs and spans, so maybe that's where you're steering this?
But for the original topic, that David raised, I'm concerned that we've lost track of what the collector's SIG is doing.
in this same actual area. So there's a metadata YAML file that each component defines, and there has been some work recently to… so the collectors had a metrics level from the beginning, so it's got basic… it started out with names that didn't match logging at all. It's got basic, it's got normal, it's got detailed.
And I believe that they've retained some of that. I don't know the current state exactly, but if you look at the declarative config for the collector metrics, it's got the same declarative configuration that we all have defined, plus this level concept, which is totally off-spec. So I'm wondering if there's already a precedent for using metric levels.
So all I know is that we recently… we've been trying to add histograms in the collector, and many people are saying, whoa, I don't want that by default. So, but there was no mechanism to disable by default. The way that they… that group has started to attack it is to have the metadata YAML, which is a close to an opt-in advisory type of parameter.
actually say this is disabled by default, or use this as an opt-in metric. I can't remember the exact syntax. So this seems like we've diverged a little bit in that space as well. Just wanted to remind us of that. And that's it. Thank you.
Tedsuo 00:24:07 I just had a quick note, kind of following up what Josh was saying around templating things and stuff like that, is another area we're looking at with Weaver is what I've been calling semantic APIs, like, how do you auto-generate
APIs for generating, you know, HTTP spans, SQL database spans, things like that.
If we do find success with Weaver in making those kind of APIs, it's just another place we could think of around doing some of this templating and automating some of this stuff for users.
Just wanted to remind people that's an option.
unknown 00:24:54 Cool. So, I think… David, would you check with the collector?
David Ashpole (dashpole) 00:25:01 Yeah, I'm very familiar with.
that they're…
metric levels. I'm… I'm personally not a huge fan, which is why I've been a little quiet. But, I will go take another look and make sure I… I understand the latest.
On that front. Thank you.
Jack Berg 00:25:20 The one thing I'll note with, like, this metric levels discussion is… It's sort of…
If you go with a metrics level type of thing versus just, like, advisory parameter where it's disabled and then you enable with views, a metrics level sounds like it's more appropriate to configure with, with, you know, meter config than views.
And so it kind of… like, we've had this discussion in the past about granularity of configuration. Should you configure things at the view level, or the reader level, or the scope level, or the meter provider level?
And, like, every question that comes up about a new capability, we kind of have this same discussion again. And view is the most granular, so that's, like, that's a nice thing to do. But, you know, it has usability concerns, because views don't merge nicely together, right? So, like, adding configuration at the view level is not without issue.
So, just something to think about, like, you know.
does having it be configured via views or meter config make more sense from a UX standpoint? Also, some language SIGs have resisted implementing meter config, tracer config, logger config, so that's, like, kind of a dynamic going on here, so…
I'll stop.
Carlos Alberto Cortez 00:26:43 Yeah, I think there's enough information to discuss, in the future, yeah.
If… if it makes sense, I would like to go to the next item. I think they verified… it was also created by David, by the way. This has been open for a bit
Longer time.
It's about adding this development for, you know, part… per time series, start time tracking. Jim McD already reviewed that, and other people have, but we didn't realize.
And it had relatively a lot of traction before the break, so it would be nice to, you know, to make it to the end line.
unknown 00:27:23 Is there any discussion we need to have, David? Anything to bring up?
David Ashpole (dashpole) 00:27:31 Sorry, muted. I don't think so. I just saw, Tyler's comment, but I don't think we need to discuss that here unless…
Yeah, I think we can move on.
But more eyes would be appreciated. Thanks.
unknown 00:27:45 Thank you.
Okay, then moving on to support for distribution config and config provider.
Carlos Alberto Cortez 00:27:54 Yeah, I put that one there. Jack, maybe, you know, no, we… basically, this is for adding to the configuration files, some section for the vendors to put their stuff. Jack, you made a comment there, I don't know whether you want this… this is the place to discuss that. I was thinking probably…
it should be discussed in the complex C first.
Jack Berg 00:28:15 Well, we had the config sig yesterday, and none of the people that were kind of proposing this were in attendance, so this was not a topic we discussed.
If anybody has any additional thoughts on this, I'm happy to discuss now.
My comment on this issue sort of makes my position clear.
unknown 00:28:36 Can you summarize?
Jack Berg 00:28:38 Sure. So, we have this thing called config provider. It's the config analog of meter provider, tracer provider, logger provider, and the point of this is to give instrumentation access to, you know, configuration during initialization.
So, you know, they can, you know, standardize configuration around things like that semantic conventions talks about, like, you know, which HTTP methods, should be recorded, and the style in which they're recorded, and whether database statements can be recorded, that type of thing.
And, so when I initially wrote the, the spec for this, I kept config providers scoped to only be able to access the portion of configuration that is related to instrumentation.
you know, you don't have an API for accessing SDK configuration. You can't go walk the SDK configuration tree and go, for example, potentially access, you know, sensitive API keys that are used in your OTLP exporters. That was an intentional design. So, the question here is.
okay, this person wants to propose extending config provider to access a new part of the config schema called distribution. There's a new block where distributions can have, you know, specific
you know, configuration properties. And distributions, you know, will naturally have sensitive keys in them as well. And so, if we expose this information in Config Provider, that means that instrumentation has access to all of the information
configure information of distribution. So, Is that a concern?
That's the question here.
And the proposal that I lay out here, you know, I think that distributions can access this information without extending the API as well. So it's like, you know, is this really needed? And if this is needed, like, do we care about the security concern of it? That's kind of where my head's at here.
Carlos Alberto Cortez 00:30:32 Yeah, that's correct, and I think that's basically something I would like to see from other people if they have an experience. This looks good on paper, but the security concerns are bad enough. Like, you don't have to expose, like, the secrets and all that.
So yeah, if you have any opinion, we don't have to discuss that here necessarily, but please take a look, especially if you work for a vendor and you are considering putting, you know, information in that configuration file, and you think that that's not good for you.
Jack Berg 00:31:00 I mean, on the other hand, instrumentation, if somebody is initializing instrumentation in their application.
in this… in this instrumentation is, like, malignant. Like, it can access these secrets. Like, if it's motivated, it can go and access this information anyways. So, you know, what we'd be doing here is adding some friction.
unknown 00:31:24 I, I'm, I'm,
The security concerns are valid, but yeah, as you mentioned, it's in the same process anyway.
the abuse is something I'm worried about. We see people in instrumentations who, maybe are not familiar with up in telemetry trying to use SDK concepts, and they would definitely get their hands on the SDK configuration if they could. I'd rather not let them do this.
Jack Berg 00:31:49 Yeah, the classic thing being resources.
unknown 00:31:52 Right.
unknown 00:31:55 Yeah, I was pretty convinced by, Jack's… Comment,
I don't… I thought that we needed this, for example, for the Java agent, distribution.
But, it makes sense to me that the security piece…
isn't as compelling to me as the SDK-API separation feels…
right here, by not… by not adding it. At least… and I think Rob, who sent this PR, the… it was for a Java agent distro, for Splunk anyways, so…
My proposal would be to, close this for now.
And wait and see if we really… Needed.
we're just building out support for this in the Java agent currently, so I'm planning to try out what, Jack's proposal here.
Carlos Alberto Cortez 00:33:08 I think we can leave a comment there saying that you said trust, like, we're going to close this, we are planning to close this,
Like, please, you know, comment if you oppose that, but we are looking for other alternatives.
Jack Berg 00:33:21 And since this person is involved in the JavaSig, you know, directly, we can… Trask and I can work with them and make sure that whatever use case they're trying to fulfill, you know, accessing this information from the Splunk distribution of the Java agent, we can make sure that, you know, we work with them to make sure they can do that.
So that they're now clocked.
Carlos Alberto Cortez 00:33:41 Yep, would be great.
unknown 00:33:50 I'll retract my… Approval to make it.
It's less… more clear, also.
unknown 00:34:09 Okay, moving on, to the next topic, it's mine.
I'd like to socialize the thing we are working on in, semantic combinations on Weaver, for the schema V2, and the way, the part that it affects.
the specification. Let me walk you through. It's currently work in progress, there are some details to polish, and some relatively small decisions to make, but I'd like to get your high-level
feedback thoughts, and just for you to be aware of the things we are trying to achieve. And I think it has a lot of intersection with the, stability OTAP.
Okay, so, what… are we trying to achieve? So today, when we, when people
receive telemetry. Sometimes they receive schema URL. Hopefully, they would see more of a schema URL, and by looking at the schema URL, they can see, the
registry, like OpenTelemetry, and the version.
But if they open, the file itself,
what they see is pretty much this, right? This is the file format 110,
This is the schema URL, and then there is a list of changes. These are renames, so, like, for example, at some point, we were named Messaging Kafka Client ID to Messaging Client ID.
It does not provide definitions, and it cannot be used for, let's say, validation of arbitrary things.
Right, so, assuming there is just semantic conventions Registry.
It kinda could work, because you… you can,
pre-fetch all the semantic conventions repository, and get the data from them, and you can be aware of them. With semantic conventions growing, and with a lot of different components trying to,
create their own conventions, documented or not. It cannot work anymore.
Companies would like to define their own conventions, and we, even us inside semantic conventions, we want to decentralize. We want collector to define their own conventions, or Java repo to maybe define their own. Essentially, we don't want to own all conventions in the world.
So…
We'd like to find a way to share the schemas so that the consumers could be aware of the schema used for the telemetry item.
You can imagine you open your visualization tool, and you hover over an attribute, and you would see a tooltip with the attribute brief, or note, or both.
And examples. And there are a lot of other things, like, for example, the opt-in thing that David shared previously, it could be part of the definition, of the metric. It is part of the metric definition, actually, the requirement level.
And, the… you could say, okay, disable all opt-in metrics in the collector, for example, drop them, and it's part of the… the processing pipeline. It's not as efficient as disabling them to start with, right? But this is the concept optimization strategy.
And there are plenty of other scenarios where this could be, useful.
So what we'd like to do, instead of, the…
File format 10110. We would like to propose a new approach.
First, instead of the schema itself, we would return the file, the manifest.
It would be just the metadata.
It would be a major break-in, major version update.
The manifest will include the stability.
And we would publish two versions, the Everything, the Development and Stable, For each version we release.
Inside the manifest, you would get the link to the actual schema.
So my, my hope is that, and I will try it out, that if we… we can let browsers
decide and HTTP decide if it's, zipped or not.
But essentially, this thing contains everything you would want to know about the, semantic conventions.
So, the resolved schema…
is what would be returned. It's like a minified version that all of the semantic conventions are compiled into one file in an optimal way.
But you could see, let's say, there is a metric definition, and it has References, indexes of attributes.
We, have it implemented in Weaver, we're still polishing the implementation, but essentially, it's defined, we can take a look at the definition and the documentation for it.
Yeah, the important part, yes, we will publish two of those things, and this would be the way for instrumentation to…
say, If they are producing stable telemetry or unstable telemetry.
you should be able to import the schema if you're developing your own semantic conventions. We don't have an example for it yet, but it's possible, you should be able to import the schema
And say, okay, I only care about this 5 attributes from it, and I'm going to define my own things on top of them.
I should be able to publish this.
If I want to, and I should be able to stamp the schema URL, the telemetry that my instrumentation produces.
Phew, I talked a lot. Any… Questions or thoughts?
atoulme 00:40:37 Like, if I may. So, my understanding is that all those changes that you allow multiple repositories emitting those conventions, and that you would like multiple projects to have their own conventions, which makes sense,
Would you…
from… how do we make this real? So, for the collector SIG, would we want to have semantic conventions hosted inside the repository? And would we then have some sort of a tie-in that go back to the semantic convention repository with a version number?
That would allow us to identify which version of it is being imported?
unknown 00:41:18 Yeah, Josh, you want to answer this? I can answer if you wanted to talk about something else.
Josh Suereth 00:41:23 No, yeah, I was gonna… I was gonna answer this. I think I said the same thing in this events convention sig, so if you wanna… if you wanna answer it, feel free. I was just excited, because this is what I'm working on.
Yeah, so the… if you make a schema for the collector, you will be able to depend on semantic conventions, and it will remember that dependency. So you'll be able to say, like, the collector's gonna depend on semantic convention version X, and then inside of this file, we might actually show, like, what your dependencies are, so you can know that you're depending on that version.
But the resolve schema will be fully consistent, so, like, your resolve schema will have a duplicate, if you will, of, like.
atoulme 00:41:59 Yep.
Josh Suereth 00:42:00 The things you need from semantic conventions.
I do want to emphasize, so I'm gonna… that was the answer to your question, hopefully, but then I also want to emphasize that the… the part about diff going away, right? Current telemetry schema is only focused on diff, and has, like, all the versions listed with changes between it.
atoulme 00:42:19 The idea here is we'd rather focus on definition,
Josh Suereth 00:42:23 I'm being cute, but definition versus diff?
And then Weaver will be able to give you back diffs if you need it, where you can look at two versions and say, what's the diff? It turns out the diff algorithm was actually relatively trivial with our new Resolve schema.
Which we're pretty happy about. And the previous diff thing that we were maintaining, we broke all the time and was completely untested, so we think you're in better shape than you were before.
atoulme 00:42:47 Okay, good to know.
Do we want to have an open issue on the collective seek to start to work on that?
Why is it too early?
unknown 00:42:56 Let us, create… we have a section here for the, importing and decentralization.
Let me write this section down so you have a more clear recipe, but yeah, I… feel free to create an issue, and the… I would love to know a little bit more from the collector side, because you folks have the schema processor that we're going to break.
It's, it has some fun…
atoulme 00:43:25 it's not really working well, from what I understand. Like, we have a really old PR that's just been sitting there to kind of reformat it, and I think it's not a bad time to rethink it.
Yep.
Josh Suereth 00:43:41 One thing I'll add is, I think there's a few, like, this is an OTEP, which means it's a design doc. So, Weaver is very close to this, but it's not actually done yet. There's, like, 3 or 4 features in here that we need to finish before you can just, like, go ham in the collector and make it work.
So, what we want is look at this experience, right, as a design doc, and, like, agree to it, and then when we have those features implemented, we'll let you know. Some of those features you could start trying out today, they won't look exactly like this OTEP, but you could start looking at, like, having your own
Weaver config that depends on Semcov, you can try that today.
it won't be the way we want it to work fully, like, in this end state, but it's close enough that you can try it out and see what works, see what doesn't. Open bugs so we can fix them prior to depending on this, right? So if you consider it, like, beta experimental work, that would be really valuable if you wanted to start that now.
atoulme 00:44:41 Yeah, we do have a couple, fouls.
We have a schema that we played with in Collector.
And so maybe that's the start.
Right? So, doesn't have to be a big investment.
Josh Suereth 00:44:55 Exactly, and please continue to open bugs for us to fix, because I think you guys have gotten a lot of good feedback to us on, like, things we can improve and features.
atoulme 00:45:04 Yeah, glad to be users. That's cool.
Okay.
unknown 00:45:10 Yay.
I think there is a lot more we can talk about here, but I… we have a couple of other topics that I think also deserve time in this call. We will keep providing updates on this one. This is not the last time you hear from us.
Okay, Anton, Finnish method, do you want to share, or do you want me to share?
atoulme 00:45:36 I can share. Let me open the issue. Well, you're already sharing, so… oh, alright, I'll share.
Here.
So, this used to be called Remove.
It has been an open issue for a little while.
Let's take a look at when it was opened, I think it's 2024… 2021. So we want to be able, in the synchronous, use case, to unregister a set of instruments, right? So you have been reporting a particular time series with, let's say, two to three…
Two attributes, right? And this time series needs to stop being reported because the thing that you're instrumenting for has disappeared.
In my case, for the Java conscript repository, we have the use case where IBM MQ is going to report information about a queue manager, but the queue manager is being decommissioned and needs to stop reporting information. Otherwise, by default, with the type of aggregations we do, you would be reporting the latest points until the end of times.
Which creates 3 issues for customers, right?
So what we want to do instead is to have a way to explicitly say, hey, this is no longer reporting, we will stop reporting this particular gauge counter, what have you.
So we decided to work on that, and there's a set of diffs that came in. There's some feedback, and this is a bit tactical, but I need to understand how to move forward.
The biggest feedback I got, thank you, was from Josh. Let me see here. That feedback is, I do not like the fact that you called it remove, which is fine. The name… naming is hard, right? That's the number one problem in computer science.
We're not removing anything, we just stopped reporting this, so let's actually make that official by calling it something like Finish. And Finish is fine, it's… okay, whatever, right? So, we can change the name.
And then, the discussion veered towards what do we want to do to let the backend know that we are actually explicitly finishing reporting this information.
And I think this becomes a bit more, difficult to explain. So,
what we need is a specification of how the touch will be transported so that the ending of a series is clear. In Prometheus, we have the not a number value, and in other, we have the missing data point flag, but we never specified how to set that flag.
I would like to see a specification that dictates is dedicated. I have to remember the finishing series long enough
To send a not number missing data flag to each reader at least once.
So, that was actually… that's one problem, right? The second problem is, from David, we need to also make sure that we don't have overlapping time series with the start time.
In the new…
the new series kind of overlap, so we take down the transaction, the queue manager in our IBM MQ, and we bring it back up, and there's some lag on the clock, or something like that, and now you have two time series that are overlapping each other, and you're in a quagmire of problems, because you don't know what you're doing.
Okay, so that's fun, but I wanted to talk about, so far, right, the work we've done is just to make it possible to open an API in the SDKs that,
stop reporting this information, but these are considerations which are much deeper, right, my opinion, and there's at least two of them.
I would like to see if we should try to do this in one PR, if we should kick that out into a separate set of PRs, because they might be easier to tackle on their own.
And, there's some other feedback here from… I think it was mostly David that started on talking about this.
Yes. So, there are a few minor benefits, right? So, we could say the end time of the delta interval to be the time at which this reset was removed. This would make rates more accurate, so I think you're agreeing here with, Josh, right, David?
David Ashpole (dashpole) 00:49:42 Yeah, yeah, I think this is the question of…
I was just trying to answer the question of, is this a cumulative-only feature? Like, is remove… is remove a no-op for Delta?
And… I'm trying to make the case that
It could be a no-op, but that it would actually be… it would have some minor benefits if it actually did something.
atoulme 00:50:03 Right.
Plus, I mean, you can always take a…
you can take one and translate it over to another, like, you can go from data to community. There are processors that do that, so…
And back and forth, right? So, okay, anyway, so it looks like we're… there's a broad agreement that the two considerations that Josh brought up are valid. I've not seen anyone say, oh, no, no, I don't think we should do that, if there's anybody on this call with different advice.
David Ashpole (dashpole) 00:50:30 I will actually say that I think the…
sending NAND values, or something similar to indicate the end of a series, to me is not a blocker for adding the API. But I do think fixing how start times are set is a blocker for adding the API.
atoulme 00:50:45 Okay, good. Okay, good to know.
David Ashpole (dashpole) 00:50:46 That's my personal opinion. I still think, staleness markers are maybe useful.
I do worry that if we just start sending them, that it'll cause a lot of disruption as well, so I think that needs a lot more thought.
atoulme 00:51:02 Yeah, yeah, I like the… okay, stellness Marker is a good name for this feature. It's difficult to articulate.
David Ashpole (dashpole) 00:51:07 That's what Prometheus calls them, so I'm just stealing their…
atoulme 00:51:10 Oh, well, great, let's not reinvent anything, I agree. That does make it that the statefulness of this is a bit more important, too, because now you don't just tell that you finished, you have to let it know, hey, you need to at least send it one more time. What does that mean? And do you track for success?
Or you… attempt.
Right? Like, if for some reason the export failure fails, do you reattempt to send the stairness marker, or do you just drop it?
I don't know.
David Ashpole (dashpole) 00:51:42 Yeah, I…
I think if we wanted to open a PR or an issue to discuss the design of it, then I think we could. But what I would like to say is, I think the biggest blocker to this PR is actually just that it doesn't have the SDK spec at all.
atoulme 00:51:58 Yes, so that came up, yeah.
David Ashpole (dashpole) 00:52:00 To include that. Otherwise, I think this is mostly, like, ready for consideration.
atoulme 00:52:05 Yeah, I wanted to get clarification on those two issues before I went into the SDKs, because the SDKs, if it has to have the stillness marker.
then, well, I have a bunch of work to do. If it's just the start time discussion, then we can put that to the SDK. I do have, yes, here, a request for change based off that. We've started to work over the break over the SDK, but I was a bit,
unsure how to go about this, so I added all of this, which is really not that much.
And, I think I need to decide the paragraph about what the behavior of the SDK should be, and then we can be… we can be on our own going.
Okay.
Jack Berg 00:52:46 Right.
We talked about the staleness marker, I just want to say something potentially obvious. Staleness markers are already a thing in the proto-definition.
Tell them about that. Okay. They are. So, it's just like, you need to have SDK instructions that provide guidance around
populating that field that is already there, right? So it's not like you need to go and modify the proto to add this concept. So that's one less thing to do.
atoulme 00:53:15 Okay.
Okay, good to know. Thanks.
Okay.
Yeah, that's… that's about it. Is there anything else that you'd like to talk about?
Okay, moving on, thanks.
Next person, please.
unknown 00:53:35 Next person is dead.
Tedsuo 00:53:37 Yeah.
unknown 00:53:37 I wanna go.
Tedsuo 00:53:39 Totally. So, this is maybe just kicking off the discussion. We got about 10 minutes. We can continue this discussion next week, and I might even try to raise it among the maintainers to get more maintainers to show up. But, this is just a general
thing we're trying to shift in OpenTelemetry, from a project management standpoint.
we, for a long time, had kind of a de facto roadmap and a North Star, which was we were building the project out through a spec. We had a set of, you know, SDKs that were being built out kind of at the same pace that the spec was getting made.
And we did the spec tracing, then metrics, then logs, and that allowed us to get feedback
from SDK maintainers and have a bit of cohesion.
But we've now kind of finished that initial mandate of tracing metrics and logs. Logs are getting stable, but we still have lots of work to do.
And we've got more SIGs, language SIGs than ever, and they're all in kind of, like, a different place.
So we feel like if we continue forward without some kind of, like, coherent roadmap or way to focus our efforts, if we just keep adding things to the spec ad hoc, and SDKs keep pulling things off of the spec, kind of…
as… as they like. It seems like all the SDKs will start to really diverge from each other, in terms of what features are available, even if they're all still following the spec.
And it would make it harder to have, like, coherent spec discussions.
So, on the one hand, SDKs need room to deal with language-specific issues and move at their own pace. On the other hand, we'd really benefit
From being somewhat organized, In, like, our initiatives and topics and things going forwards.
Things we know we want to focus on. One is stability.
Getting… in order to graduate, we've identified just not having things marked stable. It's like a big blocker for a lot of, like, users on the other side of the chasm, so we want to get everything marked stable that is stable, and the things that aren't stable that people need, you know.
get them stable, so that's an example of an initiative. Another cross-sig initiative would be config files, right? Like, if we think config files are important to OpenTelemetry, we want to kind of coherently roll them out.
So it's not like everything, but it would be helpful to be more organized.
But stigs are in a different place. So, before the break, I was actually having a good conversation with Daniel Dila about how to do this.
He was recommending that just kind of maybe beefing up the liaison program to just have a more direct connection between the GC and TC and the different SIGs around
Meeting with the maintainers, and…
seeing where they're at and having a discussion about whether this SIG can participate in these initiatives, or are they too early in their journey and they need to focus on other things?
some cadence of checking in with SIGs about how they're going to participate in these initiatives, and then having some set of high-level initiatives that we're focusing on in these meetings. I think that was the basic idea, Daniel. I don't know if you had some color.
Daniel Dyla (Dynatrace) 00:57:11 Can I add real quick, because I think it was an important part of it.
Tedsuo 00:57:15 What we had talked about was the idea that every SIG.
Daniel Dyla (Dynatrace) 00:57:19 Should have a charter.
Which, for the record, our governance docs say is the case, and is definitely not, so…
That's been a problem since literally day one.
But I think if every SIG had a charter, including ongoing language SIGs.
Tedsuo 00:57:39 Yeah. That was renewed on some cadence.
Daniel Dyla (Dynatrace) 00:57:42 Like, a year or whatever.
where the language SIG could go to the TC and propose, this is what we're currently working on.
this is what we hope to achieve in the next year, and have some check-in with, whether it's the TC or the GC or both, some charter approval committee of some kind, doesn't matter who it is for the… for right now.
it would both give the TC a better idea of where each
implementation SIG currently is, and what they're working on.
And it would give…
an opportunity for the TC to say, we would prefer you work on this, that, or the other thing, because we view them as higher priorities for the project. Or to say, we understand you're not there yet, you're, like, you may not be…
At a place where you can work on declarative configuration, because you have these other things that are not yet implemented that are higher priority.
You know, whatever the case may be, it's a sink point that's been entirely missing.
from the project for the… for almost the whole history of the project, essentially, in my opinion.
We have SIGs that start up and then kind of run on their own, and there's very few, if any, sync points between them and project leadership.
Tedsuo 00:59:12 Yeah, up till now, the only real sync point we've had is when, SIG wants to declare a signal stable.
that triggers a TC review.
Daniel Dyla (Dynatrace) 00:59:22 Yeah, and I'm not sure how often that even…
Tedsuo 00:59:25 Right. Happens, to be completely honest. I spoke a lot there, but the charter.
Daniel Dyla (Dynatrace) 00:59:29 the charter with a specific timeline and a renewal process for it was the important part that I wanted to specifically inject.
Tedsuo 00:59:38 we have a concept of project files and projects that seem to be getting popular. It's interesting, we've had more SIGs come to us and say, like, hey, we don't want to start a new SIG, but we want to start projects. I think
So I think I'm getting signals from SIGs that, like, more organization around, like, this kind of stuff is helpful, and, like, helps people accomplish things. I think it can also help bring more end users into participating if we're…
If we can announce, kind of, what we're focused on and what we're working on, end users tend to want to work on, like, specific things, not be forever maintainers.
Anyways, at this point, I'd love to hear more feedback from maintainers.
We're out of time at this meeting. I'll be going around to maintainers, but next week, maybe if we could get…
maintainers coming into the call, maybe just with some feedback and experience about how things have been going, and like… like, how much direction they would like, how much they would like to… to work with other SIGs.
On new, you know, in this matter versus wanting to kind of focus and have independence?
We would just love feedback. So maybe next week, if you could come with some feedback, that would be helpful, either here, or feel free to DM me if you have ideas. I'm just trying to compile everyone's feels about this right now. So that's what I've got.
Cool.
And we're kind of at time for this, so I'm gonna try to bring it back up next week and see if we can get some more maintainers to give their thoughts.
unknown 01:01:22 Thank you.
Okay, see you next week, then.
Carlos Alberto Cortez 01:01:28 Sweet.
Jack Berg 01:01:30 Take care, everyone. Bye.
unknown 01:01:31 A…
