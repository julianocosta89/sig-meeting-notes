SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-08-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:04 Hello, everybody. How are you?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:50 Who's leading this meeting today?
You know, David?
**David Ashpole (Google LLC)** 04:56 I don't…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:59 I'll check it out.
**Liudmila Molkova** 05:04 I think it's Carl's turn.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:08 He's got an item on the agenda, so I assume he'll come.
**David Ashpole (Google LLC)** 05:12 Yep.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:18 Oh, there he is.
**Carlos Alberto Cortez** 05:19 Hey, hey, sorry, yeah, it's like, last minute emergency, let's wait 30 seconds for one minute max, and we can start the call, sorry for that.
Okay, let's start, if that makes sense. Yeah, thank you for… let me share my camera.
I will share the screen, my screen as well. But yeah, there are a few things we have to, discussing the agenda. In the meantime, please feel free to ask.
Other stuff.
Oh, that's funny. Anyway… There we are. Perfect. Okay, yeah, thank you so much for joining. Sorry for the delay. Let's go with the first item. Jack, 10 minutes, yeah.
How to denote unstable properties and types in declarative config.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:22 Yeah, okay, so there is no config SIG anymore. That got, collapsed into the spec SIG, and… and here we are. So that… that's why I'm bringing this topic here. So, Declarative config defines the schema using this JSON schema.
And, you know, we have stable types, and types that are, you know, of other varying levels of maturity. For now, we actually… there's only… the only other stability level besides stable is development, but, you know, we reserve their ability to have alpha and beta as well.
And the way that we denote when a property or type is stable or not is, is in two ways, and one of them is with suffixes. So, if you're… if a property references a… at the point where a property starts referencing an unstable or experimental type, we include the slash development suffix there, and you know, that you see on the screen here. So, you know, in this little snippet here, we're saying how you reference that you want to use the Prometheus exporter. The Prometheus exporter type is in development because this spec for the Prometheus exporter is in development. So, you know, we can't have it be stable until the spec stabilizes as well.
And, you know, the other way besides these suffixes, and this is something that is not user-facing, is in the schema itself, types have names, so there's, you know, these types correspond to, like, the classes or structs that are generated from the JSON schema in code, and the types have.
you know, prefixes, actually, that denote their stability level. So, if the type is called the Prometheus Exporter, you know, it has an experimental prefix, so it's actually called, like, experimental Prometheus Exporter, or something to that effect.
And, you know, this issue, that Diego opened is about, like, hey, this is, this is mixing concerns. Like, having these suffixes, that denote stability is sort of like, you know, coupling concerns of, like, the names of properties with their stability. And, and there ought to be a better way to do this. Like, you know, think if you were… if you were designing, like, an API in a programming language, like, some languages have annotations or other ways to demarcate which APIs are stable versus experimental, so something like that, where it's, like, the name of the API is what it's going to be, but there's some other metadata that, like, that captures its stability level.
And so, you know, the reason that this is important is because If you can imagine what the user experience is like, for a second, when a property like this Prometheus exporter goes stable, like, you know, their… one day, their YAML will look like what you see here on the screen, and the next day, for the next version, the expectation would be that the suffix is gone.
And if a language implementation of declarative config hasn't jumped through a bunch of extra hoops to be able to recognize the Prometheus exporter, whether it has that suffix or does not, then, you know, it'll… the promotion from experimental to stable is a breaking change for the user.
Right? So, in Java, we get around this, you know, we hand-roll our code, which generates our data model from the JSON schema. And there's a bunch of, like, logic in there that is smart, and, you know, is able to recognize a property like Prometheus.
whether it has this development suffix or not. But it's… this is a very non-standard thing. There's nothing in JSON schema or the off-the-shelf code-generating tools that will do this for you. So you sort of have to commit to having, to having, like, hand-rolling your JSON schema generation code if you… if you want to facilitate this and have a good user experience. So that's sort of the conundrum here.
The other option, besides, like, having this kind of suffix approach, and that, you know, just to linger on the suffix approach, the advantage is that it forces the user to be aware of when they're using an experimental property. There's no mistaking it at all. You have to explicitly include slash development in your YAML, and there's no mistaking that you're sort of opting into an experimental feature.
And, you know, experimental semantics, like, which means we can make breaking changes.
From version to version, or minor version to minor version.
The other option, if you sort of take these suffixes away, is some other way to denote the stability level. And, you know, the most obvious thing is to encode the stability of a property in something like the JSON schema description keyword, in some sort of… using some sort of convention. There is no keyword in JSON schema that we could leverage, like, off the shelf, that is going to be able to convey this. We would have to either invent our own keyword, which is problematic, or we would have to, like, embed the stability information in, like, sort of a… in convention in plain text in the description field.
So, this is sort of the conundrum here, is that, like, you know, if you… encode this information elsewhere, like the description, it becomes very easy for the user to misunderstand the stability level of the thing that they're dealing with. Like, you know, and that's how you get angry mobs and blog posts that rage against OpenTelemetry as a project, is you, like.
have people think that they're using stable stuff, and then you make breaking changes to that stuff, because it actually was experimental, and you just didn't read the fine print. So, you know, that's what I'm trying to avoid here. So, I guess that's the… that's the introduction, it's done. David.
**David Ashpole (Google LLC)** 12:40 Yeah, so, like… Kubernetes obviously has, like, a similar problem, right? They have… Their objects, and they're versioned, and the way that they solve it is actually to put, like.
A suffix on the file format, so you'll have you know, your V1… alpha 1 instead of just your V1, and those could actually be different, right? So we… you could have… two JSON schemas.
One which is the… One that's got all the stable stuff in it, and another that has… everything, including the experimental in it. And you would say, like, my file format is 1.1 versus my file format is 1.1 slash Experimental, or something.
And if you tried to use the stable file format and throw an unstable field in, you would get, like, a not found error, or… you know, this is… we could even be nicer. So that's maybe one… one alternative we could consider.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:40 Right, and so that, I think, is a variation of this bullet point that I put here, option 3, that I didn't talk about, because I actually just sort of thought of it off the cuff, and maybe I thought of it before, but it wasn't on the top of my mind. But yeah, so essentially some way, top-level way, of a user demarcating that they're interested in using experimental features, not at the property level, but at the top level. So, file format is just, like, a way of how you demarcate that.
**Trask Stalnaker (Microsoft Corporation)** 14:11 So, I'm just thinking from an instrumentation perspective.
Where… because we don't have… I mean, that works great for the SDK schema, since that's hard-coded. That is… we have JSON schema for that, but for instrumentations, where… It's more flexible, and we just… it's kind of by convention.
We have instrumentation-specific configuration properties under the instrumentation node.
And… There's no real JSON schema, there's no real file format version for those.
Would we… I mean, we could still say, well, you can only use slash experimental attributes if you've opted in at this global level to experimental.
**Liudmila Molkova** 15:09 Maybe there should be a file… not a file format, but the JSON schema that describes the… Instrumentation config for this section.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:26 This is, just… icon.
**Trask Stalnaker (Microsoft Corporation)** 15:29 Federated configuration.
**David Ashpole (Google LLC)** 15:35 I mean, I guess there's kind of, like, an implicit JSON schema already, it's just we don't… have it as JSON schema, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:43 Yeah, I call this schema on read. The schema isn't actually written down, you know, in JSON schema format anywhere, but the instrumentation library, it's introspecting on, you know, its configuration node. It's, like, confirming that any required properties are there, you know, when they're, You know, when the property is present, that the values match the semantics, that they're the right types, you know, strings versus integers versus, you know, floating point, whatever.
And I think that's a very convenient way to, like, integrate with declarative config for, like, a random instrumentation library, is sort of like this lightweight schema on read.
**Carlos Alberto Cortez** 16:29 Diego.
You're muted.
Still no.
**David Ashpole (Google LLC)** 17:03 I don't want to get too far ahead.
Maybe I'll say something while we're waiting for him to figure that out, is that okay?
**Carlos Alberto Cortez** 17:10 Yes, I think that's good.
**David Ashpole (Google LLC)** 17:12 I don't want to get too far ahead, but have we thought at all about.
**Diego Hurtado (Dash0)** 17:15 Can you hear me now?
**David Ashpole (Google LLC)** 17:16 version, revving… oh, there you go. Okay, never mind.
**Carlos Alberto Cortez** 17:20 Just don't forget… just don't forget what you were… you were going to say, David. Okay, Diego.
Again, you're gone again.
Okay, we will wait for you. David, please, now, yeah, before you forget, and once you're done, hopefully Dyla will be back. Yeah, please go.
**David Ashpole (Google LLC)** 17:50 I was just gonna ask if we've thought about Major version revving for instrumentation, and how that would work with, like, the overall file format version. Like, I don't know if each… Like, if each… Plugin piece needs to have its own version, slash experimental opt-in, or… Like, I don't want to open too many cans of worms either.
**Diego Hurtado (Dash0)** 18:14 Can you hear me now?
**David Ashpole (Google LLC)** 18:16 There we go. Yep, you're back.
**Diego Hurtado (Dash0)** 18:18 Alright. Just, just…
**Trask Stalnaker (Microsoft Corporation)** 18:18 Just to answer David's, question, at least from the Java instrumentation, we are… we're doing what Jack described of schema on read, but we are… Applying the same stability requirements to that, meaning that, we do have to… we don't introduce any breaking changes to non-experimental properties, without a major version of them.
to the instrumentation.
**David Ashpole (Google LLC)** 18:51 To the instrumentation, or to the whole file format.
**Trask Stalnaker (Microsoft Corporation)** 18:55 To the instrumentation, which gets back to each instrumentation has its own implicit schema.
**David Ashpole (Google LLC)** 19:03 Yeah, yeah.
But we just don't expect users to write that out.
Which I think is fine, until somebody.
**Trask Stalnaker (Microsoft Corporation)** 19:10 To write what out.
**David Ashpole (Google LLC)** 19:11 Beautiful.
like, You're not gonna… we're not… if you have an instrumentation, you don't say, like.
I would… this is… This is, schema version 2.0.
Inside the instrumentation.
block.
Of the declarative config.
**Trask Stalnaker (Microsoft Corporation)** 19:30 I guess for what we're doing, at least in Java, is it correlates to the… the version of the instrumentation.
that we publish.
There's just kind of a natural linking there. I don't think we need to necessarily have an independent Schema version number from the instrumentation version number.
**David Ashpole (Google LLC)** 19:54 It makes sense.
**Diego Hurtado (Dash0)** 19:56 There is a… Yes, I… you can't hear me now, right?
**Trask Stalnaker (Microsoft Corporation)** 20:02 Yeah.
**Diego Hurtado (Dash0)** 20:02 Great, yeah. Okay, there is, option 4 and option 5.
The… another option is to have a completely separate file.
That is, for the schema that's named… let's say we have a file names table and a file name development, and there you introduce the… The changes that are… being developed.
another… option that I think it's even better is to have a separate Git branch.
So that you make, you have a branch that is stable, and you make stable releases from there, and you can make also experimental releases from your other branch. So when a, the person knows they are getting, an OpenTelemetry component that has experimental features when they install the package, and the package is named let's say OpenTelemetry, Python SDK experimental, right? So that's how… that's how they know. This is, actually.
Convenient, because you can also keep documentation separate.
So, in the stable branch.
You only document things that are stable, and in the experimental branch, you can include documentation for things that are unstable, so you don't mix them up.
So, yeah.
I also think this discussion of stability is something that concerns the entire project.
Because, I have seen that every… small… every sub-project, every little project in OpenTelemetry is handling stability in the same way. Sorry, in their own particular way, right? There is no consensus regarding how we handle stability, so… Reaching a consensus on how we do this.
It's important, I mean, it's not only about fixing this particular situation here.
**Carlos Alberto Cortez** 22:17 By the way, we are almost on time. Well, actually, we're on time, because it was supposed to be 10 minutes. We can spend some more time, if somebody else has something to say.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:30 Diego, I think, what I would say to your options 4 and 5… is, okay, a completely separate file containing alternative values. So you're talking about a JSON schema, like, file that we publish? So, there's two schema files, one for stable, one for stable plus experimental?
**Diego Hurtado (Dash0)** 22:48 Yeah, exactly.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:49 Right, so, like, that requires that the user somehow demarcate, you know, which properties they want to use, which of those schemas they want to use, which I think is actually option option 3, like, or a version of that, right? So, like, the file format is, like, a natural candidate for how you select which version of the schema you want to use.
You know, as David said, like, you know, using the Kubernetes analogy, you know, you opt in to the usage of experimental features with some sort of suffix or something like that.
So, I, I think that actually is a version of… of option 3. And then, like, maintain a branch. So… Whatever we do.
I think we need it to… I think we need to force users to be aware that they're opting into experimental features, right? We don't want them to be under the impression that they're using stable things and then get rug-pulled when we break those things. And so, like, maybe I don't fully understand, like, the proposal in option 5, but anything that requires you to go look up the JSON schema.
to go look up the documentation, I think fails to meet that criteria, right? So it has to be encoded in the YAML somehow, so that the user has no excuse for not being aware of it.
**Diego Hurtado (Dash0)** 24:09 Okay, let's discuss that in the issue, because we are on time now.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:16 Okay.
**Diego Hurtado (Dash0)** 24:17 Okay, thank you.
**Carlos Alberto Cortez** 24:20 Okay, yeah, probably we'll have to… anyway, we can discuss a lot of stuff offline. Let's, come back to other things.
Digital Trask.
Please.
**Trask Stalnaker (Microsoft Corporation)** 24:33 Yeah, thanks. This is just, to, ask folks who have seen the, for Maintainers, I have, I've been babysitting a couple of.
bots to roll out, Zizmor and, an improved, scorecard to all the repos as part of SIG security. And thanks to everybody who's, merged those already.
And, they're both… at, like, I think, like, 60% rolled out across all the repos. So there's, there's about half of them have PR, the remaining ones have PRs open in the repos, and half of them, I haven't opened the PRs yet.
So just, if you see those, please, take a look. If there's… if there's a problem with them or any confusion, feel free to ping me, tag me, or DM me.
And that's all.
**Carlos Alberto Cortez** 25:43 No comments there.
Okay, yeah, no comments there. Thank you so much for that, yeah.
Okay, so if that's the case, I have two topics that I want to discuss. Probably we can start with the last one. The previous one is just mostly, like, kind of, kind of brainstorming, so we're gonna start with the last one, if that makes sense. There's a PR. Do we have Michele here?
But basically, this is, something that we discussed in, like, last week in an issue, and this is a PR. But basically, it could be allowing SDKs to expand how service name is, detected, you know?
And we need more reviews. As I said before, there was discussion, at least initial discussion last week on this one, and Jack already, approved that, and Cijo provided some reviews. And just to be clear… oh, never mind, sorry.
There was some clarification here from Michele, which I think it's important for people to understand.
That these changes are about service detector, you know? It doesn't matter whether it's triggered by declarative configuration or use, you know.
in the actual SDK.
Yeah.
Do we have Cijo here, by the way?
I think she was here to me.
**Cijo Thomas (Microsoft Corporation)** 26:59 I'm here. Yep, yep, I'm here, Carlos, yeah. I only had, like, one major comment, which is, if this is about changing the entire SDK's default, that might be considered breaking, because we have a normative wording that says, must start with unknown service, if not provider.
if we are proposing to change that, then that needs to be a completely different discussion, because that is changing a stable behavior. I think I left that comment in the issue, not in the PR itself, so if you can… opened the issue, I think that was a comment I left towards the end.
**Michele Mancioppi (Dash0 Inc.)** 27:33 I mean, as far as I know, that part of the spec never made it too stable.
**Cijo Thomas (Microsoft Corporation)** 27:38 Oh, it is stable. The default behavior is stable from, like, 2021 onwards, so it was stable for quite a while. The section which was updated in the PR is… more like a named service detector section, which is not stable, so we are free to update that, but the SDK's default, is already, like, marked stable, like, quite some time ago.
**Michele Mancioppi (Dash0 Inc.)** 28:01 When you talk, and that is part… it's my fault for, not… I mean, I made a bit of a mess in some of the comments on the PR. The default resource, so the one that will set telemetry.tdk.something, that doesn't change. It is the service detector that I proposed can change.
**Cijo Thomas (Microsoft Corporation)** 28:19 Yeah, this… yeah, service name is also part of the default.
So if user does not do anything, we have a specification which says service.name must be set to process executable.
And if processor executable name is not found, it should start with unknown service. That wording is in the stable aspect of prospect.
**Michele Mancioppi (Dash0 Inc.)** 28:41 That is in the semantic conventions, if I recall correctly.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:43 They're intertwined with each other. The spec references, semantic conventions, semantic conventions references the spec.
**Cijo Thomas (Microsoft Corporation)** 28:50 Like, a lot of folks have hands up, so maybe, like, Jack, since you're already talking, you can continue.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:58 I don't want to jump the queue, Josh.
**Cijo Thomas (Microsoft Corporation)** 29:01 George Floyd.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:01 jump in here.
**Josh Suereth (Google LLC)** 29:02 Yeah, it's all good. Yeah, so… just to untangle this a bit, I hear what you're saying, Cijo, but, like, the way… the way I'm viewing this is we have a specification for the fallback for service name, because we needed it, particularly for Jaeger compatibility. It was, like, a mandatory thing. You had to have service name, so we had to have a fallback.
However, the new, like, we have bundled service detectors with names, Jack added that as part of config, it's awesome, it's a new section that's experimental that we can change, but the interaction between the fallback default and the service detector is actually not clear in the spec.
And my read on what I'm seeing is that we have room here to say, here's what that service detector is when it's configured and it's on by default. And yeah, it's experimental, but basically, if you disable the service name The service resource detector, you actually still need a service name for Jaeger compatibility, and the spec is not clear on whether or not service shows up.
Like, that's actually… like, you're walking into some… we're in some dangerous territory, the spec, but when we come down to it.
The thing I always want us to focus on is what is our goal with this discussion around compatibility and breakage and user expected behavior? And what do we want to give people, right?
In our experience so far using OpenTelemetry, every time unknown service is chosen.
which is what the spec recommends. It is a bad experience for users, every single time. It is poor.
And so, there's a piece of me that wants to be like, sure, that's what the stable part of the spec says, but let's consider that a bug, or something we can fix. There's also a piece of me that says, we're working on this new bundled resource detector, that's one of the things we want with entities, is to improve this whole ecosystem.
Let's take time to take the new part of the spec that's not stable and get it to a state where we're happy with it.
Right? And what it should be. But to some extent, the piece, you know, my two points are, one.
The thing that you're saying is stable, I actually consider kind of hugely problematic, like, almost a bug.
And most of the time that that occurs for users, it is a broken experience in hotel.
The second thing I want to call out is that I think, like, what Michele is doing here with this PR is this new portion of the spec, and the boundary that you're discussing is actually not clear.
when I read the spec and I think about it generically and try to interpret, like, how the one works with the other, I don't think we actually call out that the service detector and the you have to have a service name no matter what spec interact.
Directly. Like, I don't know if that's actually called out anywhere, and so I don't think that's actually resolved. So I still think we have time to resolve it.
Okay, those are my two points.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:44 Alright, let me jump in. So I think we can have our cake and eat it, too. We can get this mechanic that we want, which is, you know, for many, many cases, avoid unknown service showing up.
And without needing to modify, you know, this stable part of the spec. And that's because these named resource detectors They don't exist.
outside of declarative configuration. They didn't exist until I introduced them a couple of years ago, explicitly for declarative config. The names that exist there, they're written in the specs so that declarative config can use them in its schema.
And declarative config, the references to these resources detector names, it's opt-in.
Right? So they're not enabled by default. You have to write in your declarative config YAML that you want to use this service resource detector.
And so, I expect many people will do that. Everybody should do that. So, it should… it will become, like, effectively the default, but you'll still have to do it. And if you don't do that, you'll fall back to this default behavior.
Because that's what's built into the… that's what happens when you, you know, you get an SDK, or a resource from the SDK, and you haven't layered anything on top of it. That's where you get the unknown service. So, yeah, I think we're good here. Like, these re… we've just got to keep in mind that these resource detectors, they… they did not exist before declarative config. We don't need to worry about, you know, breaking changes to them, because they're experimental.
And they're opt-in, and they're for declarative config, which is all net new.
**Cijo Thomas (Microsoft Corporation)** 33:20 Yeah, that part is totally fine, Jack. I think I left a comment. If we're only changing that aspect of the spec, then we are totally fine. My only concern was we were potentially trying to break something which we ourselves declared, like, stable.
**Carlos Alberto Cortez** 33:36 And by the way, if I can add something, it's like, I really agree on that part with George, that I think it's not clear, and we can consider this a bug, you know, I think it's a bad experience, so I would support that, like, interpretation, let's say.
**Cijo Thomas (Microsoft Corporation)** 33:50 But based on what Jack described, we don't need to touch the existing part. We will only be affecting those users who use declarative config and declares they have a service detector, which is not really the default default, because someone has to opt into declarative config itself, so it's not really, like, default.
**Carlos Alberto Cortez** 34:10 Yep.
**Michele Mancioppi (Dash0 Inc.)** 34:12 the, I am a bit undecided whether We would also need a companion PR.
For modifying the definition of service naming the semantic conventions, because right now, it says… It's either the value of that environment variable, which, by the way, it's wrong, because we implemented it differently. Every single SDK out there will either get the value of auto service name, or it will very happily take the value for service.name equals blah from auto resource attributes.
So, the semantic convention thing is already incomplete, and whether we should add some, the possibility of mention there the custom behaviors that a service detector could have.
I think that if we merge this PR, then opening a second companion PR in the semantic conventions, what should be accurate in the description where service money comes from makes sense to me.
**Liudmila Molkova** 35:15 Did we have a conformance test for resource detectors?
It's actually would be really easy to do.
**Michele Mancioppi (Dash0 Inc.)** 35:30 You mean in, in, the, autosomatic conventions conformance?
**Liudmila Molkova** 35:36 Yeah.
Just start the service with a set of environment variables.
That's it. At the OpenTelemetry.
Compare the results.
**Michele Mancioppi (Dash0 Inc.)** 35:50 I'll, I'm typing in my to-do list.
**Liudmila Molkova** 35:54 Thank you.
**Carlos Alberto Cortez** 35:59 I think that's all on that front.
So, in that case, I think we can won.
Yeah, so I have the last item, by the way, and I just… I don't think we need that much time, it was mostly a question. In the Kotlin SIG, by the way, we were discussing, long story short.
the possibility to not have a global OpenTelemetry object with everything included. But among, like, the pros and the cons and all that, and by the way, this is something that I was asking Jack about, the global GET, and which is especially useful.
In the case of auto instrumentation, for example, you know, like, you need to expose when you are injecting the SDK, so the user and every, like, all the libraries can consume that. But if you're not using, like, auto-instrumentation, and the plan is not to expose something like this for Kotlin.
then it's not as useful. I mean, it's useful, but, you know, you can just get by without it. And I was wondering, because there's a specific line in the specification, which is this one, get global propagator.
And this method must exist for each supported propagator type. Propagator typing, in this case, only one, which is text map.
But anyway, so basically, it's like, we are forced to have that. And I was wondering whether people see this as something that… Has to remain.
you know, even Go has that, you know, for example. And I don't know whether, Jack, in case, you know, like, we were talking briefly about that, as I mentioned before, and yeah, I was wondering if you or anybody else has an opinion on this one.
As I said before, this is in case we don't want to expose a global OpenTelemetry object for now.
At all.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 37:50 Okay, so my read on what you're saying, Carlos, is, you know, we had this chat in Slack, and I was saying how, in Java, we sort of regret Different things that we've done with our global. And, you know, over time, we've sort of arrived at an opinion where, global is useful.
for instrumentations to access the instance of OpenTelemetry that was installed by the Java agent, so that, you know, you can access it in other instrumentation that is not the Java agent, and all the telemetry that's being recorded can flow through the same instance. But, like, outside of that use case, it's, like, we don't like the global.
in Mead and others. It's just been problem after problem. But the exception to this is propagation.
Right? And, you know, the idea being that, you know, client libraries and servers, regardless of whether they are being instrumented by OpenTelemetry, should still propagate context.
And so that's where, like, sort of the global propagator sort of stands maybe aside above from, you know, the need from a global for meter provider, a global for tracer provider, a global for logger provider. And so, like, what do we do about that? Like, should a language like Kotlin, which doesn't have sort of this auto-instrumentation requirement that I talked about, should it still have a global for the purposes of context propagation?
the… so, I guess… Well, the… Does anybody know of, like, a library, an instrumentation library.
let's say anywhere, within the OpenTelemetry umbrella, outside of the OpenTelemetry umbrella, that, like, you know, wants to participate in context propagation, but, like, doesn't want to participate in instrumentation otherwise. Because I think that's who we're trying to accommodate here.
**Michele Mancioppi (Dash0 Inc.)** 39:53 I have two. One is OBI that will go and read information about the trace context.
To be able to inject it in the logs.
the log collection, so that you can correlate, through trace context the log with the active span. And the second one is the ongoing work in profilers to expose the trace context, so that eBPF-based profilers can also annotate on the samples correctly the trace context.
When you say…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 40:26 How does the global interact there?
Because that's what this is about, like, should there… should there be a global propagator? Do you… should we have this normative must that requires global propagator?
**Michele Mancioppi (Dash0 Inc.)** 40:40 I'm a bit dodgy on the, on the details, but I am under the impression that if we do not have the global propagator.
Then, these two use cases would break.
But… Don't exactly quote me on that, I'm, like, 50%.
**Carlos Alberto Cortez** 41:04 Okay, I will follow up with you, Michele in case we can discuss details. Cijo?
**Cijo Thomas (Microsoft Corporation)** 41:09 Yeah, I'm wondering, like, what is the need why we are treating propagator as a separate thing than obtaining a global tracer or meter provider? Because those exist, so libraries can always get ahold of a provider, and from there, they can create tracer, meter, and all.
So that's already required for any instrumentation or any libraries to natively instrument with OpenTelemetry. They need a way to get a hold of the actual provider which the user has set. And similarly, they'll need a way to get a hold of the propagator. So what is the reason why we are specifically discussing the global nature of propagators?
I think Jack mentioned something, but I didn't quite understand, like, why is Propagator different from providers?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 41:51 So, in Java, we regret the global. The global has caused more problems than it has solved.
And… and, like, so, Carlos is talking… is… is the… is the, you know, the liaison, the sponsor for this new Kotlin group, and I think is trying to give them guidance on, like, you know, what lessons they should, you know, learn or take from, you know, other language implementations, and is sort of thinking about global, and trying to maybe avoid some of the mistakes.
If they are missing.
**Cijo Thomas (Microsoft Corporation)** 42:20 Pretty… Yeah, but if there is an instrumentation library they want to participate in, like, both span creation and propagation.
they need a way to obtain the current pressure provider and the current propagator. So, without global, the only option is that EPA has to… the instrumentation has to expose some way to Accept both propagator and tracer provider.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 42:42 Yeah, and that's what we do in Java. That's what we recommend to everybody, is, like, just explicitly pass around an OpenTelemetry instance, which is a wrapper around propagator, tracer provider, meter provider, logger provider. And, you know, so, you know, what the global accommodates then, you know, if… if you follow my point of view on that, is, like, the global accommodates libraries that, you know, want to participate in context propagation, but not instrumentation otherwise.
Like, that's the… that's the set of users that it's… it's… it's trying to exist for.
**Carlos Alberto Cortez** 43:15 Yeah, sorry, sorry to interject, but yeah, that's exactly what Kotlin wants to do, like, you require every implementation piece to require an OpenTelemetry object, but not a global object, and then it would have propagators and all this stuff.
**Cijo Thomas (Microsoft Corporation)** 43:30 And those libraries have only interest in doing the propagation aspects, but not creating in span or things.
**Carlos Alberto Cortez** 43:38 We don't know. The idea, in general now is, like, we would actually have a global OpenTelemet… sorry, a specific OpenTelemetry object that is not global, and is specified there, and then they can decide to do whatever they want.
But in this case, like, I could say the problem is that there's this specific line about propagators. As Jack said, I think that, because, like, in the case there are libraries or custom code that may… want to do propagation even without doing, like, creating spams, like, and thus relying on Tracer Provider, for example.
**Cijo Thomas (Microsoft Corporation)** 44:13 Yeah, yeah, but for other spaces, other areas in the spec, we do have similar normative requirement.
But it says should. We do have wording which says there exists… there should be a global way to obtain tracer provider. It was not a must, but it's not very unique to propagators.
**Carlos Alberto Cortez** 44:30 Yeah, exactly.
**Josh Suereth (Google LLC)** 44:33 Just to jump in quickly, like, one of the things I want to re-emphasize on what Jack was saying, they regret it in Java, but I think the reality is, we're growing up as OpenTelemetry.
when we started this notion that there is one SDK per process, and there is one definition of things per process, and there is, like, one way to do everything observability.
One of the things that we're definitely feeling is, like, multi-tenancy is a problem. You can see there's an OTEP about that specifically. The notion that you'd have the same propagation model for all of your edges might not be true as well. And so, I feel like some of this is us growing up.
as a project, as a system, and I… you know, Global has a use case, which is a simplified use case of, I have one process, I have one system, I have one way of doing everything.
We have found that that's not necessarily true, and as a default, like, I would almost argue at this point we should extract the global thing as a separate library you can opt into.
of, if I want to live in that world, I can use this global API that's way easier and simpler for me, but the core is the system that can work for more things, right? But I want to back up Jack here, where I think, you know, the recommendation I would give is not to provide Global by default, but assume you're going to have multiple instances by default, and then global is an optimization or a simplification for some systems.
If they want it.
**Jason Plumb** 46:08 Yeah, I'll jump in. I wanted to respond to what Jack had put in chat, and basically what you just said as well. I mean, I think… Well, we have an API, and what we're looking to do is to… we're combing through all of the details of that API, And trying to find where there might be gaps with the spec, before marking stuff as stable, before marking certain components. In this particular case, propagators being one that we stumbled upon, because if you read the spec, we hit that little bit about there needs to be a global get for propagators, and we're like.
why? We don't… no one wants that, and so that's how we ended up here, but I agree with the, the approach of, like, can we start with the simpler thing and not have the global, and then add it later if we'd like to? Yeah, as long as we're allowed to declare it stable, like, API stable without that, because the spec… does… require it, right? Yeah, there's the text that just got pasted.
Yeah, I'm sorry.
What are you too, Joe.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 47:02 Jason, just to reply to you briefly, so, I think it's allowed to relax normative language. So, you know, whereas the spec today requires this global propagator, if we, you know, the consensus here, it seems like it's emerging, that, like, hey, maybe this isn't the right thing for all cases. Like, I think it would be within our power to, you know, relax that to a should.
**Jason Plumb** 47:24 Great.
Cool, thank you, love it.
Cijo.
Alright, Carlos, do we get the answer you were looking for? I think we did.
**Carlos Alberto Cortez** 47:43 I think we did, yes. At least we have a good start, that it's enough to get us working. Okay, thank you so much for that, yeah, really appreciate it.
Yeah. Okay, we have nothing else in the agenda. We still have 14 minutes, so if somebody wants to raise something… I know that these weeks are kind of slow because it's summer, etc, but… If there's something… Oh, it's.
**Cijo Thomas (Microsoft Corporation)** 48:08 There is nothing I want to make a quick, talk, I mean, took attention to something. I don't have a way to share my screen, so… Carlos, can you open the message in the chat, which is referring to APR?
It's adding something to the spec for what I call as instrumentation library supplementary guidelines.
Yeah. So there is an open question. I think David has the only one responded before. So I'm trying to find, like, where to place this content. I don't think anyone, ever looked at the actual content except David.
But first question is, do we see this being in the specification, or should I place it somewhere else? I think David preferred it to be in a website.
Think, my opinion is that we put a lot of supplementary guidelines Targeting inducers in the specification for metrics, traces, and logs.
I'm kind of inclined to keep it in the spec itself, so I want to get some opinions from other spec people about What is the right home for it? That's the first question, and the actual content itself can be reviewed, once I know where to send the PR to. Is it a spec repo, or the website, or some other place?
I think there is a discussion which is open, between David and me, and yeah, I think just two of us who got engaged so far, so if anyone has opinion on where should this be placed, I can… take the next step, like, once I know, where people are preferring need to be.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 49:41 And, Cijo, I'm wondering what the best way is to advertise this to the folks in the community who write the most instrumentation.
**Cijo Thomas (Microsoft Corporation)** 49:52 I have mentioned, like, in this PR itself, somewhere I left a comment, which points to a draft PR in the website, where once this is merged in the spec, the website would be updated to point to this one, exactly the place where it says instrumentation, So whoever is writing or reading about instrumentation, they would be, getting a pointer to the supplementary guidelines, which itself would remain in the specification.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 50:17 I guess what I mean is, like, within each language ecosystem, there's, like, there's some folks that maybe tend more towards SDK development, and some folks that may tend more towards instrumentation, and there's, of course.
**Cijo Thomas (Microsoft Corporation)** 50:29 overlap.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 50:29 between them. But, like, from a spec PR standpoint, the folks whose feedback you're interested in are the folks who have written a lot of instrumentation within the OpenTelemetry umbrella, and Yeah, I don't know, so that'd be, like, the contrib maintainers for some languages, instrumentation Maintainers for other languages that maintain dedicated instrumentations.
But yeah, like, if you're looking for eyes and checkboxes, you know, maybe you could gather up a list of those folks or those teams and tag them explicitly.
**Cijo Thomas (Microsoft Corporation)** 51:02 But that would be to get feedback on the content itself, or do you expect them to be the right people to ask for where do We place the content itself.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 51:13 That would be on the content itself, not on the placement.
**Cijo Thomas (Microsoft Corporation)** 51:17 Yeah, so my first question is to figure out where the, like, placement should be. Is it on the spec repo or I.O?
And once that part is sold, then I would, yeah, really reach out to the people who are mostly focused on writing instrumentations.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 51:30 Okay, then I'll take a look at this from a placement standpoint. I'm not sure I can offer a ton of feedback on the actual content, but yeah, I'll take a look.
**Cijo Thomas (Microsoft Corporation)** 51:40 Yeah, thank you. And it's also mostly reverse extracted from existing guidelines, which are spread throughout multiple languages, including some of them which I myself wrote, like, long ago in .NET contribute.
So, to your point, like, yeah, I think I should get more feedback from… the contribute Maintainers on the content itself, so once… I'll wait for some spec blessing.
And then I'll reach out to more folks for the content itself.
Yeah, thanks, we can move to the next one. Thanks, Carlos.
**Carlos Alberto Cortez** 52:11 Thank you so much.
**Jason Plumb** 52:12 I'll go fast, I think it's pretty quick. There is discussion among the client SIG folks that meet every two weeks. There's kind of two parallel things happening there. One is that we're… I think there's an issue that's open about creating a new repository for federated semantic conventions for client stuff. That's… that's fine, that's kicked off.
There's another question that came up.
Around the long-standing issue of session being ill-defined, and… A few of us agree that it's long overdue that we just create a working group or a SIG for this specific topic. We get the language defined in the spec about what it is and how it's treated and all of those important things.
that we've been kicking that can down the road for years on, and how it relates to entities. But no one was sure whether or not we still call them SIGs if they're intended to be short-lived. Like, if we put a 6-month timeline on this group. Do we still call it a SIG? Do we call it a working group? And can anyone point me to the… are there guidelines for bootstrapping a new short-lived SIG?
I'm sure there are. I don't know where to look for now.
**Carlos Alberto Cortez** 53:19 If there is, they should be in the community repo.
**Jason Plumb** 53:23 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 53:24 Yeah, I could take that. The… we have officially, sunset the working group term, and just call everything SIGS.
**Jason Plumb** 53:36 Okay, good.
**Trask Stalnaker (Microsoft Corporation)** 53:37 And… because it's just too confusing.
And the way… yeah, it's fine, and expected. It's great to have, you know, 6-month SIGs. it follows the community project proposal.
So it's… just go and, open a PR… For one of those, to propose a community project for it.
**Jason Plumb** 54:05 Cool. Yeah, I mean, I think, like everyone, we're a little strapped on resources for that, but we really want to do it, so… I think it's long overdue.
Thanks.
**Carlos Alberto Cortez** 54:19 Thank you so much for that. Yeah, we have… that's all in the agenda.
And probably 8 minutes is not enough to discuss anything big.
So, calling it once… Calling it twice.
Okay, thank you so much.
See you offline.
Cio.
**Trask Stalnaker (Microsoft Corporation)** 54:38 Bye.
