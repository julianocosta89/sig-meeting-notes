SIG: Semantic Conventions SIG
Date: 2026-10-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Jack Berg (Raintank, Inc. – Grafana Labs) 00:01:14 What's up, David? How are things?
David Ashpole (Google LLC) 00:01:17 Is that good? Very good.
Talking with Dylan last week, who sits next to me.
About… log levels and opt-in, opt-out, opt-out, and so I'm hoping to… Raise that here.
Chat about it.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:01:43 Yeah, yeah, I think I saw something about that, the idea of bringing, like, advice to the other signals, essentially.
Something akin to that, where… you know.
Or just… I think that's… that's my read of… Of what's going on. So bring the opt-in, opt-out nature of metrics to logs.
David Ashpole (Google LLC) 00:02:04 Mmm.
Well, it hasn't arrived at metrics yet, so… We'll have to get there first, maybe, but, Yeah, I actually… I mean, I'll save it for the… Yeah. But I actually… Would rather we just stuck with logging levels for logs, because it already exists.
I think spans is the most interesting one.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:02:32 Yeah, there's no… There's no advice, and there's no pre-existing severity.
field.
David Ashpole (Google LLC) 00:02:44 Yep.
Trask Stalnaker (Microsoft Corporation) 00:03:07 Ayy.
David Ashpole (Google LLC) 00:03:13 interest.
Trask Stalnaker (Microsoft Corporation) 00:03:24 We can probably get started.
Hoping a couple more folks join for… Jack's topic… Let's see, is Sven is not… Here, general guidance on recommended versus opt-in.
Opt in… yes, in case you're listening to this recording, Sven.
But recommended, we don't generally ask for an opt-out.
Anyway, we can… maybe Sven will show up later.
Lewis, hey, welcome back.
Lewis Lewis 00:04:31 Inc.
I'm back, talk- still talking about this. About 2 weeks ago, I came by to say.
Hey, there's an instance ID that's… used for Azure metrics exported by Azure.
received in OTEL, among other places, and the value to match them to the resource is not currently in Semantic Conventions. Could we add it? There was a discussion, I think it's captured in a comment at the bottom of the issue.
And I guess I just wanted to check in on this.
And see if it could get traged somewhere.
Trask Stalnaker (Microsoft Corporation) 00:05:10 Oh, you got a lot of clothes.
Lewis Lewis 00:05:12 Automatic closed, if it's not.
Trask Stalnaker (Microsoft Corporation) 00:05:15 Yeah, yeah, we can fix that.
Sucked… I mean… And reopened…
Lewis Lewis 00:05:36 Do I need to do that? I can do that.
Trask Stalnaker (Microsoft Corporation) 00:05:38 No, no, no, I got it. Alright, cool. Yeah.
App service plan instance…
Lewis Lewis 00:05:45 There was a couple options, if people want to talk about it more.
Trask Stalnaker (Microsoft Corporation) 00:05:49 Are those laid out here, or in.
Lewis Lewis 00:05:52 They are laid out in the issue in the comment.
And if there's a session, I can edit them in appropriately. I think that this argument was the one I thought with clearest.
Trask Stalnaker (Microsoft Corporation) 00:06:05 And this matched the… I think this matched the GCP, had an instance name.
Lewis Lewis 00:06:11 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:06:12 Okay.
Cool.
Yeah, yeah, awesome. So, yeah, you can go ahead and mark it ready for review when… oh, I can approve that. I wonder why… Feel like you've sent… PRs before, it's supposed to recognize you and… Then… run CI. You're not a… no longer a threat actor.
Okay, cool.
Alright.
Lewis Lewis 00:06:48 Anything else I should do there? Or we'll just do it in VR?
Trask Stalnaker (Microsoft Corporation) 00:06:52 Yeah, yeah, just mark it ready for review, make sure that it is, in that state of waiting on reviewers.
And then, yeah, you might need to bug us.
Since it's not in a, since it's outside of an active SIG.
Lewis Lewis 00:07:09 I can continue to do that. Thank you.
Trask Stalnaker (Microsoft Corporation) 00:07:19 Cool, jack.
Thanks for… Bringing this topic…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:07:27 Yeah, so… I opened this PR a while ago, and then it auto-closed, and I think a lot of us are busy and doing a lot of different things, and this is kind of like a… like a big project, or… and so it's easy to just… not want to spend the time to review it. But I do think, like, the notion here, the proposal is… we gotta make progress on it somehow. I think Semantic Conventions needs to own the definition of the configuration schema for instrumentation, and that's ultimately what I'm trying to get towards, is, like, how do we decentralize or federate the open telemetry configuration JSON schema so that Semantic Conventions owns the bits that are relevant to it. And, so I… the PR that I opened a while ago, it's a lot to review, and I actually think it's, like, probably the bad way to… not the right way to talk about this, because, I think the PRs sort of fall out once you get a conceptual agreement.
And so, I want to talk about, like, the concepts right now.
And what I propose, you know, the first thing is, you know, just, you know, restating what I just said, is that Semantic Conventions owns the definition, the type definition for this JSON path, instrumentation development general.
and, you know, the way that I would… I imagine this working out in practice is, I delete the type… or we delete the type definition from OpenTelemetry configuration and update the description of that, that properties to say, like, hey, this type is owned by Semantic Conventions, and if there's, like, a well-known place where the schema is, you know, maintained as part of the Semantic Conventions repo, then the description can contain, like, a reference to that. But it needs to be, like, essentially, like, a floating reference, because the version schemes are going to be, like, published differently. Semantic Conventions has its, like, you know, versioning cadence and scheme, and, you know, same with declarative configuration, and so they need to be, like, decoupled from each other fully.
I think. And… you know, Ludmila, I think you showed in one of your… in your comment where you sort of sketched and iterated on what I was doing on how some code generation could work relative to this, and I think that, to me, was, like, the strongest signal that the versions need to be disjoint from each other, because whoever's doing that code generation, like Semantic Conventions Java, that's, like, publishing the the generated code that interprets the schema and, you know, extracts out configuration values and applies them to instrumentation, that is version… that's like following the Semantic Conventions version schema.
not the declarative config schema. And so, you know, that… You wouldn't want that type of component, taking a dependency on declarative configuration, and it's like, It's schema version.
Liudmila Molkova 00:10:39 Yeah, one… there is this thing I don't understand about declarative config, and maybe you can help me. So, there is… there wouldn't be one single version of Semantic Conventions, because the GenAI would be a different version, client would be a different one.
And, we won't be able to have Well, unless we put a lot of effort into it. A single place where we have the full instrumentation schema defined.
And we… in some cases, it won't be our towel.
is… is it… does it have to be typed? Like, can instrumentation think about it as something untyped and never care about, the full schema?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:11:21 That's a good question, and yeah, Trask and I were just talking about this type of thing the other day, you know, we're trying to federate declarative configuration into semantic conventions, and Semantic Conventions itself is federated. And I guess, like, a counter question to you.
Since Semantic Conventions itself is federated, what is the… what's the recommendation for projects like Semantic Conventions Java, which want to publish, you know, generated constants, generated code related to Semantic Conventions, when that's federated?
Liudmila Molkova 00:11:55 So we had these discussions in Gen AI SIG, where we are questioning whether we want to generate, GenAI conventions into existing artifacts, or new artifacts.
And I don't believe we have a consensus yet. It depends on the language. So, for example, JavaScript would want them inside the existing library, if I remember correctly. In Python, we probably don't want them in the common one.
And we would generate them as internals into a helper library that exposes the higher-level API publicly, rather than low-level Things.
At least some of them.
And… It… it seems like both models can be possible, because… some… Third party.
thing can publish their own semantic convention.
library, and do we… Care about single motto.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:13:04 I don't think I care about single… like, so, in my head, the way that this, like, Semantic Conventions is federated, therefore Semantic Convention Config is federated as well. So, I was kind of assuming that we'd have to, you know, solve that type of problem.
And, so… You know, just like… OpenTelemetry configuration has this sort of floating reference to the semantic invention schema.
I think that Semantic Conventions, where if it publishes a JSON schema for its, you know, the general type, I think that would contain properties with, like, floating references to the portions of semantic conventions which are federated out.
That's, like, the idea that was in my head. So if there's, like, the GenAI domain is maintained separately, then the instrumentation development.general.genai property would have, like, a description that, like, you know, refers to the GenAI config schema, which is maintained elsewhere.
Liudmila Molkova 00:14:08 Is it a requirement? Oh, go ahead.
Christophe Kamphaus 00:14:11 Yeah, this would work for everything under the hotel organization, but the federated part could also be Commercial registries that are private.
So it wouldn't work for that.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:14:25 Yeah, and the same thing is sort of even true within the OpenTelemetry organization, because, you know, there's individual language libraries that have their own config schemas, and, like, you know, if you kind of take that to its extreme, every single one of those could have its own config schema, which needs to be federated to.
That sort of seems, like, impractical to manage that type of coordination.
Trask Stalnaker (Microsoft Corporation) 00:14:51 Jack, wouldn't, you're talking about individual language library configurations?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:14:57 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:14:58 I was thinking those wouldn't be under… I was thinking general would be limited to, like, semantic conventions.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:15:07 Correct, correct. And so, but like, you know, the, you know, in theory, so you have, instrumentation development, Java, library. Each one of these libraries has its own schema, and, you know, we could federate those as well. It's like, it's not exactly an analog, but it's close.
Trask Stalnaker (Microsoft Corporation) 00:15:25 Yeah, yeah.
Yeah, but, like, to… Christophe's point, though, There's not really a… I don't think the configuration, Repo can point to one place where all of those things are going to be defined.
We don't have, like, a registry, we're not… The Semantic Convention core repo doesn't have, like, links out to other things.
So I think I… Hmm… to… I think Ludmila was saying, just… can it just be… untyped, sort of… And each domain can… Semantic Conventions should define these things.
And the configuration under a given domain.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:16:20 What?
Trask Stalnaker (Microsoft Corporation) 00:16:20 up.
to the consumer to pull in, I guess, the different pieces.
That they want.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:16:28 Well, that seems like… fine to me, and not too different than what ends up happening in practice if, like, you take Federation to its extreme. But, you know, aren't you… aren't you worried a bit? At least, like, I'll say it for myself. I'm worried a bit about the core, domains and the core config options You know, if we don't have a schema for them, that the, like, you know, all the different languages sort of have inconsistent interpretations of what that schema is that's, like.
you know, not strongly typed. It's just like, you know, a series of pros, and they need to infer a schema from pros in a doc somewhere.
Liudmila Molkova 00:17:09 Oh, I… I'm not suggesting this, I think we should define a schema, we should document it properly, we should… Probably link to, like, the central configuration repo would link to semantic conventions in some way, formal or informal.
and semantic Conventions would link to federated hotel places, but if I'm developing a custom instrumentation, I should be able to just invent some property names, like, you know, in spring properties.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:17:44 Oh, I see.
Yeah, yeah, no, I get what you're saying now. So it's like, you know, federate and have, like, you know, sort of references to these different sources or schemas where it makes sense, but don't try to have that, like, everywhere that you need config.
like, let there be sort of exceptions. And I agree with that 100%. Like, that's what we're doing in Java.
today, and I call this, like, schema on read. So, like, you're introspecting this, like, this node you have, like a YAML or JSON node, and you're trying to, like, read properties out of it, and, you know, you don't have a schema, except for, like, what's embedded, like, encoded in your source code itself.
And, you know, you're reading properties out, and they're present or not present, and, you know, they may or may not match your expected types.
And along the way, you're validating, and you're throwing exceptions if there's some sort of thing that doesn't compute.
And I think that's what you have to do.
And it's just, like, try to standardize where we can.
Liudmila Molkova 00:18:49 Yeah, I like this, and we kind of want within OpenTelemetry to have the hierarchy, the root passes specified for everything, that they don't conflict, they look consistent, and, things like this.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:19:10 Yeah, okay, so… how much time do you want to spend on this topic? Because there's other ones there, and, like, maybe we should try to wrap this up in, like, 5 minutes, just for the sake of other… Folks, or how do you feel?
Liudmila Molkova 00:19:23 R…
Trask Stalnaker (Microsoft Corporation) 00:19:24 Thank you.
Liudmila Molkova 00:19:24 Maybe we can't… Talk about the next steps?
And we can also get some time on the speckle, because it's across… Language and cross-cutting concern.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:19:38 Yeah, and let's pick the right time to go to the spec call, because, like, let's get consensus amongst us, like, first, and, like, I'm willing to keep coming to this meeting on a weekly basis, and just, like.
Until… until we need… until, I don't know, we don't need to anymore. But, yeah, so this is not, like, the last that I'm gonna show up and talk about this, so we don't need to rush.
And then, like, let's see, next steps. So, here's the rest of my proposal, just, like, briefly then. There's, you know.
There's some tooling in OpenTelemetry configuration that takes a YAML representation of a JSON schema, applies various sanity checks to it, and spits out a proper, like, JSON schema that is compliant with these other rules of thumb that we have that are a little bit stricter than normal JSON schema. And so, I would propose making those, like, verification and compilation scripts like, public, such that places like Semantic Conventions and the other Semantic Conventions repos can depend on them and ensure that the schemas that they publish are consistent with whatever norms we have in configuration.
That's one part of it. And then, Lududmila, in your, branch that you proposed, and this, this is a while back, so, if you don't remember it fully, that, that, that… I understand, but you proposed some good ideas about how to embed config into the Semantic Conventions model.
And, like, in my current iteration, I have, like, branches that, you know, represent this proposal of mine, but, like, I just go with all… everything that you said. Like, basically, I'm unopinionated about how Semantic Conventions wants to represent this information in its YAML data model. And, you know, just what we need to do, roughly, is, like, the Semantic Conventions YAML needs to encode this information somehow.
and it needs to compile to the OpenTelemetry Configuration version of YAML, and then, you know, we use the scripts that OpenTelemetry Configuration publishes to do verification and compilation to the final JSON schema format. So that's, like, roughly the shape.
It's, like, kind of a two-stage compilation process.
Liudmila Molkova 00:21:47 Yeah, and we would publish the results schema along with other schemas that we will publish.
And this would be the link you can embed in the configuration.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:22:01 Right, exactly.
Liudmila Molkova 00:22:04 Would we accumulate… okay, so maybe we should design it later, but, like, we can… like, I'm still thinking how we can accumulate different links from different places, but maybe it's the overall semantic convention schema that would take into account federated ones, but we'll decide.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:22:20 Yeah, that's… that's a kind of a question, like, I want to help think through it with you all, but also, like, I want to, like, you know, Federation delegation, I want you all to kind of, you know, own your own destiny there with how you want to represent other Semantic Convention repos, sort of, being referenced or, you know.
Whatever. So, yeah.
Trask Stalnaker (Microsoft Corporation) 00:22:42 My initial thought is that it would be, like, that we could just match the way that the schema registries work, where… the consumers are responsible for… I mean, you pick the schema registries, and you pull all those together, and that's what gives you your full declaration for the general, for your particular use case.
Liudmila Molkova 00:23:15 In our case, schema registry is the schema URL, right, or the schema name.
Trask Stalnaker (Microsoft Corporation) 00:23:21 Yeah, so you would, you would list, kind of, all of the schema URLs, that you want.
And that would… and then there would be kind of the way that, don't we have that, like, an Uber, like, the… with this… the registry, it'll create a Uber registry with all of those things kind of all squashed together.
Which is then, like, the consumer's single registry.
Liudmila Molkova 00:23:55 Oh, I see. So consumer can declare all the dependencies, and it will include not just semantic conventions, but also the schemas from different places that they meet.
Trask Stalnaker (Microsoft Corporation) 00:24:05 That they want, yeah.
because, like, I'm thinking, like, Java instrumentation, you know, we would link to… we would pull in whichever ones we are… supporting… So, we would pull in Gen AI, but we wouldn't pull in, like, client-side or mainframe, necessarily.
And Jack, to the earlier, earlier discussion about, artifacts, like, one or multiple artifact… one artifact per schema registry, or an Uber artifact.
I like the… I think I like the idea for Java, at least for the separate artifact per… schema registry.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:25:06 I think so, too. And then, I think what we're kind of, sort of circling around is you need tooling to, sort of resolve an Uber artifact, an Uber schema that is, like, you know, the base semantic conventions plus whichever other ones you want to reference.
Trask Stalnaker (Microsoft Corporation) 00:25:24 Well, for the artifacts, at least, the constant… the artifacts, we can have… dependencies, I mean, because we have schema registries have versioned dependencies in them already, to which, like, core version, it has a transitive dependency on.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:25:44 Okay.
Trask Stalnaker (Microsoft Corporation) 00:25:45 So I think we could model the artifacts in that same way.
And then users would just pull in again, the artifacts that they use, and rely on Maven artifact, Maven, version alignment.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:26:01 Okay.
No, don'.
Liudmila Molkova 00:26:08 The last thing to throw in here, On the topic of whether configuration should only know about the core semantic convention. This is one option.
On the other option, configuration can know about the… federated ones, and the ID of the federated one is the part of the schema URL.
The unique one.
So you identify your path, your hierarchy by schema URL.
Without diversion.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:26:45 Yeah, yeah, I don't know, could you, like, maybe write it down? I'm not…
Liudmila Molkova 00:26:51 Yeah, yeah, so let's do, let's talk about it next time.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:26:54 Okay. Yeah, so… Let's see, what can I do for next time? I can sort of take these local branches that I have and try to Create some… some… some… like, a document or something that sort of brings all the current state of the conversation together, so that we can iterate on, like, the concepts in a central place, and then, you know.
once we… once we have consensus there, then, you know, I can open, serious attempts at PRs, and… and we can talk about it with the spec folks as well.
Liudmila Molkova 00:27:28 Awesome, and I'll refresh my prototype and try to build what we also talked about.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:27:35 Okay.
Thanks.
Liudmila Molkova 00:27:39 Thank you.
Trask Stalnaker (Microsoft Corporation) 00:27:43 Yeah, just for context for other folks, this is… this discussion is, kind of the key to unblocking and stabilizing instrumentation slash the instrumentation node for the declarative config.
Which… I am, at least in Java, very interested in stabilizing, because we're using it a lot.
We want to promote it more.
Cool, moving on, Oh, Martin, hey!
MK Martin Kuba 00:28:25 Hey, Trask.
So, I just wanted to, double-check a couple things. Like, in the client side… Sig we are looking to move or migrate a few namespaces from… from here to the client-side registry.
So I… we have this high-level, issue. If you scroll down a little bit, you'll see that there are, like, sub-issues, like, for each of the, namespaces that we want to… we're thinking about moving.
we're looking to do the first one, and I wanted to just double-check with you guys to see, like, if the process that we're thinking is the right one. Like, I saw some, maybe, precedent, like, with the mainframe, some of the mainframe.
Semantic Conventions, and if you go back up a little bit to the main description, so what we're thinking of, is… is, opening a PR here to add the exclusions, and then when a release happens here, then we would actually merge our… The namespace into our registry.
And then, after that, we would open, a second PR to deprecate the, The Semantic Conventions from here.
I think that's what Mainframe did, and I wanted to just double-check that that's the process you would recommend.
Liudmila Molkova 00:29:53 Yeah, so you would need to exclude, things in chorus Semantic Conventions so they don't So you can depend on Semantic Conventions directly.
And maybe it's not worth it to send two PRs to first to exclude and then to deprecate.
You can just deprecate, point to the new repo, and it won't… things would not immediately show up in the new repo.
But it's okay.
We want to release overnight.
We can wait, we can hold release until things… until you merge things into this repo.
MK Martin Kuba 00:30:35 Okay.
Okay, but we should, we should, wait for your release before we actually merge things in.
Liudmila Molkova 00:30:48 You don't need to. You can depend on a specific commit shot. So, like, technically, like, of course, for you to release, you should depend on the proper version of Semantic Conventions, but just to develop stuff, you can depend on a specific commit.
MK Martin Kuba 00:31:02 Okay.
Okay, yeah, that's… that sounds good.
Liudmila Molkova 00:31:10 Yeah, thank you.
MK Martin Kuba 00:31:12 Thank you.
Trask Stalnaker (Microsoft Corporation) 00:31:13 Alright.
Ludmila!
Let's see…
Liudmila Molkova 00:31:21 Maybe I would, maybe we can push this spot, this thing to the last one. I want… David is here, and it's related to configuration, and related to federated… well, not related to federated Semantic Conventions, but I think it's natural to talk about the David's topic, and there is also Christopher's topic in between.
Christophe Kamphaus 00:31:44 Yeah, mine is also very related to the federated SAMConf, and how it's displayed on the website.
So the question is, what should the structure be?
on, hotel.io.
So in the docs, we currently have the specs.
And there it's now just the core semantic conventions.
So the question is, how would we show the federated Conventions here?
In the issue, there were a few different proposals.
So, the first one was in the issue description.
And, No, below.
So here… where… The federated ones would be integrated.
Or, no, it would be all on the Semantic Conventions, but it would be different points.
The downside here would be that links would… Have to change, so any links that were… Saved would break.
The alternative would be to keep the current core sumconf where it is.
And, lists the other semantic conventions, like general AI, below it.
Or integrates them here in the core sumconf.
So that's the second proposal, where they would be side by side.
And in later discussions, The proposal came up.
to integrate federated conventions inside CE.
or docs.
And here, I'm a bit hesitant to go in that direction. Of course, it would be nice to have everything Together.
My fear is a bit, it might be confusing to users to know where A document came from, or where the registry came from.
So I wanted to ask your opinion on this.
Liudmila Molkova 00:34:15 So essentially, it's the flat structure versus things are nested under semantic conventions.
Christophe Kamphaus 00:34:23 Yeah.
Or merge all together into one.
Liudmila Molkova 00:34:30 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:34:32 Sounds like we're all kind of rejecting the third option.
Liudmila Molkova 00:34:37 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:34:39 Also, from a versioning perspective.
Liudmila Molkova 00:34:46 And I do…
Trask Stalnaker (Microsoft Corporation) 00:34:50 I think it's kind of good to promote this concept. We kind of want to promote the concept of federated semantic conventions.
And so, having it… Sort of almost front and center in the docs is a good thing.
But at either of these…
Christophe Kamphaus 00:35:10 Maybe take a look at my proposal.
I, I propose something in between.
Where we would keep the core semantic conventions.
Where they are today, so it's the one below.
And we would have federated semantic conventions below it, and there we could have whatever structure we want, and list any federated Conventions.
Liudmila Molkova 00:35:41 Would we want to list language-specific conventions there?
Probably under… corresponding languages.
And, like, from ownership model, Everything Java is owned by the… Java people.
Rather than there's pieces everywhere.
Trask Stalnaker (Microsoft Corporation) 00:36:11 I mean, if it's federated, If, when we federate the Java, then it would just naturally fall Here.
Liudmila Molkova 00:36:23 If I'm a reader.
if I'm looking for semantic conventions, Or Java.
It's subjective, but they would start in Java.
And there is an instrumentations there, and it's maybe even instrumentation-specific.
Very likely.
Trask Stalnaker (Microsoft Corporation) 00:36:48 instrumentation-specific… Oh, yes, yes, I understand what you're saying, yeah.
Liudmila Molkova 00:36:57 And maybe it's the… rather, the ecosystem explorer that would show it.
It'll be very… a lot of things if we want to show language-specific conventions.
Is it consequential, whatever we decide?
Christophe Kamphaus 00:37:17 I think C… Most consequential one would be if we wanted to merge some.
And maybe put a comment here that we don't want to go that way.
Liudmila Molkova 00:37:59 I think the first option that puts all conventions under semantic conventions is not right. So, like, this… this demonstrates it perfectly, that… oh, sorry, sorry, this one… Might be okay, because it… they are flat, but under semantic conventions.
The one that puts everything under specific… under Semantic Conventions, we… we want something?
Somewhere below. It's just not right.
Trask Stalnaker (Microsoft Corporation) 00:38:29 The merge… the merging option.
Oh, weird.
Liudmila Molkova 00:38:36 No, no, this one. Oh, sorry, can… No, not the merging, this one. So, you see here, the GenAI-specific version appears on.
Trask Stalnaker (Microsoft Corporation) 00:38:45 Oh, yes, yes.
Liudmila Molkova 00:38:46 Semantic Convention, and the direction is opposite, the GenAI depends on semantic conventions, and this creates an impression that it's the other way around.
Christophe Kamphaus 00:38:55 Yeah.
Liudmila Molkova 00:38:56 It's essentially the question of.
If we do the Uber registry of all semantic conventions across open telemetry, how we would organize it.
And, the specific ones would be leaf nodes. It would be flat, plus dependency.
Trask Stalnaker (Microsoft Corporation) 00:39:18 Where even is the merge? Was there no, example of the merge? That was just discuss… oh, merge.
Christophe Kamphaus 00:39:25 It was discussed, and that's why I wrote it there as an example to illustrate it.
And the second, part was where I came up with the… A flat 1, we see the core semantic conventions, and below we see federated Semantic Conventions.
Liudmila Molkova 00:39:46 Did this make sense, or the flat one?
To me.
Christophe Kamphaus 00:39:50 My preference would be that one.
Because it has the benefit of keeping the current one where it is, so all links would stay the same.
And we don't have the problems that… Every additional federated convention would increase the list of specs.
So, as they would be under federated Semantic Conventions, we could… Describe what those are.
So, yeah.
Liudmila Molkova 00:40:24 Anybody has objections to… That one, because I… I… I agree.
It looks the best.
Sorry, wait, Trask, this is… this one doesn't look good, or…
Trask Stalnaker (Microsoft Corporation) 00:40:39 I haven't copied the one that looks good yet.
Liudmila Molkova 00:40:41 -Oh, okay.
Trask Stalnaker (Microsoft Corporation) 00:40:43 Let's see… this… This one, like, okay, let's see, preview. Okay, we don't want to merge them.
this… Doesn't look right.
Because it's nested. This one looks good.
Liudmila Molkova 00:41:06 Yeah.
Maybe we should call it Other Semantic Conventions or something, but I'm pretty sure Patrice and other Otelier people will figure it out.
Trask Stalnaker (Microsoft Corporation) 00:41:17 Oh, and not sure about language.
Okay.
Is that, enough, Christophe, for…
Christophe Kamphaus 00:41:58 Yeah, I see.
Trask Stalnaker (Microsoft Corporation) 00:42:00 Awesome, thanks for helping them with that.
Christophe Kamphaus 00:42:03 Yo.
I'm not driving it, but I just saw there were discussions there.
And I didn't agree with the direction it was going.
Liudmila Molkova 00:42:14 Yeah, thank you.
Trask Stalnaker (Microsoft Corporation) 00:42:17 Alright, david!
David Ashpole (Google LLC) 00:42:26 So I was talking with my teammate Dylan here, who opened this A bit last week. And… I kind of came across it, and was surprised by it, and so, dug into it a little bit deeper, but… You know, we… we've come a long way from the logging API being for bridges, right?
And, Yeah, I was… I guess I was surprised to find that we were considering opt-in for logs as an API, given logs already have Like, typical logging already does log levels.
Right.
And so, I think… I wanted to raise it here. I think we actually added opt-in to the Semantic Conventions for all signals, is that… is that right?
Liudmila Molkova 00:43:21 Okay. Yep.
David Ashpole (Google LLC) 00:43:22 And so… I guess from my point of view, I wanted to come and maybe have a conversation about whether that actually makes sense. I kind of… similar to, like, what Jack was talking about earlier with declarative config.
matching up with what Semantic Conventions does.
I think we need to coordinate what Semantic conventions has with what our instrumentation APIs look like, right? Because ultimately, like, we want to be able to take these YAML documents, Markdown or whatever, and convert them into code that uses the OpenTelemetry API.
So my thinking… For this specific issue.
is that… My preference would actually be, or my proposal would be, to actually, instead of having requirement levels for logs.
To actually use logging levels, because that's what… that's the knob that the API currently provides for… Controlling the, like, verbosity.
opt-in, opt-out behavior for logs. There's one caveat there, which I think is, like, surprised me as well.
Which is that… Like, for most other logging libraries, if you… you know, log something at debug level, it doesn't show up by default, right? Debug level is the way that you say, like, hey, this log is really noisy, or it contains things you might probably not want, and so… Like, I'm making a debug because I want it to be opt-in.
And so the funny thing with our current… logging SDK, because it was originally for bridges, is that the default logging level is all the logs.
So one thing we're missing… perspective.
Is the ability to… Provide a default logging level.
Jack.
I'll let you…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:45:19 I know, I agree.
If you want to finish your thought, please do.
David Ashpole (Google LLC) 00:45:23 I have some, maybe, very rough ideas for what that could look like.
But I guess from, like, a super first principles point of view, it feels like… from an API design perspective, we should have one knob to control like… The requirement level slash, like.
Opt-in, opt-out verbosity of a piece of telemetry that you emit?
In the instrumentation API, and I think For logs that already exist as level. For metrics.
I, like, obviously, I have a separate proposal that's been around a while, but I'm flexible on that, which just has a opt-in, opt-out, kind of inspired by this requirement level.
Concept. And then, for spans, I think the design space is pretty open. I could, I have some interesting ideas, but I don't know if they're that useful yet, until we've kind of… I think the bigger question is, like.
Are we willing to revisit having requirement level be a cross-signal concept, and orient this more towards how the APIs are designed today?
And then… Like, are we okay?
Do we want to switch from using requirement level for logs and events to something that's more closer to what, like, logging has traditionally looked like with a log level?
So, those are my questions.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:47:00 just so, my hand went down, but… I think that was automatic, not from me. So, I think what you're saying makes sense to me intuitively. One thing that I was thinking about as you were talking was that the way that you typically select, to the severity level is with is by scope or library name, right? And so… events are sort of, orthogonal to that, in a way. Like, I think if you want… if you wanted to have severity be the primary way that you selected which events are on or off, you'd want to have a selection criteria in the SDK to be able to select not just by scope, but, by event name.
That's all.
David Ashpole (Google LLC) 00:47:51 I agree, and just before, maybe, I'm sure Liudmila has something to jump in and say as well, but I will say that, like, to me, I just want to make sure we separate the API that we give to instrumentation authors, so that they can, like.
Have a very clear way to… say what they, you know, what the relative priority of something is, versus the knobs that we have in the SDK that let someone change the defaults, right? Okay.
Liudmila Molkova 00:48:20 Yeah, so, I think… Opt-in.
Is… very vague.
And it means two different things. The per-signal enablement, And… just enablement. So, for example, today, all the… Event-based exceptions.
Log-based events exceptions are opt-in.
Not because of the severity level, it's orthogonal, but because they are in development.
They're not stable.
And opt-in is, in my mind at least, it's all of these things. It's a feature flag. It can apply to a feature. Is this operation instrumented? It would equally apply to metrics, spans, and events, because Let's say this piece is in development, or it's very verbose, and you only want it in certain cases.
Opt-in and Semantic Conventions is the way we say That, we don't know how, but please make it configurable and not done to meet it by default.
the… for logs, well, we can argue about logs, but I don't… I don't want to talk about signals between… well, differences between signals.
In my mind, I think it's not the OpenTelemetry API in its current shape concern.
it's the higher level API, the instrumentation API, if you will, where you say, okay, is this… enabled.
And there could be a multiple set of options that are… Defined for this property, for this signal.
That affect how and if it's recorded.
For example, the development, the experimental opt-in thing.
It's also not related to stability, because, you know, the old thing is stable, the new thing is opt-in, and you want to opt in into new thing and disable the old thing.
So I'm kind of thinking about it.
as if we did what Jack proposes.
In Semantic Conventions, if we specified configuration options.
the requirement level on all signals. ALL signals in my mind, would go away.
Because for metrics, you would say, okay, this is controlled by this config option, and this config option is off by default.
So we would do better. We would specify how exactly instrumentation can check if it should emit it.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:51:17 I think we have that API already.
is enabled, right? And the question is, does that include all the parameters that you would want to make a decision on? I think we've tried to do a pretty good job.
Liudmila Molkova 00:51:27 Enabled is on… it's on the, logger tracer meter. It's not on the signal.
For the signal, you need a configuration option.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:51:40 What is it?
Liudmila Molkova 00:51:40 Not given… It does, because you can… you want… A stable, let's say a stable signal is on by default, the experimental is off by default.
David Ashpole (Google LLC) 00:51:53 When you say signal, do you mean… Individual, like, instrument span event, or do you mean, like, tracing the signal?
Liudmila Molkova 00:52:03 I mean the individual instrument, span, or event.
David Ashpole (Google LLC) 00:52:14 I… I agree.
I think I could… I could get behind… our API is consistently… Having, like, a stability level or something on them, like, as an advisory parameter that controls.
Liudmila Molkova 00:52:34 I'm saying it's orthogonal.
David Ashpole (Google LLC) 00:52:36 I… It's orthogonal to what, sorry?
Liudmila Molkova 00:52:42 to the… default level.
So you, you say, okay.
David Ashpole (Google LLC) 00:52:48 I agree. So there can be a stable opt-in thing, and there can also be An unstable recommended thing.
And the default behavior… Is gonna be, like, the union of the two.
Like, it has to be stable, and… And required for it to actually turn on by default for users. Is that what you're trying to say?
Because I definitely agree with that.
Liudmila Molkova 00:53:18 I think there is a list of configuration options that may affect instrument, whether instrumentation should emit it or not.
And… A single thing opt-in does not describe them.
And if we hand that.
If we had it described in configuration, if it was easy to use for instrumentations.
What do we need?
to express these requirement levels at all. I don't think so.
David Ashpole (Google LLC) 00:53:50 I mean… I guess I'll… I'll give my… my, like… so, from a higher level, I think… the way I… you know, think of, like, API versus config design, is that I want the configuration to be on the SDK, And I want the API to be… What the instrumentation gives to the SDK, so, like.
The instrumentation API should have the knob that says, how important is this piece of telemetry?
And then the SDK can decide you know, like, whatever properties about the instrumentation the instrumentation author or Semantic Conventions wants to provide gets passed to the API, and then on the logger, like, the SDK config, right, that's where all of that Those configuration and, like, YAML and stuff. I know we're talking about instrumentation configuration itself.
But I guess… To me, the better overall design would be if Actually, the basic things, like turn things on or off, or… similar things to that are actually configuration on the SDK. Like.
If you can do it with a view or something similar for metrics.
you would do that rather than have it be on the configuration of the HTTP instrumentation library.
Liudmila Molkova 00:55:25 It is true, but only because, it's… Okay, let me reverse this for a sec. So, for instrumentation to know which advisory parameter it should set.
It needs to consult this configuration first, anyway.
David Ashpole (Google LLC) 00:55:44 No, so I… I think that's backwards. Or, like, I… I think the Semantic Conventions should state, essentially.
the things that get passed as advisory parameters, right? Like, this… this log here You know, that we've defined includes some, you know.
Piece of information that should be off by default, or… Like, this thing is experimental, or… like, whatever it is that needs to be passed to the API should be defined in the conventions, and then when you want to override the defaults, that seems like it's better done through SDK config, right? Like… Rather than having to pass configuration to the instrumentation, and then the instrumentation passes it to the API.
Liudmila Molkova 00:56:30 It would be impossible, because then instrumentation would need to collect everything.
And SDK would need to drop a lot of it.
David Ashpole (Google LLC) 00:56:39 Well, I mean, most of, like, maybe Jack was gonna make this point, but I think, hopefully, we capture a lot of that via the isEnabled Functionality, like…
Liudmila Molkova 00:56:48 Enabled on the SIG… on the tracer for everything, but not on the signal.
David Ashpole (Google LLC) 00:56:59 That was Jack's earlier point. Yeah, I'll let you talk.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:57:01 Just a signal, it's not traces, metrics, logs, it's, like, the individual piece of telemetry that's being emitted.
Liudmila Molkova 00:57:08 EVs, yes.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:57:09 Yeah, but, like, the point is, with enabled is, like, you know, you're… it's on the… it's attached to the logger, but you're presenting it with the information for the individual piece of telemetry that would be relevant for making that decision. So you're saying, like, logger is this log enabled, where you specify the severity and the event name and the context.
And hopefully, that's all the information that you would need to make the decision of yes or no.
Liudmila Molkova 00:57:35 Oh, for enable, but then, let's say we wanted SDK to take care of instrumentation config.
It's impossible.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:57:45 Yeah, no, like, and what I was actually going to chime in with, was that, like, we need a litmus test for, like, which types of configuration should be, like, instrumentation API side, like, upstream, and which things should be, you know, in the SDK. Like, you can make an argument for any SDK option should be instrumentation and vice versa, but there's… there's side effects and repercussions, and… I think it's probably, you know, Worth writing those down.
David Ashpole (Google LLC) 00:58:12 I agree, by the way. I understand that, like.
the HTTP header allow list that we collect or something might not be… well-represented an SDK can be, right? But, I think for, like.
Most of this discussion centers around turning things on or off.
I think in this case, it's, like, at an event level.
Liudmila Molkova 00:58:35 Well, I don't think… I don't think it's an event level, I think it's at the feature level.
It's, multiple, signals, in the sense that multiple… This… this span metric and event can all come together as a part of operation instrumentation.
And you would essentially enable certain operations, or disable certain operations, rather than say, okay, I… opt in this metric, but the spend for it is recommended. You would… we wouldn't do this.
So, I think, like, saying that, we… requirement levels make sense on metrics and don't make sense on other signals is… is not right. We should either remove them from everywhere.
And replace them with some form of configuration options.
Or, we should keep them everywhere.
Trask Stalnaker (Microsoft Corporation) 00:59:38 I'm gonna call… have to call time on this.
Any, what… what sort of next step, could… David, could you maybe, like… write up, kind of, these two different yours and Ludmila's, sort of, proposals… Like, sort of something concrete we could look at next.
In the meantime, and next week.
David Ashpole (Google LLC) 01:00:05 Yeah, sure. Would you prefer that I comment on the existing issue that Dylan raised, or do you think it would be better as its own Topic.
That's probably a question for Ludmila.
Liudmila Molkova 01:00:20 Either. And maybe we can continue tomorrow on the spec call?
David Ashpole (Google LLC) 01:00:23 Okay, yeah, this is definitely relevant for maybe more than just this group.
Liudmila Molkova 01:00:29 Yeah, and I'll try to show what I'm suggesting, with the… the… Config options.
David Ashpole (Google LLC) 01:00:37 Yeah, the idea of a cross signal turning on of a batch of telemetry that's related is very intriguing to me, so I… yeah, I'm definitely… Interested.
Trask Stalnaker (Microsoft Corporation) 01:00:51 Yeah, seen the declarative config… For me, helps to visualize the options also.
Cool, Sorry we didn't get to that, but we will… See you all tomorrow and next week.
Christophe Kamphaus 01:01:10 See ya.
Liudmila Molkova 01:01:11 dear.
