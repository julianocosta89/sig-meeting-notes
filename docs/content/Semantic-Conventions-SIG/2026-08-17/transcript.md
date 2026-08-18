SIG: Semantic Conventions SIG
Date: 2026-08-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker (Microsoft Corporation) 00:02:57 Hey, folks.
We'll give a couple minutes for people to join here.
Cool, well… I hope everyone's having a better day than GitHub.
Looks like we've got a good group here, so let's… Bye.
kick it off, with Ran.
Rayhan Hossain 00:04:22 Hey, can you hear me?
Trask Stalnaker (Microsoft Corporation) 00:04:24 Hey, yeah.
Rayhan Hossain 00:04:26 Yeah, I was also trying to open my issue in GitHub, but unfortunately, I can't.
Trask Stalnaker (Microsoft Corporation) 00:04:31 Yeah, I'm not sure we're gonna, be able to, look at anything in GitHub today.
Rayhan Hossain 00:04:39 Yeah, but maybe, maybe I can just, describe something?
Trask Stalnaker (Microsoft Corporation) 00:04:45 Yeah. Yeah. Yeah.
Rayhan Hossain 00:04:47 So, hey, this is Rayhan, so this is my first meeting in this special SIG. Before that, I worked in the hotel collector, but here, we are coming with a new proposal, kinda, like… At Microsoft, we are working with a new database called, like, DocumentDB.
And it's now open-sourced and also under Linux Foundation.
Our idea is, like, okay, in the client side, we are still using, like, Mongo protocols and MongoDB drivers, but behind the backend, we have our own Postgres engine, which is running and serving the purpose of MongoDB engine.
Now, when we are working with all the MongoDB drivers and, like, Mongo Protocol, so we don't have a solid way to Track the, like, end-to-end traces.
And, unlike our HTT protocol, we don't have a very special, like, specific headers or something like this in the Mongo protocol.
So, we are thinking, like, how can we enable end-to-end chesses in this Mongol world?
So, then we figured out, like, okay, there is a field called, like, comment, and it's already implemented in all the MongoDB drivals, and as well as, like, honored by the backends, like, different implementations of Mongoose.
And we wanted to use that, like, leverage that, like, comment field.
So that, like, customers who want to, tag this, like, end-to-end trace data, they can push their, like, traces In a very specific format.
And that format, we already implemented this as a POC, for our internal DocumentDB. Well, not internal, so, it's already in the GitHub. The reason I am bringing up this DocumentDB is, like, it, like, talks in MongoDB protocol, like, it uses and supported by all the Mongo ecosystem drivers. So… Now, the question came into mind, okay, so now we are doing this, we did this as POC, and it's working, and… if we start, like, supporting all of our customers, and in Fusar, maybe there will be another implementation, like us in the, like, Mongo world, and hope they come up with, like, a different kind of solution. It's not a good practice in our Mongo ecosystem.
That's why we came here, to discuss, like, hey, so the way we are trying to solve the problem, it's already kind of proved it works, and it does not break anything in the engine or, like, protocol layer for the MongoDB. So… We just want to discuss, like, this, hey, is this the right direction we are going, and how can we kind of, like, can we do something to standardize it so that, like, not everybody develops their own custom solution, something like this? Can we standardize it? And what is the process?
Hope you… hope you could hear me.
Okay, I cannot hear anything. Is anybody talking?
Trask Stalnaker (Microsoft Corporation) 00:08:07 No, you… nobody's talking. I was gonna defer since we've chatted before, and see if there's other, other.
Rayhan Hossain 00:08:16 Okay, yeah, yeah.
And I opened the issue, so try to summarize what we did versus what we are proposing to do in the GitHub issue. Unfortunately, we cannot look into that, just, try to get an idea and discuss.
On the fly here.
Josh Suereth (Google LLC) 00:08:34 The only question I have is, it's… this is more of a practical question. Are there database abstractions that put MongoDB, like, with other things? So, like, from an instrumentation perspective, if I'm using JDBC, And I have to say, is my driver MongoDB or not? You know, that would be broken, but as far as I know, MongoDB, like, that's not how this works. We already have MongoDB clients for everything, they're kind of custom, they're not, like, standard SQL drivers, in which case, like, having a MongoDB-specific convention for how to pass things into MongoDB seems fine to me, and yeah, I think there's a… we need to kind of document what that is, where that lives, and standardize it.
Yeah, it… but this is more like the, an open question, right? If… if there are non… if there are systems that we need to instrument that interact with Mongo and other systems.
Such a standard could be somewhat awkward for us to maintain.
But if Mongo's kind of always, like, this leaf that we can just say, do you support Mongo, yes or no, then it's fine, in my mind.
Trask Stalnaker (Microsoft Corporation) 00:09:45 And I think that's how all the, the Mongo drivers, are, and… So… I think that, point of standardizing this would be that we could, in our OpenTelemetry Mongo, client instrumentations, we could add this kind of support, and then if a backend that is implementing the Mongo protocol.
Could choose to do something with that or not.
Ravi 00:10:28 Yeah, just… my name is Ravi, I'm from AWS team, and we also provide Amazon DocumentDB, and we partner with Microsoft for this open source document DB initiative. I'm also here for this same issue.
So, from the MongoDB, it is a very standard practice. Please pass any debugging, tracing information as part of comment field.
All drivers supports it. The only thing we might need to be cautious is, while we are using this comment field, we need to make it a little bit more flexible so that The existing applications or the drivers which are sending the messaging or debugging tracing, they still have a scope to send it, so probably we can add this as an object.
That we can discuss as part of design, but at the high level, it seems to me the right place to pass the telemetry information.
Rayhan Hossain 00:11:29 Yeah, in the design, just to give a little bit idea, like, right now, we are, putting it into kind of very specific methods format, like objects, but we also wanted to, kind of, reserve some flags, like a structure, object, like, structure, and make it extendable in future, like Meetings and others, then we kind of, like, we didn't go to that direction because we thought, like, we are making it unnecessarily heavy. Yes, so we can discuss these options also as part of our design.
step, if we, like, agree on the first side, okay, this sounds like a good idea, then I can submit the PR, design PR, and we can discuss there as well.
Trask Stalnaker (Microsoft Corporation) 00:12:17 Yeah, yeah, that sounds like a good, definitely some… details to… Understand and, propose separately, just seeing if, No.
We're not… it's not gonna happen. Cool.
Any other… Anything else you wanted to share about this, Rayhan?
Rayhan Hossain 00:12:43 No, then,
Trask Stalnaker (Microsoft Corporation) 00:12:45 I think.
Rayhan Hossain 00:12:45 That's not mixed.
Trask Stalnaker (Microsoft Corporation) 00:12:46 In general.
Rayhan Hossain 00:12:46 maybe I will think, like, okay, so please take a look when GitHub is back, if you get a chance, and I will, get a draft design PR ready, and come to the next meeting, or maybe, some next meeting, very soon, to discuss the design and see, like.
How do we feel about our current implementation versus what could we sends before making it a standard?
Trask Stalnaker (Microsoft Corporation) 00:13:10 Cool, that sounds great.
Rayhan Hossain 00:13:12 Thanks.
Trask Stalnaker (Microsoft Corporation) 00:13:13 Thank you.
Alright, moving on, Jack!
Welcome.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:13:21 Aye.
Yeah, I, Well, I guess let me… let me try to figure out how to frame this. So, There is a sort of informal relationship between declarative config and semantic conventions today.
The way that it is played out is that, you know, there is some sort of ad hoc prose in the notes section of certain attributes in semantic conventions.
And declarative config, not wanting to define concepts itself, waits for those note sections to exist that define, you know, the names of properties and what the semantics should be. And once those exist in semantic conventions, we'll go and add the equivalent types and properties in the declarative config JSON schema.
And, you know, I think a lot of us have sort of been looking at this and seen an opportunity for tighter integration for a while. There's a Semantic Conventions 2026 roadmap issue, which mentions this.
And, you know, I think several of us have talked about, like, you know, using some of the Weaver or Semantic Conventions tooling to generate accessors for these different, you know, standardized instrumentation configuration properties, so that instrumentation can reliably access them and initialize accordingly. I think that's kind of, like, the next step to making Declarative config and instrumentation config work in a sort of intuitive, seamless way.
So yeah, that's… this is the sort of… this is sort of the background of this problem, and what I aim to solve, and what this PR does here is one direction of what we could do for a tighter integration. And, you know, after I describe this, I'll kind of discuss the alternative as well. I think there's kind of two main paths that we could take, and this is one of them. So, This PR is characterized by, you know, directly in the Semantic Conventions YAML model, there is, there is, you know, additional data, additional metadata that describes for certain attributes and certain groups what the properties are that should be configurable, and what the descriptions and defaults of those configuration properties are. It's sort of like we're embedding little bits of JSON schema directly in different attributes in the Semantic Conventions YAML model.
And, you know, the idea is we embed little snippets of JSON schema and Semantic Conventions, and then over on the declarative config side of things, we have Semantic Conventions as a Git submodule.
And so we have a, like, you know, a ref.
to the Semantic Conventions version that is encoded into declarative config JSON schema, and when we update that ref, then we update the type definitions and declarative config that, you know, correspond to instrumentation config. And there's, you know, tooling in, you know, the declarative config repository.
that goes and walks the Semantic Conventions YAML model, finds these little bits of embedded JSON schema, and sort of maps them to the correct types and, you know, format that we render and compile our output JSON schema with.
So, yeah, it's like, you know, on the Semantic Convention side, there's bits of embedded JSON. On the declarative config side, there's a submodule for semantic and tooling to incorporate, you know, the Semantic Conventions little snippets, into the schema.
And… I guess I should also say that, you know, in order to verify that a change to Semantic Conventions doesn't break open telemetry configuration, there's a new Semantic Conventions GitHub action workflow that, for any given commit, will go and check out declarative configuration. It will update its submodule reference of semantic conventions to whatever PR commit is being you know, being acted on, and then it will run the declarative config tooling to try to, you know, generate the… and compile the JSON schema in declarative config, and, you know, if any errors take place, or if any diff is produced, those are sort of, like.
You know, spit out as artifacts of that build.
So, yeah, that's sort of what I propose, and I've been talking for a couple of minutes, so I'll pause, and, you know, there's a distinct other direction we can go that I think is worth mentioning as well, but I just want to first get your all's reaction to that.
Josh?
Josh Suereth (Google LLC) 00:18:39 I'm not sure if you could read my comment on GitHub, because GitHub went down slightly after I commented, but, I love what you're doing here, like, this looks amazing, but one thing I want us to sort out is ownership.
Right? So, one of the things I noticed was we had main of some kind of point out main of configuration, and if we create a bidirectional dependency hell here, I think that's problematic. So, like, the main thing I want us to figure out is who owns what.
And can we have a very clear interface between the two projects? So, if Semantic Conventions is the truth for instrumentation config.
great. I think that gives us a real clear boundary. So then the… if we can get to the point where the tests that you have are on some stable release or something, that we can make sure we don't break you via a consistent interface.
And then, you basically consume our releases into the configuration spec.
that's fine. If we do it the opposite way, I'm also okay, of, like, we… you define it, but we need to figure out who owns the baseline, right? Like, and what I heard you say, so tell me if I'm wrong here, was you tend to wait for the semantic conventions first. So, like, if I were running instrumentation.
we would start with semantic conventions. We'd define all the configuration capabilities when we define the signal.
there, and then that will create a configuration package that we apply to the configuration spec. Is that correct?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:20:05 Yeah, exactly. So, it's… configuration depends on semantic conventions, not the other way around, and I guess, like, there's a test time dependency for semantic conventions on a configuration, just as, like, a smoke test type of thing, because, like, you don't want to be writing in semantic conventions little bits of JSON schema, which, like, you know, upon updating.
the configuration dependency on Semconf break everything, right? So it's just, like, you want to make sure that you're not going to break that, like, when configuration updates its dependency on semantic conventions.
Josh Suereth (Google LLC) 00:20:39 Right, so what we want to do then is find a way to make that test not have our two repositories both depend on main of each other. Because if you break your tooling, and then all of our code is broken, right, that's like a huge… it's just like blast radius of breakage.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:20:55 Right.
Josh Suereth (Google LLC) 00:20:56 The way that we could get that level of enforcement that doesn't rely on both of us relying… both of us depending on each other's main headline branches.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:21:05 So they don't both depend on main. Configuration depends on a pinned version of Semconf, and it will actually only depend on releases of SemConf. So, what release are you on now? Like, 146 or something? 145?
Josh Suereth (Google LLC) 00:21:19 But we depend on main of configuration.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:21:22 Right, so you can make that, adjust that from main to something else as well, like, you know, I don't think that that would be problematic, but, you know, we're in this sort of chicken and egg situation where we initialize this, right?
Josh Suereth (Google LLC) 00:21:35 Yeah, yeah, that's fine, as long as we break the hard-coded dependency here. Like, again, anytime I've had these, like, bidirectional dependencies, it becomes… A maintenance nightmare at times, when you make a break.
But not that we want to make a break, it's good that these things catch it, but sometimes the breakage is not even, like, that significant, but unrolling it and just getting things to pass where you can start submitting is somewhat problematic, right? Yeah, definitely. So that's all I want to avoid here, yeah.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:22:04 And I think you do want to reserve it, the ability for it to be, like, Semantic Conventions, it's, it's build workflow, it depends on a ref from configuration that can be, like, changed over time, because, like, there's this one bit of the integration, which is, like, there's this concept that I talk about, which is called, like, config scopes, and so it's like, you know, Basically, we don't want… I don't think we want, you know, explicit hard-coded references to declarative config types scattered all throughout semantic conventions. So instead, we say something like, hey, within the scope of HTTP client.
which is applicable to client spans and client metrics. You know, there's… there's this configuration property, which is, like, you should be able to configure the set of, HTTP known methods.
And so there's a mapping that's defined. So between these scopes, which are, like, sort of identifiers over in Semantic Conventions land, and the actual types that are in declarative config, what those… what those properties are gonna, like, map to in terms of types. And, somewhere that mapping needs to be defined.
And I want… that mapping needs to be able to change, and so, like.
you know, the reason I'm talking about this is because, like, occasionally it will be a good thing for semantic conventions to be able to update to, like, the main or the latest ref of declarative configuration, and not necessarily, like, always, like, a pinned version.
Josh Suereth (Google LLC) 00:23:35 Yep.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:23:36 So, there's that, and I also, just on a related note, I would say that, like, you… if we go forward in this direction, we would want this build step in Semantic Conventions to, like, not be required to merge. Like, have it be, like, something that informs your decision, but not necessarily blocks it, because we don't want to get, like, stuck.
Josh Suereth (Google LLC) 00:23:55 Okay. Yeah, I, I'm fine, I, like, but for context, I… Maybe we do both, maybe we have some sort of confirmation step that does a bare minimum.
Right? That would block a PR for submission if it, like, could never work with config, and then we have the full integration test be something that informs things and runs as well, right?
I'm fine with both, yeah. Just, I want to make sure that we can handle the inevitable breakage that we will cause each other, because we're human. It's gonna happen.
And if we use agents, it'll happen faster.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:24:29 Right. And this actually leads to… this, I think, is a good segue into, like, the other direction that we could go for this. I just want to, like, plant the two major directions you can go and see whether you guys lean towards one or another. And the other direction is, like.
Rather than trying to have semantic conventions and declarative config versions be coupled together, that's what I'm proposing here, is, like, every version of configuration has, like, a pinned version of semantic conventions that it's associated with.
And so those versions become coupled together. So rather than that, you treat them as completely independent versions.
And you say that, hey, there is a declarative config type called, you know, ex… instrumentation, or some path in declarative config, and the description of this is that it is, like, completely this type and all of its, like, properties are owned and versioned and managed by Semantic Conventions.
And if you want to go see the schema for this type, you know, go look at this link.
And, and so, you know, essentially then, when you are… Like, when you're a user.
You have a sort of declarative config version, and you have a Semantic Conventions version, and those are not in lockstep with each other.
And there's trade-offs, because, like, what you can do with the approach that I'm suggesting in this PR is you have one completely compiled schema, where it's, like, all the schema, the SDK config, and the instrumentation config, and you can go to, like, a schema, you know, renderer, like I'm about to send over in the chat.
And you can, like, walk through as a user.
all of the different types and properties that exist in this schema, and they're all, like, work nicely together. And you know that for that version of declarative config, these types and these properties are all, you know, the source of truth.
and that goes away if the versions are sort of more loosely coupled with each other.
but, you know, on the other hand, it sort of gets around this weird, emergent property of the design that, like, I have a PR for, which is, like, think about, think about, code generation, if we go forward with the PR that I've proposed.
When you have code generation, and you want to generate, like, accessors for instrumentation config properties, you need to have a version… a dependency version on not just semantic conventions, but on declarative config, and those versions need to agree with each other.
And that's weird that, like, generated code needs to, like, sort of be pinned to declarative config.
And I guess on a related note, like, declarative config needs to publish a new version every time that Semantic Conventions does, because those, like, those versions need to develop in lockstep with each other. So… trade-offs.
Josh Suereth (Google LLC) 00:27:40 Yeah, one thing that has colored our view for, like, the Semantic Invention tooling, like in Weaver, is the notion that we have, like, open telemetry is open, which means it's open for extension.
Which means people can create a new component, and they can define new instrumentation for that component. They can define new configuration for that component, right? And so, what's… what is the… the ex… open extension idea or rationale in the configuration spec? Like, could it be that you actually define a core.
like, Semantic Conventions Core, and then, we would publish our configuration extension somewhere, so you still get the registry from OTEL, but where it's known that you're going to be open, and so if someone uses this configuration capability for their own instrumentation they're writing in their company, they can still get declarative config samples from it, right? Because we allow this open extension everywhere. Like, to me, that's more powerful, like, that's the world I'm trying to go after with Semantic Invention, of like, make sure we build something where the core is stable, and you can extend any piece.
And that the extensions can continue to compose with the original, right?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:28:52 Yeah, that's exactly this alternative path, is, And, you know, declarative config could participate, or, you know, be a more… facilitate this by providing reliable tools to do some of the things that we do on configuration for, you know, conformance to JSON schema.
To, like, we, we, we have a sort of, we have a JSON schema compilation process where, you know, you write this sort of raw schema in YAML format, so you can take advantage of YAML, and you can take advantage of some additional keywords that we've introduced that aren't supported by JSON schema, and then we compile that into, like, a proper, like, JSON, JSON schema that, like, you know, conforms to a very specific version of the JSON schema spec.
And so, like, we could make that tooling accessible to semantic conventions, so, like, you know, what you all do if you write your own, you know, type that is an extension point for declarative configuration is, like, it meets all the same guarantees that we… that we hold ourselves to over in declarative config.
So, that would be another route.
Trask Stalnaker (Microsoft Corporation) 00:30:11 Jack, would that, If we did that kind of extension point, could that be generalized also to, like, custom instrumentations?
Would that be even beneficial? I'm trying to think.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:30:28 I've thought about that a little bit. I think in theory it could be. You know, I would probably make… try to make the tools available to, to be used in, like, an open-ended capacity, but I… for individual instrumentations, I think it's just simpler to, to do, like, what, a schema validation on read. So, like, rather than trying to, you know, incorporate all this tooling from the configuration repo and express things in JSON schema, just, like.
You know, read this generic configuration properties object, and assert that the configuration the user has tried to provide to you matches whatever schema you need to enforce for your instrumentation.
I just think, like, instrumentation libraries are a lot lighter weight and smaller, and…
Trask Stalnaker (Microsoft Corporation) 00:31:19 Yeah, and it's single use.
Place, as opposed to that your… even your… your corporate Semantic Conventions, say, that would be in use by lots of different places.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:31:34 Right.
But, you know, I think I would try to structure it so that if somebody wanted to go in that direction, they could. And, you know, I think it would really help if… If there was… a library that wanted to sort of, like, work with me on that, rather than me trying to, sort of.
guess their needs. They could, you know, we could work hand-in-hand to develop the tooling together.
Trask Stalnaker (Microsoft Corporation) 00:32:00 Yeah, I'm trying to think from the, like, Java instrumentation perspective.
So we have… we do have a bunch of, sort of, common Settings that we, have across, like, across our… messaging instrumentations, or across our database instrumentations, we have various settings that aren't in SEMCOM, but that we apply. And I guess we've got a couple options. One is to push them up to SEMCOM, Which is maybe the… probably the better path, but the… The other would be… something there, but yeah, I don't want to complicate this, because, I… I do, I, I, I really like… I mean, As… Much as this brings a lot of extra complexity, Which isn't great.
It is a really… I think it is the direction that Semantic Conventions is going.
So it makes… make… probably makes more sense.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:33:12 I just don't know… What the other candidates would be for, like, extension?
In, like, you know, Semantic Conventions is getting into federation, right? So, declarative config federates a portion of its schema to Semantic Conventions, and Semantic Conventions itself is federated to other places, and so… How does all that get bundled up together into, like, sort of one resolved, schema, or, you know.
A Resolve schema you can explore and navigate.
Trask Stalnaker (Microsoft Corporation) 00:33:49 Yeah, so kind of what you were describing before of the users who want to resolve the schema, would supply their schema, their semantic convention registries.
That they want to be resolved.
Which is sort of how the Semantic Convention Registries work.
also where you have, like… we have the Gen AI registry, and it depends on the core registry, and you can kind of… Josh has been doing a lot of work on, kind of, transitive, dependencies and resolution there, so I think you would sort of piggyback on top… on… on that a bit.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:34:31 Okay, and then, so every one of those registries then sort of has this new thing that it encodes, which is its JSON schema for configuration, and… Thus by, like, you know, if you… if you say you depend on this set of registries, you know, the core semantic conventions and then your company-specific one, you can sort of resolve the full set of JSON schemas related to the configuration.
Josh Suereth (Google LLC) 00:35:00 So, I have to drop in, like, 2 minutes, but real quick, if you put all the things into annotations, Jack, then all of our distributed things will keep those annotations.
So if you have a mechanism of inferring the JSON schema from the annotations, then yes, for the entire dependency resolution hierarchy that you have, we could re-infer that JSON schema.
Like, we could provide a… we could make it first class if you want. Right now, you could do it via, like, a template or a package or something, but yeah, you should be able to resolve for all of those. And then the idea behind Weaver is now, in the future, instead of getting just one.
repository resolved, you get the whole dependency chain, like, fully resolved. So we actually do dependency conflict resolution grab, and to Jack's point, the entire maintainer group has been fixing all the bugs. It's way bigger than one person.
But we are adding dependency resolution. That's been, like, the past 3 releases. I've been fixing all the bugs and trying to make that be as stable as possible. So, you should have it, it should be working.
Right now, it's… from the tests we have for, like, the hotel side, and from some companies that use Weaver internally, the next release should fix most of the bugs there, if you want to kind of try it out manner.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:36:10 Okay. Yeah, I think… I think just thinking about this more, just with, Semantic Conventions itself federating, we… we… that's really sort of pushing in this direction.
It's gonna be hard to sort of go against the grain and have declarative config and semantic conventions, like, centrally managed, whereas everything else is federated.
So…
Trask Stalnaker (Microsoft Corporation) 00:36:36 Yeah, and I mean, it's gonna require… it requires certainly a lot of, tooling, to support But in the long term, then you don't become a central bottleneck.
Which is part of the… thing that the Semantic Convention Federation is solving.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:36:58 Yeah, and luckily, at least for now, there's not just, like, a massive amount of configuration surface area that we need to sort of, like, migrate. The surface area is small, so… You know, by getting ahead of it, it's just… it's more manageable to migrate.
Okay, well, thanks for the conversation.
Trask Stalnaker (Microsoft Corporation) 00:37:24 Yeah.
Yeah, thanks for tackling, or starting to look into that, because, yeah, that has a lot of promise.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:37:33 Yep.
Trask Stalnaker (Microsoft Corporation) 00:37:35 Riccardo, hey!
Riccardo Magliocchetti 00:37:37 Hi, everyone.
Let's see if… It helps… I will open the issue, otherwise I've shared a bunch.
more links, like… I was reviewing the… Python, default service name implementation, both in this SDK path and in the Kali config part.
And… I saw, like, I was reviewing the Semantic Convention.
And… When the service name is not explicitly set up.
The service name should be set to a no service, and then followed by the process exhibitor name.
And so, Trask, if you open the other link.
The process executable name is defined as, like, the target of, prox LFX on Linux, and some, edpers on Windows.
And on Python, we don't do that.
And so I took a look at Java, Go, and JavaScript implementation.
And I think most of the languages… Are not following, this, definition.
The one that is doing, like, is post-implementation is closed, that is Go.
But the other languages do something completely different. Like, JavaScript, and Python.
Does not, like, try to use, Platform-independent Implementation, just by looking at The first, argumente na argv.
And… Yeah, Java, I think, if I remember correctly, just out-codes Java as a name.
And so I was wondering if… We won't update the Semantic Convention, like, relaxing a bit, the suggested implementation.
Or if you really want to have, implementation follows more closely with the Semantic Convention. Even if the Semantic Combinator says, should.
But, yeah, Michele, you have your on the rest.
Michele Mancioppi (Dash0 Inc.) 00:40:17 Yeah, this is an interesting topic, because it comes a lot with automatic injection. If what you're doing as a service name Is put the name of the runtime.
It's not really helpful.
So, a lot of languages, like you mentioned Java, .NET does something similar. I've seen vendor distros customizing the behavior further. They actually tend to have language-specific mechanisms to come up with as sensible a service name as you can.
Out of the box.
So, thank you for your service?
Trask Stalnaker (Microsoft Corporation) 00:40:57 His service name is based on the process… let's see… I see, that's the connection, is that it's… Sort of a default.
Michele Mancioppi (Dash0 Inc.) 00:41:13 It's, not very good.
And I feel that's something that we should do in the automatic injection kind of workstream.
Is actually to… to define To open this up, definitely, but with the suggestion of actually Trying to find something meaningful for the language.
Because this is not meaningful.
Trask Stalnaker (Microsoft Corporation) 00:41:47 Yeah, this is an interesting, If the value is not specified, does… I don't… like, in Java, we have some other detection mechanisms, like spring application name, stuff like that.
That makes… More sense for some users.
I'm trying to decide if that is violating the spec here, if this value was not specified. It wasn't specified by the user, we kind of…
Michele Mancioppi (Dash0 Inc.) 00:42:19 Exactly.
Trask Stalnaker (Microsoft Corporation) 00:42:20 Inferred it, or rather, we specified it.
By, some component we have.
Michele Mancioppi (Dash0 Inc.) 00:42:27 We are violating the SPAC, but for a good reason.
Trask Stalnaker (Microsoft Corporation) 00:42:31 Right, right.
Michele Mancioppi (Dash0 Inc.) 00:42:33 Which means that…
Trask Stalnaker (Microsoft Corporation) 00:42:34 Must. Yeah.
Yeah.
Michele Mancioppi (Dash0 Inc.) 00:42:43 What I think that this should say is to extend it by saying the SDKs are encouraged to find a meaningful value, if none of that can be done, then you must fall back.
So here is missing.
giving the latitude to the SDKs to find a better service name out of the box.
Which could put pretty much all the other districts, including Wagner distros, back into compliance.
Without, actually undermining the worthy goal to say you must have a service name.
Trask Stalnaker (Microsoft Corporation) 00:43:21 Now, Jack, since you're here, I'm gonna pick on you as a SDK, from the SDK… perspective.
Because… you… I think the SDK does follow this. It's the Java agent and sort of our bundles on top of it that don't.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:43:47 No, that's correct.
Trask Stalnaker (Microsoft Corporation) 00:43:49 Michele, like, I guess, kind of… That's… Like, maybe we… maybe it is… valid currently? Like, SDKs generally are just the bare-bones implementations. They don't try to do anything special.
Whereas an auto instrumentation package, Could do more.
Michele Mancioppi (Dash0 Inc.) 00:44:15 We could also put it like that. I honestly would prefer… It's… I've never found a situation where the unknown service Was any good?
And it is always, friction.
For the users.
if we could be more reasonable at SDK level as well, not only at the auto-instrumentation bundles.
I think would be a win for the user experience.
Trask Stalnaker (Microsoft Corporation) 00:44:52 What would be an example that, like, I'm trying to think of it, like, with Java, the SDK, like, the other places where we're getting name… service name from… Oh, totally.
Michele Mancioppi (Dash0 Inc.) 00:45:05 meta.shamf slash pom.xml slash, like, the build.name, I wanna say, Maven.
The equivalent for Gradle.
When you look at Python, there is a lot that you can do by looking at the metadata, the package.
For example, the equivalent of what you would put in byProject.tomo, that data is available inside the, the package, so you can introspect it in Node.js.
package, the meta-leading package JSON, it's usually pretty good, also for, for… Application that you start, yeah?
dot net.
look at cs.project.whatever the form it is, I never remember, that also tends to have the name that the user intends for the component. Very often, those two things go step, like, hand in hand.
Trask Stalnaker (Microsoft Corporation) 00:46:08 So, before I add, like, Jack, I guess… Whether or not you would… want to capture that in the SDK, I wonder if the ship has sailed at this point, like, we couldn't… It would be considered probably a breaking change in the SDK to… Capture something different, unless we consider unknown service to just be kind of useless, and we're okay with breaking that.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:46:41 Sorry, what would be captured instead? Like, some of the more advanced, like, mechanics?
Trask Stalnaker (Microsoft Corporation) 00:46:46 Yeah, say, like, the MetaMF, you know, or the JAR name, or, you know, something… some other heuristic.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:46:59 So the way that the SDK works is, like, every resource that you initialize comes with some default attributes, the telemetry.sdk attributes, and this service.name attribute. If you just use the resource API by itself, that's what you get.
And, you know, you basically, you override that by just merging other resources that have, like, more specific service names, and you, you know, you call the merge API in an order that prioritizes the one that you think is more informative.
And so, like, I think, from a… I think it's impractical to take the, like, low-level API that is the thing that's always responsible for populating unknown service for all resources, and to change it to be, like, more informed.
It's just… it's like, it's too low of a place to, to, you know, start to do this introspection on MetaImph and all the other things that you would need to do to have, you know, better service names. And so, I think, like.
You know, we're… the territory that we're talking about is, like, one of the other resource detectors that's higher up.
from, like, the base API, so something in auto-configure, something in the agent that sort of detects these other sources of service names and does something with them.
Michele Mancioppi (Dash0 Inc.) 00:48:25 So, this is a very legitimate position.
But then we need… Like, my feeling is that we should treat it as one of the… what is the correct word for that? Kind of the built-in…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:48:43 Built-in service detectors? Or resource detectors?
Michele Mancioppi (Dash0 Inc.) 00:48:46 Yeah, because, for example, you wouldn't be able to use the resource detector through declarative config today, right?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:48:54 That's right, yeah, the, you know, exactly. So there's a set of, I think, four built-in resource detectors that are named in the specification. It's, like, service, and container, and process, and host, and None of them are sort of the mechanics that we're talking about here, which is, like, trying to introspect it, like.
how would you guys describe it? Like, in my head, it's like looking at common places within the language runtime where, like, you know, users typically name whatever the application is. And so, is that… I don't know what… how you would abstract that, but yeah, like, coming up with a resource detector that's one of the named ones.
Trask Stalnaker (Microsoft Corporation) 00:49:35 language.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:49:35 It's true.
Trask Stalnaker (Microsoft Corporation) 00:49:35 Specific curious… language-specific heuristics.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:49:39 Yeah.
Michele Mancioppi (Dash0 Inc.) 00:49:40 I would like to raise a point. So, the default, like, the built-in resources that are host.
service, and I'm going to stop here. Which one do you think should set a decent service name?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:49:51 Yeah, yeah, like, maybe you could expand the one that's service, right? Because what service does, what the service resource detector does today is it looks at the environment variable called hotel service name.
And that's it. So it's saying, like, hey, look at the environment to try to infer what the service should be. And, like, I don't think there's anything stopping us from attaching additional behaviors to that.
Michele Mancioppi (Dash0 Inc.) 00:50:15 Exactly. This, I think, would be the best compromise, because it is… it would come in the place where you already expect It's something that SDKs will ship. It's something that, to the best of my knowledge, most SDKs do configure.
And we end up in a better state than the deluge of unknown service whatever.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:50:35 Yeah, and to your point, you can still maintain the same mechanic you have today, where it's like, if you set the hotel service name environment variable, that still overrides anything that was detected automatically, but, you know, you just build in some additional smarts.
Michele Mancioppi (Dash0 Inc.) 00:50:49 Okay.
Trask Stalnaker (Microsoft Corporation) 00:50:53 Riccardo?
Riccardo Magliocchetti 00:50:56 Yeah, like, I think that me and Michele are trying to solve two different problems.
But, yeah, like, on the issue, like, if I remember correctly, like, I left true question at the end.
And… one was, like, to make… the… The language here in the service name description a bit more broad.
So, like, I think that… If you have database, To something like… As described by the process executable name, resource attribute, or whatever the SDK… Can, detect, or…
Michele Mancioppi (Dash0 Inc.) 00:51:43 This would be already compliant the moment to replace… so, with the idea of allowing or encouraging SDKs to make smarter service detectors, this would already be compliant if we changed the… if the value was not specified to if no better value could be found, or something to that effect.
Riccardo Magliocchetti 00:52:03 Yeah, but I think that the definition of, like, for me, like.
it will be, like, keep the current code and just use the arcv0.
Or even, like, if you're not able to have that, just our code Python, I think you are looking for something more specific.
Is that, yeah.
Michele Mancioppi (Dash0 Inc.) 00:52:24 But they go hand in hand, right? Because your problem of, oh, how do I do the unknown service? I promise you.
that in virtually every language that anybody cares about, there are always automated ways of finding out a value that is miles better than a known service with ArcV or Python or something else for coded, yeah?
Riccardo Magliocchetti 00:52:47 Yeah, but I'm not sure we can do that in the SDK, like… Bye.
Michele Mancioppi (Dash0 Inc.) 00:52:51 Sure, yeah.
Yordis Prieto 00:52:58 I feel that the SDKs are the ones that are closer to the platform that are deployed, right?
Like, for example, like, if you put it lower than the SDK, would that platform now owns understanding every single programming language, and runtime and release packaging thing?
Michele Mancioppi (Dash0 Inc.) 00:53:16 In reality, it's mostly a matter of, the, when you go and look at the ways you would do it across multiple languages.
There are… there are a couple of… maybe Java is a bit more, I mean, let's say 4. Easy.
packaging and framework-specific places where to look at, and a lot of them are already implemented, so…
Yordis Prieto 00:53:40 Yeah, but that leaves other ecosystems outside, right? And I'm speaking because I come primarily from Merlin and Alexa, and I can guarantee you that the experience there is definitely not the one that you're most likely describing. That is because of that, right? Like… the… from my perspective, right, you take the ownership of LAO, we're gonna make it work for all these 4 or 5 different programming languages or whatever, but then that comes at the cost of the rest.
And they don't even know that it's not even possible, they assumed that it was possible because in some other place was, right? Until they dig in and say, oops, why is this experience in Elixir or whatever so different and suboptimal? And that has been the conversation before, by the way, and… So… What about that, from the ecosystem perspective? Because… Now the conversation derailed into, yeah, it's supposed to be a shared standard, yadda yadda, but… In reality, we all get completely different experiences.
Michele Mancioppi (Dash0 Inc.) 00:54:38 I don't know how comfortable I feel saying that because a language cannot do something better, we need to go with the minimum common denominator.
Because then…
Yordis Prieto 00:54:48 No, I'm not suggesting any solution, all I'm saying is, like, okay, like, how could you solve that problem as well?
Michele Mancioppi (Dash0 Inc.) 00:54:56 If you want, I can go and crack out the manual for the BMVM. I've not looked in a bit, but I'm sure we can come up with something.
Yordis Prieto 00:55:04 Nope.
Sure, you can narrow down to any specific, and eventually just a matter of somebody sitting down and doing it. I get that, like, I'm just, like… From the process perspective, from the spec perspective, from the ecosystem perspective, right?
Like, for example, like, I don't see that many people joining this call like me, speaking in that perspective, as far as I can tell, especially that I maintain the contract early as well.
So, I'm more curious about, like, you know, can… Can they group.
Give better guidance, guidance and tools and so on, for them to own that situation.
Trask Stalnaker (Microsoft Corporation) 00:55:43 I think that's… I… I may not be understanding your question, but I think the kind of proposal here would be to try to relax this and allow languages to do whatever is best in their ecosystem.
Like, not necessarily overly… define, like, oh, in Java you have to do this, in .NET you have to do this, but just leave it a little bit more open for the languages to decide what's best for them.
Riccardo Magliocchetti 00:56:24 Yep.
like, one of the worries I had was, like, that the… like, for us, dynamic languages, I think it's a bit unpractical to have, like, a platform-dependent Implementation, also because, like, we don't have, like, direct access to… platform or operating system APIs.
like, on Linux.
Trask Stalnaker (Microsoft Corporation) 00:56:50 Yeah.
Riccardo Magliocchetti 00:56:50 the file, but on Windows, we have to call.
Trask Stalnaker (Microsoft Corporation) 00:56:53 Yeah.
I agree, like, there's almost no way, like, we're gonna do this in Java.
Word, but, as… Potentially still a useful… something in the spec in that we might be able to find that there's a public normal Java API that Essentially gets us, you know, the same thing.
and it is a should.
Riccardo Magliocchetti 00:57:32 Yeah, but, like, for example, like, I would, like, relax on the service name side. Like, this can still be… Like, instead of pointing to the cross-exhibitor name.
Because, like, you can take a look at this, but the various languages can implement whatever.
Trask Stalnaker (Microsoft Corporation) 00:57:52 Yeah, I agree, like, this one seems kind of okay to me. It's the service name.
That I think our discussion has been around, and it seems like there's at least support among the folks on this call.
To explore relaxing that.
Riccardo Magliocchetti 00:58:14 Yeah, like, so maybe, like, when GitHub's, is online. Maybe, like, Michele you can add a comment, describing the… Your, point of view?
And maybe Riccardo.
Yeah.
Thank you.
Trask Stalnaker (Microsoft Corporation) 00:58:37 Cool, martin, sorry, we didn't have… I know we don't have… time for this. It's a big topic.
And I wanted to have, also, I think, it'll be good to have Lyudmila and Josh here.
To kind of… just kind of discuss the launching of the client-side, SUMCOM, group.
Are you all currently block… blocked on having that repo? Because I think, more or less, I think there's, you know, there's… There's support for the doing that. We just wanted to kind of discuss the kind of oper… like, mode of, like, keeping these groups close, where I think the main concern is, the client-side folks going off And just completely doing their own thing, and not sort of, filtering in knowledge and background from the general semantic conventions.
group.
So if it's something that you all are blocked on and, you know, want to get rolling right away, I could create the repo and you guys could, get going, just with the understanding that, you know, let's still have some conversations and see how we can keep the two SIGs.
You know, contact.
Martin Kuba 01:00:13 Yeah, I think that's something that we need to discuss, But I… so, like, I think the… Android has already… Created their own federated semantic conventions in their repo.
And… and we are about to do the same thing for browser.
So it would be good to have this, so that we can… we can… the idea was to have some… some place to have common client-side synthetic Conventions, And I think it's especially important for the mobile SDKs.
Because they have a lot of overlap, so… But yeah, I think one of the asks that we have heard over and over is that we have to have… we must have representation here, so… So yeah, that's… that's why I'm here, and… And I also tried to… I think… I think the other… the mobile folks have probably conflicts, but, we have a SIG tomorrow, and I can bring it up again.
Trask Stalnaker (Microsoft Corporation) 01:01:11 Cool, yeah, yeah, that would be great, because it is a big… area, of, semantic conventions and of open telemetry. So, like, yeah, if we can… Yeah, figure out how to work together. And not that you need our, you know.
Approval on stuff, but just to make sure that there's, Sort of feedback, and people are aware of what's going on.
In both directions.
Martin Kuba 01:01:45 I'd be curious, like, to hear also how other SIGs are doing it. I know that the Gen AI already has a repo for this.
So, if you can take, you know, some lessons learned from that, Awesome.
Trask Stalnaker (Microsoft Corporation) 01:01:58 Yeah, so I mean, like, Gen AI, right, is, led by myself and Lyudmila, so we're both here and there all the time, so it's maybe not the best. I mean, but it is, you know.
That has, like, been sort of how we've worked. Mainframe is a new one, and I can't remember his name.
but he's… he shows up to a lot of these meetings, so that's… yeah.
Cool, alright, well, we are out of time, but yeah, ping me if you want the repo, created sooner, and we'll chat more next week.
Martin Kuba 01:02:44 Sounds good. Thanks.
Trask Stalnaker (Microsoft Corporation) 01:02:45 Alright, bye.
