SIG: Semantic Convention Tooling
Date: 2025-10-29
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

Laurent Querel 00:00:23 I guess…
Arthur Silva Sens 00:00:35 Hello.
Laurent Querel 00:00:37 Throughout you.
So there is… I quickly passed a link into the chat.
It's, it's a Google Doc that, we use to,
To keep track on the list of attendees, and to have the…
PR project, board, and so on, so I encourage you to… To open this document.
Josh Suereth 00:02:01 Hey, how's everybody doing?
Arthur Silva Sens 00:02:04 Totally.
Josh Suereth 00:02:14 Nope, that's not what we want.
There we go
Thought we'd give another few minutes for the, folks in the, Pacific Northwest to join, since it's a little early for them.
Laurent Querel 00:02:36 Indeed.
Arthur Silva Sens 00:02:41 Is this meeting… in the EU time zone, which changed, or…
Josh Suereth 00:02:50 This meeting has been at this time for a while.
Laurent Querel 00:02:54 From the… from the beginning, I think.
Josh Suereth 00:02:56 Yeah.
Arthur Silva Sens 00:02:57 It didn't change with the similar time savings, right?
Josh Suereth 00:03:03 Oh, oh, you guys, you guys are now earlier, earlier, right? Yeah.
Yeah, interesting.
I don't know if that was on purpose, or by a happy accident.
A happy coincidence, if you will.
Anyway, why don't we get started? I think Jeremy's here, so let's, let's, you wanna walk us through what you want to talk about, Arthur?
Arthur Silva Sens 00:03:32 Yeah,
So, I'm not sure who saw, but, I think Laurent shared in the Hotel Weaver Slack that I gave a talk at PromCon.
Explaining how Weaver could be used by Prometheus, like, to generate Prometheus SDKs, dashboards based on Prometheus instrumentation, etc, etc. And after this… this talk.
the Prometheus team sat together, and we discussed several topics. One of the topics is
considering adopting open telemetry schemas for Prometheus' own metrics.
So, we discussed a little bit, I got green light to implement it, so I would really…
So my task is replace all the current instrumentation from Prometheus with auto-generated instrumentation.
So…
That's what I want to do, how to do it. I would love to discuss this with you, because you know more than I do about Weaver.
some pain points I had when…
Doing the demo for the talk.
The Jinja templates, are very hard.
Josh Suereth 00:04:48 Because I don't know Ginger?
Arthur Silva Sens 00:04:50 And I expect that people will have the same hard time as I did.
So I want to abstract this somehow.
Like… some… I don't know, I create a…
some automation, some CI, a GitHub action that runs and generates the instrumentation code instead of asking people to
Like, I don't want to commit the templates to the primitives repository. I want this to live somewhere else.
And have this automated somehow.
Do you see this… That's something doable.
Josh Suereth 00:05:29 So…
the… I think today we already have the ability for you to reference Jinja templates from another GitHub repo.
So one person can write the Jinja templates and everyone else can use it. Automating the Jinja templates, where, like, something auto-generates it,
I don't know, maybe LLMs can soon. We'd have to figure out, like, here's what I want it to look like, here's a definition, go write me a Jinja template.
But I, I don't know…
I don't know if we're going to be able to automate those,
otherwise. But I do think we should be able to reuse. Like, our idea is one person would write this for a language, for a thing, and then everyone can reuse it.
Arthur Silva Sens 00:06:14 Okay.
Josh Suereth 00:06:15 gotten there yet.
Arthur Silva Sens 00:06:16 That works for me, because I can… I can commit the templates to Prometheus SDKs, repositories, and then Prometheus will just use the templates from there.
Liudmila Molkova 00:06:27 It actually would be not a great idea to hide templates away.
Because people have interesting preferences when it comes to certain languages, and you actually want to expose them. And I don't think you want to generate a dramatic code in every language per video SDK, so it's an impossible task.
Arthur Silva Sens 00:06:54 Alright, I… I have a… like, a good feeling.
that people don't want to go through what I went through. Like, they don't want to write the templates, it's very hard.
Liudmila Molkova 00:07:05 They don't, but they do it not because they want to.
Arthur Silva Sens 00:07:10 Okay, AC.
Josh Suereth 00:07:11 I also think, I'll say this, there are people who will want to.
Like, there are people who, like, they have a coding style, it's different than the rest of the world for some reason, they force everyone to use it, they will go to great lengths to, like, update linters and code formatters, and there are people that do this.
Those are the people that'll touch the template, and we're happy to let them do template work. And if we provide a good default, that's my opinion, is we provide a good default, we're flexible enough that those people are happy, we should be good.
Do we have the links to how to reuse the… I know that that syntax was added. Is that in the code generation docs? I was just looking for a link to send Arthur here.
Laurent Querel 00:07:54 I will, provide this link.
Josh Suereth 00:07:57 Okay, thank you, Lauren.
Alright, so what was the next pain point, then?
Arthur Silva Sens 00:08:03 The next thing is,
like, Prometheus is a large codebase, a lot of code owners.
And, I want code owners to own a specific…
schemas. What I'm thinking is, I have one single schema that imports all the sub schemas. For example, Prometheus has a database, it has service discovery, it has a parser, text parser.
I want one schema for the parser, one schema for the database.
And one scheme for the service discovery, and one that imparts all.
Does that make sense? Or I'm tripping?
Josh Suereth 00:08:47 G.
you're not… I think we see that with the collector and the metadata and YAML files,
We… we don't allow… One schema to import subshemas today, because
we didn't have time to implement. I don't think it was on purpose that we say… right, Lauren? Like, the goal was to have multiple imports at some point?
We just don't.
Laurent Querel 00:09:12 Yes.
Josh Suereth 00:09:12 Because of… we can't deal with the problems of it, right?
Laurent Querel 00:09:16 Yes, I agree, that's what we, we had in mind at some point, but I'm not sure to fully understand what… because
The sub schema idea could be interpreted in many ways.
In fact, when you look at the semantic convention, there are multiple files, and they are merged together.
to form a global schema, that could be considered as multiple schemas that are combined together. So I'd like to better understand exactly what you mean by sub schemas.
Arthur Silva Sens 00:09:48 Yeah, I… It's just because the, like… Prometheus is a giant monolith.
And, for example, I am a co-owner of the OTLP ingestion part.
But I'm not a co-owner of all the rest.
Yeah. So, I want to be independent on my schemas, on the OTLP ingestion.
But I don't want to block others.
We're working on other, parts.
Laurent Querel 00:10:16 So, that's a question for, semantic function folks, like Lumila or Josh.
Don't you think that, the fact that we are already supporting multiple files
And they are already organized by the men.
We… there is nothing preventing us to have a custom registry that is, in fact, multiple files.
One per domain, like database, parser, and service discovery.
Liudmila Molkova 00:10:44 Yeah, so what Lauren is saying, that if you…
Happen to have all these files in the same repo, or if you can submodule or check out when you generate into the same folder structure.
Then it should be enough.
I'm kind of curious, is there a common part between different
parameters components that they would need to reuse. Like, the attribute names is not a concern, metrics are all individual, so it's multiple individual components, but you want to generate them
Together, is it?
Arthur Silva Sens 00:11:22 Yeah. Okay.
I can, I can see attributes repeating.
I don't have anything in mind right now, but I…
I have a feeling that attributes will repeat.
Liudmila Molkova 00:11:35 Okay, so maybe they should import semantic conventions and not invent… New common attributes?
Josh Suereth 00:11:43 Sorry, no.
Liudmila Molkova 00:11:44 But, I mean, it would be weird if Primedeus would start the new common… conventions.
No?
Arthur Silva Sens 00:11:55 I… I'm not a… I am not… I don't want to build a new convention. It's just metrics… replacing the already existing metrics.
With auto-generated instrumentation.
Josh Suereth 00:12:07 Yeah, so, like, Prometheus already has metric names and things, you already document and advertise them, right? You're just trying to, like, define them.
Arthur Silva Sens 00:12:14 Yes, yeah.
Yeah. Put them in the schema, create a structure.
Josh Suereth 00:12:18 Yeah, I put what semantic invention does in case this helps clarify, but basically, you have a single model directory that your build will use to generate code and Weaver and all that, right? And then you would have model component.
And that, you could have cod owners for a component.
that have commit rights to update their piece, but it's all…
Arthur Silva Sens 00:12:38 Yeah, I got it.
Josh Suereth 00:12:39 the, like, global repository of all the things for… that's what we do in semantic conventions now. It's…
Like I said, eventually, we… the collector, by the way, the OpenTelemetry collector, has the same problem as you, where they want to have, little definitions right next to the code that, it…
We don't support that yet, but we're…
it's something we should talk through and figure out what we can do. For now, this is the model I'd recommend, is have a directory where your YAML lives in.
Have sub-components in that that you can dole out ownership for, and one person owns, kind of, the build infrastructure of it, and then teams can own their particular metric piece.
Arthur Silva Sens 00:13:22 Yeah, I can work with that, no problems.
Liudmila Molkova 00:13:24 By the way, we could support individual components.
The interesting parts happen when we need to import things, but we could, in theory, support per-component code generation.
Josh Suereth 00:13:38 Yeah, yeah. What I'm saying is that import thing, where we have to import them all together into one
cohesive whole.
We're not ready to deal with the complexities of that yet, and we… our implementation today doesn't, so…
In case we end up with… basically, that's where you can have Deadly Diamond.
And we… We've avoided that.
So… Yeah, that's where it gets fun.
Arthur Silva Sens 00:14:10 I don't have any other pain points, to be honest, I think that's it.
Josh Suereth 00:14:14 Cool.
I actually think, by the way, this… when our feet 2 schema comes out.
Because of the way we modeled refinements.
It might be easier for us to deal with that.
Arthur Silva Sens 00:14:30 Oh, okay, what you said?
Josh Suereth 00:14:32 But that's a discussion for Lyudmila and Jeremy and Lawrence, about… we're making a V2 schema. The TLDR there is today, when you want to make a metric in Weaver, you know this, you write, like, groups.
and then you say ID, whatever, and then you say type is metric.
And then you have all the other junk, right?
In the future, instead of that, you're just gonna say metrics. You're gonna say name is this, you know, is it metric type? I think we just call it type, you know, histogram.
Whatever. Let's say counter.
And all the stuff goes right there, so it's just a lot less boilerplate and a lot more targeted, and your error messages are cleaner, because we can say, you have to provide a unit for a metric, you have to provide a description.
Arthur Silva Sens 00:15:25 Yeah.
So that made me think,
If I implement things in Prometes using V1, will I have a hard time to migrate to V2?
Josh Suereth 00:15:38 If we've done it right, no.
So, right now, this erases down to this?
And so, like, you should be able to reuse all the stuff you have. The…
I think the way this is going, and you can stay for the discussion because we're going to talk about V2, is that we'll have all the existing templates and Rego policies and stuff that people use on V1, and that will continue to work for a long time. And then we'll have an opt-in flag where you can move your templates to be on V2.
And V2 should be easier to write
the Jinja or the Rego 4. And if it's not, we've done something wrong.
Liudmila Molkova 00:16:22 And if… when it comes to the authoring, the semantic conventions themselves, you can already write in V2.
Josh Suereth 00:16:30 Yes, you can already create V2 files, yep.
Arthur Silva Sens 00:16:34 Altering, you mean that, like, renaming metrics?
Josh Suereth 00:16:39 No, when you write your YAML files, you can use V2. Where is that?
Liudmila Molkova 00:16:44 Syntax… You mean the… oh, schemas, right, yeah.
Josh Suereth 00:16:49 Yeah, so this documents the syntax for V2. So basically, if you put a version with a to string, and apologies, it has to be a frickin' string, I couldn't figure out how to make it be an integer. I'm still annoyed by this, I opened it up.
Fuck.
Arthur Silva Sens 00:17:04 I honestly don't care.
Josh Suereth 00:17:06 Yeah, if you say version 2, then suddenly you can start interacting with the version that's more raw. So, there you'll have, there's an attributes section, a metric section, an event section, an entity section, a span section, and imports.
As opposed to now it's just groups, right?
Arthur Silva Sens 00:17:24 Got it.
Josh Suereth 00:17:25 So yeah, if you wanted to try it, if you want to try it out, defining things today, this will get erased into groups, though.
So, like, it'll go back into groups in your template. So your template would be the same, and you'll have a conversion process to figure out. But in terms of defining metrics, I think it looks a bit better. Where's… do we have an example?
Thank you, you had one.
Liudmila Molkova 00:17:45 Yeah, there should be.
Josh Suereth 00:17:47 That's breakthrough…
Arthur Silva Sens 00:17:49 V1, V2, the difference is more relevant to the templates?
Liudmila Molkova 00:17:57 Both.
Josh Suereth 00:17:58 It'll be both.
Arthur Silva Sens 00:17:58 Okay.
Josh Suereth 00:17:59 Yeah. But you'll be able to opt-in separately, so you can make your definitions be V2 before you do your templates, and you can decide when you switch.
And I'm… what I'm working on right now, the next discussion, is going to be about automatically converting V1 model into V2 for templates.
Which is what this,
yeah, I have a giant PR, and it's… it's exciting. Anyway, this is what the syntax looks like, which I hope… I hope we all agree looks better, otherwise this is a huge waste of time.
But I think this is actually, like, gonna be much nicer for you and your ecosystem, right? You can just straight up define your metric, you're done. Yeah.
Liudmila Molkova 00:18:40 Yeah, actually, we are doing it not to improve the… this part, but to improve the resolve schema, the thing that happens. For Prometheus, it probably is most… will mostly be the same.
But for semantic conventions, the result schema today card kind of sucks.
Arthur Silva Sens 00:19:00 Honestly, just, like, the group… group stuff, it's kinda strange for us.
like, groups, group IDs, I don't really understand, I just do it because I copied from somewhere else. Like, having matrix arrays looks a lot simpler.
Josh Suereth 00:19:18 Yeah.
Yeah, I think that this is…
This is what we get for evolving, taking a schema that someone made and evolve. That's why it was groups. It was the first thing that someone thought that was a decent idea. Over time, we're like, okay, this isn't working, and…
You know, now we have to find a way to not break people and move.
Arthur Silva Sens 00:19:37 Yes.
Josh Suereth 00:19:38 Yeah.
Go ahead, Lauren.
Arthur Silva Sens 00:19:40 Anyway.
Laurent Querel 00:19:43 Oh, no, I wasn't, I was not saying anything.
Okay. I was just adding the explanation regarding the ability to import remote templates.
So the… right now, with the…
dash T dash dash templates parameter, you can basically specify a local folder.
a Git report, a Git repo URL.
or, a Git archive,
That's work like the, in fact, the parameter, dash dash for history.
explain that. It's…
Not well explained, right, in the documentation that we can use that for the templates, but that's the same model.
Arthur Silva Sens 00:20:29 I appreciate…
Josh Suereth 00:20:31 Should that be this, right?
Laurent Querel 00:20:34 Yeah, so in fact, behind the scenes, this parameter is using the same infrastructure that we are using for
importing registry.
And and for the registry, we already support the local folder, the…
And the values of the option I mentioned.
If you, if you, scroll down.
Use, yeah, dash dash registry, and then we have, in the description, we have local folder, git repo URL, and… or git archive URL.
And, and we have, when you are, specifying a Git repo URL or
a Git archive, you can specify between brackets.
A subfolder, so the bracket model… bracket means that you want to punt to a subfolder part of this repo.
Arthur Silva Sens 00:21:28 Got it. I… I'll try that out.
I, I already tried the registry,
registry flag, it worked as I expected. I never tried the templates, but if…
I can figure it out from here. I appreciate it.
Laurent Querel 00:21:44 That's exactly the same mechanism, so you will not be lost. If you can do that for the registry, that should work for the template.
Arthur Silva Sens 00:21:51 Cool, nice.
Josh Suereth 00:21:54 Cool.
Arthur Silva Sens 00:21:56 That is all from my side.
Josh Suereth 00:21:58 Awesome.
Hey, great talk, by the way, and excited to see this.
Arthur Silva Sens 00:22:03 Thank you.
Laurent Querel 00:22:04 They put it.
Josh Suereth 00:22:05 Cool.
Alright. I wanted to spend some time on V2 Resolve Schema, if everybody's cool with that. I already kind of did.
But are you ready to see where we are now with, resolution and things?
Liudmila Molkova 00:22:20 Yay!
Josh Suereth 00:22:21 Okay.
So basically I started updating for Attribute Group, and we now can get resolved schema
Oh, come on.
GitHub.
This page is taking too long to load, sorry about that. Okay.
Give me a sec.
I got the unicorn.
Alright, so for context, we're trying to get, a new registry resolve layout eventually.
What we have today… I added attribute group support, and I answered a bunch of,
Pool request, like, implementation concerns that we had.
So… oh, come on.
Maybe this PR's too big, and I should actually just browse the repo, but I think it's easier to see here. First, I added some more lineage tracking.
Because I need it to reverse engineer in V2.
Are you able to see this?
Laurent Querel 00:23:30 this…
Josh Suereth 00:23:31 Okay, so at the group level.
when… so, first of all, I already added lineage tracking for extends, so that we can actually track what extends, so we understand what's a refinement.
This now adds the includes group as well from the V2 syntax, so if you include a group, every group will understand what other group that it depends on.
in lineage.
Okay, so that's, that's, like, a big one.
let's move to… is this… this is WeaverForge, not ready to look at WeaverForge. So, in Weaver Resolve's schema, what we have now…
Is we have a registry.
And registry has attributes, attribute groups, registry URL, spans, metrics, and events. And then, this big… oh, entities.
So, it includes everything. The URL, the attributes, the attribute groups, the spans, the metrics, the traces.
Catalog is now no longer exposed publicly. Catalog, by the way, what I did for this, Laurent, you might appreciate this, is I made a efficient map lookup
So we don't have to row scan the whole table, to look for where an attribute is. You actually first look up all attributes of the same name, and then you row scan for,
the particular attribute that you are by size. So it's… there's still a bit of scanning there, but it's a bit more efficient. And this just makes that easy.
Okay. The other thing we have is we have now a refinements
resolution that has all of the span metric and event refinements. We can add more as we need more refinements,
This is a separate structure.
even though all of the references in here reference the registry. So in the registry, you have the attributes in order, and any attribute ref from refinements is
an attribute ref on this. The registry itself, though, like, events will have attribute refs that ref this attribute array, the groups will reference the attribute array, so it's a little bit weird in that the attributes are in one spot, and then you have, like, two spots where one references it, like before.
just calling that out, this is my proposed structure, then. So what we end up with in our V2 Resolves thing… is it… it's not under mod?
Thought I was… oh, I have to load diff, because this has the algorithm.
What we end up with for V2 resolved schema is we have a file format
We have a schema URL, We have the registry ID,
We have the registry itself that has all of the, like, signals, metrics, traces, attributes, and then we have refinements that you can engage with, where I… I'm actually considering refinements mandatory for semantic conventions, but optional for the rest of the world.
Because I think the simplistic way to use Weaver, you don't need them at all.
Okay.
I also… Yeah, go ahead.
Liudmila Molkova 00:26:48 I… I don't disagree. The… the… something, from Arthur's, side of the world, So…
from Prometia's side, they would actually interact with requirements. They only care about metric definition.
And the attributed references.
Josh Suereth 00:27:12 Why would they interact with refinement? Why are they making a refinement?
Or when would they make a refinement, I should say?
Liudmila Molkova 00:27:19 Oh, you no longer have the refi… the original implementation and refinement.
Josh Suereth 00:27:27 No, they would be in here, but you can interact just with the raw…
Liudmila Molkova 00:27:32 So we would tell them to go to registry, then metrics, and then…
ignore the rest. They don't care about, let's say, registry attributes, really.
Josh Suereth 00:27:43 I… I think so, yes. This is my opinion. But basically, they would just never define a refinement, so to them, they're just invisible, like, it doesn't…
Liudmila Molkova 00:27:51 Yeah.
Josh Suereth 00:27:52 Right. Sounds good.
Laurent Querel 00:27:53 questioned, boom.
Josh Suereth 00:27:54 Go ahead.
Laurent Querel 00:27:56 For one question, initially, we… so, we… in my opinion, we have two types of reserved schema.
For different purposes.
The one that is used by the Ginja template, the rigou, and so on.
Josh Suereth 00:28:16 That is beautiful.
Laurent Querel 00:28:16 Very soon.
Yeah. Yeah. So this one is the one where we, we,
that I will qualify this one like the previous shable.
Reserve schema.
Josh Suereth 00:28:27 Yes.
Laurent Querel 00:28:28 the one that we will, at some point, be able to import, that is, fully versioned and archived into Git repos and things like that.
Josh Suereth 00:28:37 Yes. Okay.
Laurent Querel 00:28:38 And we have another one, which is also reserved schema, but I will qualify it fully reserved schema, where there is no reference at all, just to ease the consumption of it.
into Jinja templates and other things like that, right?
Josh Suereth 00:28:54 Yes, let's give these things names, because…
Laurent Querel 00:28:57 Yeah, I think that would be.
Josh Suereth 00:28:59 Same thing, and you used to call the one the template schema and the other one the resolve schema, but basically what we have is, we have the, the definition of, like, a file schema, like, how people write their YAML.
Yeah, they'll talk.
Laurent Querel 00:29:15 Yeah.
Josh Suereth 00:29:17 We have post-resolution, where we have the giant schema. This is the resolved schema that you're looking at now. This is not what goes to a template.
This is an optimized schema to compress that we could publish. Yeah. Okay, that's what this is. That's as far as I've gotten with this. I have not done.
Laurent Querel 00:29:35 Thank you.
Josh Suereth 00:29:36 But I want to call this one the Resolve schema, because it comes after Weaver Resolver.
Okay. And this one I want to call the forge schema.
Because it comes for… it's what you send through the Weaver Forge components.
Laurent Querel 00:29:50 Yeah.
Josh Suereth 00:29:51 That's okay, just for nomenclature, because it… I confused myself.
Laurent Querel 00:29:56 Yeah.
Josh Suereth 00:29:57 I… I want names for these things, if possible.
Laurent Querel 00:30:00 That works for me.
Josh Suereth 00:30:01 Okay.
Liudmila Molkova 00:30:02 Today I learned. Okay, can we expose just one to the end users?
Do end users care about two flavors of results schema?
Josh Suereth 00:30:15 I… This is a question of, if you look at
If you look at what we send to Forge.
That schema has a whole bunch of duplicate information. And so if we actually publish this on the web, you're gonna have ginormous files.
Laurent Querel 00:30:30 Yeah, that would be problematic.
Josh Suereth 00:30:32 So this is basically a compressed version of this for publishing and consuming. It's like a… it's like a partial… mostly resolved schema that you can then turn into the forge schema to do rendering where everything is… all the links are connected, right?
Liudmila Molkova 00:30:48 I see, okay.
Laurent Querel 00:30:49 Most of the… most of the people, I think, if you, if you…
If you look at the consumption of those schemas, The forge and the reserve.
Most of the people will, in fact, consume the forge.
Josh Suereth 00:31:04 Yes.
Laurent Querel 00:31:05 But they will import… they will import the result. They will not necessarily look inside the result.
Josh Suereth 00:31:12 Yeah.
Laurent Querel 00:31:12 But they will, in fact, import the results. So that's why the two are important, in my opinion.
Liudmila Molkova 00:31:20 I'll… I'll take a look, I'll try to wrap my hand around it and maybe document it, because…
Yeah, it's… yeah. I didn't realize it until today.
Josh Suereth 00:31:30 we need to document it. It's also a pain in the ass, because basically what I've had to do, or what I'm trying to do, is, we have…
the version schema that we convert for input, right? Then we have post-resolve, and that's where we… the resolution happens in V1, and I'm trying to reverse engineer the V2 resolution stage.
Then after that, we define what goes into Forge, where we map from this optimized version into the Forge version.
Okay, so, like, this already exists in the CL, so you might, you might have heard about PR, so you might have already seen that.
this is where all of the guts happen, is try from, of basically take the V1 version, get V2,
that's… this is the public-facing thing I want to have everyone interact with for V1 to V2. We basically take everything, fire it through, we have a resolve, get resolve schema.
This is what we would publish.
Although it's possible that if we… we actually want to publish multiple files, or maybe we split things up so that it's easier to consume, I'm a bit nervous about how big this thing is gonna get with both of these here.
But that's… Anyway, we, we can…
Laurent Querel 00:32:51 Okay, can you, can you, precise that a little bit? I'm not sure to follow the… why you are now this…
Josh Suereth 00:32:59 If you look at the registry now,
this file. It was big enough that in Visual Studio Code, you know how you can, like, minimize text blocks?
The file was so large that it stopped allowing me to minimize text blocks.
Laurent Querel 00:33:16 Okay.
Josh Suereth 00:33:17 on sections, because it ran out of, like, space and just gives up after a certain size. So, I think this is pretty big, and that's for just a test example semantic convention repo, not semantic conventions itself.
So, I think inside of Rust, resolving in this way is fine, but I think when we actually write files and consume them.
we need a whole design around that, and I think that we should have, like, a header, and then maybe pieces of this get put in different spots.
you can reverse engineer it, you know, like, I still want to sort that out. But the… what I have now, this is what it looks like, and…
let's talk a little bit about, in Resolved Registry.
we have, oh, that's Forge. Yeah, let's not talk about Forge. Inside of here.
I added the include groups, two signals.
So, I'm doing lineage tracking, right?
And so, if we have public attribute groups, the theory here is
Attribute refs are every single attribute you use.
No matter what.
Including all the ones in the include group.
This is just leaving you a breadcrumb trail.
to reverse engineer.
what public groups attributes are part of, if you want to co-gend public attribute groups. I'm considering attribute groups an opt-in feature.
of Weaver CodeGen as well, where we might not use it initially, we might add it later, but yeah. What this does is all attribute groups are included here, only public ones.
And this is true for refinements and for signals, so you can see what public attribute groups you have. Now, what's more fun
If you want to see the real pain, we had to…
We have a recursive algorithm to grab these attribute groups, because we actually have to… if you're a group that extends a group, that extends a group, that extends a group, you have to actually follow the include groups all the way down that path.
to know what public attribute groups you use. So it's actually a rather expensive bit of tracking.
That's fine, I just… it works, it's tested, that's where things stand. I just wanted to run you by, like, the current shape of things where they are today.
So this is what the Resolve schema looks like. Now, going into Weaver Forge.
So now we're going to talk about WeaverForge, and what templates…
Liudmila Molkova 00:35:59 A quick question, do we actually need it in?
the group includes in the results schema, or in the Weaver words schema?
Probably it's Weaver Forge.
Josh Suereth 00:36:13 Well, I… we need it somewhere. I probably need to add lineage tracking, if we're not going to include it directly as a thing in Resolve Schema, because otherwise it's completely erased. You lose it. You have no idea how to reconstruct it.
Liudmila Molkova 00:36:29 Yeah, like, the resolved schema is the schema definition, and lineage is debug information, there.
Josh Suereth 00:36:36 There's no lineage in V2 yet. I haven't figured out lineage yet.
Liudmila Molkova 00:36:40 Yeah, so what I'm saying, it does not need to be in the result, the published resolved schema.
Josh Suereth 00:36:46 the lineage?
Liudmila Molkova 00:36:47 Yeah.
Josh Suereth 00:36:48 how will I use that resolve schema and figure out attribute groups without lineage, if lineage is the only way I know about it?
Liudmila Molkova 00:36:56 You would be using them in the… when you're interacting with templates?
Josh Suereth 00:37:01 How do I get them to the template? Again, remember, I only have access to this schema, so how do I get them to the template at all?
Laurent Querel 00:37:07 Yeah.
Liudmila Molkova 00:37:07 I see.
Laurent Querel 00:37:08 the way that Lumina, the modern model for that… so let's say we have the semantic conversion file, then we generate the result.
And from this result, which is a more optimized version of the Forge, the forge is based on the pre-use one.
So, the forge, if we want to expose lineage in the forge, we need to get it into this reserved. I think what I did initially was an option where
You can generate the resolved with or without the lineage, and we enable automatically the lineage when the reserved schema is created for the purpose of the forged version.
Liudmila Molkova 00:37:53 Yeah, so what I'm saying is that you don't need to serialize it, so when somebody resolves.
Laurent Querel 00:37:58 Yes.
Liudmila Molkova 00:37:59 It can be in the REST code, it doesn't have to be in YAML.
And I remember when I was playing with,
schema V2… sorry, sorry, with schema publishing for the current resolved, schema lineage is a huge part of it, so if we remove lineage, the file size will also significantly go down.
Laurent Querel 00:38:18 Yeah, there is an option already in the existing code to do that. I don't know if Josh maintained it, but definitely, that was, yeah, when the option to publish was taking this parameter and optionally, you can generate the lineage. I think we should keep this kind of approach.
Josh Suereth 00:38:39 Agreed. The thing… the thing that we need to do is you cannot generate a V2 schema without lineage right now.
So, I preserved it, it's just what happens is if you use it, V2 schema breaks.
Liudmila Molkova 00:38:55 Can we just add not serialized annotation on the… Lineage?
Oh, it's not there. Once we add it there, we can add it with…
Josh Suereth 00:39:06 Yeah.
Liudmila Molkova 00:39:07 email sterilization.
Josh Suereth 00:39:08 Right, so we don't have, like… we need to define lineage for, for this at some point. So, like, this will need lineage of some fashion.
And that lineage will have to be, like, on a metric or whatever. But the… one of the things that, we'll have to sort out what lineage actually is. With the way we're doing refs now, right, requirement level no longer has to be in lineage.
So, attribute lineage is gonna be a little bit simpler. I think that's good.
And,
should this actually be a lineage thing, or should this be raw? The reason it's raw right now is because the only way you can interact with this
today, at all, in Forge, as if it exists. So, I don't think we can allow it to be erased.
Liudmila Molkova 00:39:58 Okay, yeah, that's…
Laurent Querel 00:40:01 I'm not sure to follow, Josh. So, I think I… you mentioned two things. Include groups.
And all the information related to, lineage.
in my opinion, should end up into a section specific to lineage.
Otherwise, why don't you think that we could
So the published version, so what you named the reserved registry right now?
Josh Suereth 00:40:32 Yeah.
Laurent Querel 00:40:34 I don't see… I don't think there is nothing preventing not to generate the input groups when the outcome of this reserve registry is not for Forge. If it's just for publishing on a website.
Is there anything preventing to do that? I don't think so.
Josh Suereth 00:40:53 Include groups are completely erased, unless we put it here. So, let's assume lineage is optional.
I have no way to know what include groups this metric actually used. I could guess, but I could also be wrong.
Because… because…
Laurent Querel 00:41:13 I can reference a group, or I can reference the attributes individually.
Josh Suereth 00:41:17 If I reference the group, that implies I care about the public group, and I want people to engage with that public group.
But if I reference the attributes individually, I don't want you to have to engage with the group if I didn't intend that.
So, that's the weirdness here, of, like, we have to preserve the fact the group was used.
And we shouldn't reverse engineer, oh, what groups are applicable here? Let's do a reverse lookup of, you have attribute XYZ, and this group has XYZ, so obviously you used this group. No. Like, I don't think that's the right thing to do here. So we have to remember what groups, public groups, were used.
which is why I'm doing it in the resolution phase. I'm using lineage from V1 to infer this, but we need this to engage with groups independently.
So, this can't be in lineage. This, specifically this. I'm not saying we don't have lineage, I'm saying specifically this field needs to be there so you can engage with public groups, regardless of whether you have lineage.
Laurent Querel 00:42:19 Okay, maybe there is something I'm missing, because…
For Ford, I totally understand the rationale.
For a publishable, registry, We don't care about those input groups, right?
Josh Suereth 00:42:35 No, we… they're gonna… they're public, they're gonna be in the… they're in the registry.
So if we look at the published registry, we have only the public attribute groups. There are private ones that get erased, that's fine, but the public ones are there, and we need to know which ones were used.
Laurent Querel 00:42:51 But we have a list of attributes reference. If you go back to the matrix, we have this list of attributes, right?
Josh Suereth 00:42:59 We have a list of ashes.
Laurent Querel 00:43:00 attributes. This one is complete. There is no… nothing missing there.
Josh Suereth 00:43:05 there's nothing missing there, but how do I know that a public group was used to fill out.
Laurent Querel 00:43:08 I don't care.
Josh Suereth 00:43:10 People don't care? Like, the whole reason for a public group is that you care.
Otherwise, it would be a private group.
Liudmila Molkova 00:43:20 the… each attribute has lineage, and it knows that it comes from a public group. It's hard.
Josh Suereth 00:43:28 We don't have lineage. We don't have lineage.
Liudmila Molkova 00:43:30 We will.
Josh Suereth 00:43:31 No, no, no. Someone, someone turned off lineage. Lineage is gone.
Liudmila Molkova 00:43:35 So, if they turn it off, they don't care.
Josh Suereth 00:43:41 Why do we have public attribute groups, then?
But, okay.
Liudmila Molkova 00:43:45 Let's go back to what is the reason for public attribute groups at all?
Josh Suereth 00:43:50 maybe we just don't need them, but that's why… this is what I'm getting into. Let's… I'm assuming that if I say I have an attribute group.
I forget how it works. Is it an ID?
Liudmila Molkova 00:44:00 It is an ID, I think, yeah.
Josh Suereth 00:44:03 And then there's, attributes, right? And I would say ref…
you know, X dot Y, something like this. And then I have a metric.
called ID bar, and I would have, you know, attributes…
And I would have rough groups.
So the idea would be, in CodeGen.
I would have something like struct, you know, foo attributes. I'm gonna use… I'm gonna use Rust here, I hope you don't mind.
That has, foo of type, you know, attribute type.
And then I would have, you know, new function, record… Actually, let's just say structs.
Bar metric.
It's not… bar its name.
I'll try to be consistent.
struct barometric, and then I would have impulse, barometric…
And I would say, you know, Record…
I don't know if it's gonna be mute or not, I don't care, but the idea here would be, you could say foo, foo attributes, so that in my code gen, I'm literally…
I'm literally interacting with a public group. Like, the whole idea behind a public attribute group
is that somehow I'm going to interact with it, and it's important that I do.
Otherwise…
Liudmila Molkova 00:45:36 Yeah.
Josh Suereth 00:45:37 Can we just get rid of them?
Liudmila Molkova 00:45:39 So, the reason we have them is because we have some groups that we document. We never reference them on signals, like thread properties.
Or, loud event properties. We don't… we don't defy a signal that references them. It's temporary, I'm sure we will.
But we need them to document stuff.
We don't need them to be referenced on signals just yet.
And we don't know how this would look like. But, the moment we…
Josh Suereth 00:46:17 Needed.
Liudmila Molkova 00:46:19 Then we will need a weight.
When you interact with resolved schema to know that this group is a group, and not…
Just a regular attribute.
Josh Suereth 00:46:35 Okay.
So maybe the issue I have, then, is we don't need…
Ref group and public attributes shouldn't be used together?
Rev Group.
Liudmila Molkova 00:46:54 And…
Josh Suereth 00:46:55 Like, I get the need for code or thread, right? There's a set of attributes that are not associated to a signal.
that don't have a name or definition that we want to be able to attach to signals. They're like.
Attachments, if you will.
That's what you want a public attribute group to be.
Liudmila Molkova 00:47:12 Right, so then RevGroup can only reference internal groups, and essentially this is the roadblock we put, because we don't… we didn't design how the public group interaction would look like.
Josh Suereth 00:47:24 That… that's… yeah, that's what I'm running into, is I actually think we need to sort this out.
Liudmila Molkova 00:47:31 So let's put the block. Let's say rev group only applies to internal groups for… Now.
Josh Suereth 00:47:37 I… I can… I think…
Yeah, I can do that, and I can remove all of the group stuff I just did, and just ignore… like, I can have public attribute groups get shown.
But actually, I want to call this something different, then.
Right, like, if a private attribute group is just a grouping mechanism for inclusion in the list of attributes, that's great.
My opinion was that public you need to engage with in some way, or you need to, like, even if we generate, like, metric record rules, we'd have to have the ability to throw a bunch of extra crap in for, like, spans and stuff.
I… I think the way that you want to use these
There needs to be a term for this.
that denotes what we're doing. Of, like, these are attributes that could attach to any signal.
Jeremy Blythe 00:48:31 On the, sort of, journey that… We're on…
In our comp- in my company.
It's very, very common. In fact, it's the most common case that we've documented the attributes, and that we're building the signals on the fly, so what you're describing is a loose.
loose attributes. I'd describe them are like loose signals that use strongly typed attributes.
It's kind of the other way around. I don't know if that's…
So I think it is a common use case that you want to have a library of attributes that you're going to use in all sorts of different ways.
And then we… everybody wants to get to a point, like, where all the signals are really nicely, strongly typed, and, like, that isn't that… that's an amazing world.
But it's a journey to get there, I think.
Josh Suereth 00:49:25 Yeah, what you're implying is that these would be the most to use things for CodeGen today.
Jeremy Blythe 00:49:31 Right, and if you look at all of the SEMCON libraries today.
They just make… they make lists of constants for the attributes.
Josh Suereth 00:49:40 Right, they're just doing that, yeah.
Jeremy Blythe 00:49:42 Yeah.
Liudmila Molkova 00:49:43 Unfortunately.
Jeremy Blythe 00:49:44 And that's what the world is using right now. And so if we then go like, oh, you don't get access to these attributes anymore.
You have to have all these signals, and that's, like…
Josh Suereth 00:49:52 Well, no, you get access to attributes, you just don't get access to the groups.
Jeremy Blythe 00:49:56 Right.
Josh Suereth 00:49:57 But I… but I… I think I see what you're saying. I mean, the…
The reality is, if you want access to the groups programmatically, it hurts… like, the question I would have on this journey, Jeremy, is like, how do we get to generating here?
If we add this in the middle, and we don't have a way to interact, or, like, bridge the gap, we're never gonna make it. And we're actually gonna put roadblocks in the way to prevent us from getting there.
Jeremy Blythe 00:50:28 Y-you- are you… Are you saying we need something to kind of…
force people in a better direction? Is that what we're trying to…
Josh Suereth 00:50:38 I think we need to understand the end state.
Jeremy Blythe 00:50:41 Yeah.
Josh Suereth 00:50:42 That's what I want to know. Like, I'm happy to have public attributes if we know where they're going. This is what I thought we were going towards, and the reason I'm designing things is because we can never get here if we don't remember public attribute groups.
like this. To know that when we generate code for bar metric, we have to interact with the attribute group instead of the pure attributes.
Liudmila Molkova 00:51:12 My feeling there, that we are just exploring what the public groups are, right? And maybe it's not that you record the metric, it's maybe that you annotate a span with code attributes, like today we do record exception. Record exception is actually an example of public group.
That we are saying, okay, this is an extra you do on top of.
And… It's a different type of cogeneration.
Like, we never tried building it.
So, all this to say, we just don't know how public groups will be used, but they will be used.
Josh Suereth 00:51:59 Well, it might mean we don't know the design space either.
Liudmila Molkova 00:52:03 Maybe, yes.
Josh Suereth 00:52:04 Of, like, options and what we can do.
Liudmila Molkova 00:52:07 All we know about them so far, that they should be documented.
Josh Suereth 00:52:12 Yeah.
Liudmila Molkova 00:52:18 And definitely there is a future where there will be cogent, and we will need to know about them.
Josh Suereth 00:52:27 Alright, I'll have a think about what's… what decisions we have to make now and can't change in the future, and what decisions that we can fix later with resolution.
But I think I am going to gut a lot of the tracking.
Of attribute group, for now.
Until we know what they're used for. I also think, like, in terms of, like, a code gen capability and attribute groups and that sort of thing,
It would be nice to know what these attributes can and cannot attach to.
Like, I can write this on a span, I can write this on an event, I can't write it on a metric.
Its have to be complete.
So…
Jeremy Blythe 00:53:13 Why… why… why do we want to impose that restriction?
Josh Suereth 00:53:19 If somebody adds a bunch of labels to a metrics, they're likely to break all their observability.
So, if we were to code gen metrics that don't limit exactly the set of attributes that are allowed, you can easily break all your metrics. I have a doc about that, if you want to see that, for, like, compatibility things.
Jeremy Blythe 00:53:37 Oh, sorry, I thought you meant that when you define an attribute.
You're going to say, this attribute can only be used on spans.
Josh Suereth 00:53:45 Oh, oh, no, no, no, I mean, actually.
Jeremy Blythe 00:53:46 groups.
Josh Suereth 00:53:47 Specifically, yeah.
Jeremy Blythe 00:53:48 Sorry, alright.
Josh Suereth 00:53:48 And I was thinking for attribute groups, like, an attribute group could be… like, if we're defining public attribute groups like code, that'd be cool. This is a set of attributes that can apply to spans and logs.
Or this is an attribute group that applies to entities.
Right? Like, I'm trying to understand…
that use case. I still think the public attribute group use case, like the code use case and thread use case, are… there is something that we have not modeled correctly.
Or not modeled, I should say.
In our system that leads to these.
Or there's a hole in our model that's going to cause lots of friction going forward, unless we sort out the details of it.
So, I understand we're just documenting them for now. It's more, I'm thinking about the long-term health of our model.
And if our model can't account for these things.
Effectively, or understand the relationship between stuff.
you know, how do I do CodeGen?
So…
Has anyone tried to actually write code gen for metrics and spans and logs that, like, actually, you know, uses structured
Stuff to fill out the… Data.
When you did that, did you leave room for attribute groups, like code, or like thread?
Laurent Querel 00:55:14 No, not for the conjun.
For me, the attribute groups, if they matter, they matter for documentation generation.
But for Kojin,
We basically have a strict representing a collection of attributes that are either required, and we have another strip for
All the optionals.
And when we, report a metric.
we take, one or two of those truths, and that's it. There is no concept of a group of attributes, because
For me, they don't really matter at this level, but .
Josh Suereth 00:55:55 Well, yeah, well, how…
Laurent Querel 00:55:56 Sonimi.
Josh Suereth 00:55:57 How do they get added, then?
Right? If our coaching doesn't allow them to be added, how do they get onto the telemetry?
Laurent Querel 00:56:05 When you open your metric description, you have this list of attributes. At this point, you don't care about a trivial group.
You just have a list of attributes that are assigned or attached to this metric, and that's it.
Josh Suereth 00:56:17 Right, they'd be referenced. The ones that we're talking about specifically, though, Laurent, are never referenced in anything.
like, thread, and code, and exception, those aren't actually referenced directly on any specific span.
Laurent Querel 00:56:31 Yeah, but it's a problem of resolution. I understand that. So you have, like, an alias to represent multiple attributes.
That's the… what I… my understanding of this public attribute group, that's, like, an alias of multiple attributes.
Josh Suereth 00:56:49 Yeah.
Laurent Querel 00:56:50 When we are talking about Kojen, why do you care about that?
Josh Suereth 00:56:55 Well, what I've…
Laurent Querel 00:56:56 Since you kill those, it's…
Josh Suereth 00:56:57 What I'm saying, Lawrence, is, like, this is what we're talking about. Let's say we have a spend, right?
Laurent Querel 00:57:03 Yeah.
Josh Suereth 00:57:03 This doesn't exist. There's just another set of attributes, you know, ref.x.z.
This can still… because this is public, it could still go on the span at any point in time.
That is the model we have in semantic conventions today. There are public attribute groups that could be included on any span or any event.
Laurent Querel 00:57:26 Yep.
Josh Suereth 00:57:27 That are not directly referenced in the model.
Ever.
How does that work?
How do we make that work? With CodeGen, with what we're building?
Laurent Querel 00:57:47 I must be slow this morning, I'm not sure to… So, I'm talking about,
A feedback on what exists today, not what we are designing now.
on what exists today, I don't see the problem.
We, we just take referenceions with Repeat Group, they are combined together, and we formed.
Josh Suereth 00:58:08 No, no, we're never…
Laurent Querel 00:58:10 in Lizable.
Josh Suereth 00:58:10 We never make a reference to the group. We're not gonna do that. We don't do that today, we will not do that in the future.
There will not be a rough group here, ever.
Laurent Querel 00:58:18 But we ex… I'm sorry, but, we… we are able to extend,
To extend… in a metric, we are able to extend an attribute group, and so we inherit the… all the attributes from it, right?
Josh Suereth 00:58:31 I guess this could be a question for Lyudmila, for, like, the thread… for thread attributes, right? Are you gonna add those as ref groups to every single span in semantic conventions?
Liudmila Molkova 00:58:39 No, but we might have a special definition of, I don't know, messaging plus cloud event spend, and then we wouldn't maybe include all the cloud reference properties attributes on some span. Maybe.
Right?
Josh Suereth 00:58:55 Well, that's what I'm saying, it's a maybe thing, right? Like, that's what I want to understand, is what will that look like?
what's the plan there? How are we planning to deal with those?
Liudmila Molkova 00:59:05 So, these…
Josh Suereth 00:59:07 Here's the thing, like, what you're saying is, I would make a new span refinement.
That would include the public attribute group, And the other spent, right?
In which case, why do I need to… I don't need to remember attribute group at all.
Right? I might need it for docs, but I kind of don't, because the refinement could be documented.
Liudmila Molkova 00:59:32 Yeah, so the way… I see it in general case.
Ugh.
Imagine… a helper.
that…
says, annotate this span or event with code details, and it takes code. It's not the span definition, it's an extra annotation on the span.
Extension method that adds some structured foo onto that span.
This is how it could work, and then…
This pan refinement probably would never…
Care about those attributes, they are…
Extra, and if you define that.
Okay, so if you define something that takes exception.
You would still want to say, okay.
Generate this event, or sorry, create this event, and there is an exception.
Comma, and then the other properties of that thing.
Yep.
Josh Suereth 01:00:39 Yeah, that's fine with me, but that's where you would have refgroup here, right?
It's things like thread, like, when we talk about stuff like thread, or code.
Are we going to explicitly put this in the spans where it can be used, or not? That's kind of what I want to know. If we're not going to, that means that attribute group is this weird thing in the model that these could be added to any possible span, or any possible event.
Liudmila Molkova 01:01:07 So we, I think we can limit the problem space today to not including public groups.
Either not including them at all, on signals, or including them as any other group.
Like, keep ignoring… yeah, we have to…
Josh Suereth 01:01:32 We have to drop. I want to continue this, because I just… I…
I don't see how this hangs together, or, like, what attribute group means. I think we need to really define
what these is, and how you… how you interact with them, and what's expected. Like, how do I interact with it in CodeGen? How do I interact with it in OpenTelemetry, the data model? You know, like, how does Weaver… how does Weaver, actually enforce attribute groups?
In live check?
If you don't annotate it to the signal, and we're using the signal to look up what attributes are expected, and these things just show up on a span or an event.
I have to know that that's okay somehow, for LiveCheck to do a policy. Otherwise, I'm going to flag all these as, hey, I don't know what the hell these are.
We have to have some way of tying this knot to know that they're okay. Or to say, here's a bunch of attribute groups, these could be anywhere, and LiveCheck understands, cool, I have to check any possible attribute group to see if these things show up, right? Like, how are we going to make this work in our ecosystem we're building? I still can't answer that question.
Liudmila Molkova 01:02:39 So, I think for this discussion, do you want to solve this giant design problem before we address resolved schema? Can we address resolved schema and let the giant discussion evolve, take its own course?
Josh Suereth 01:02:54 So, what I'm asking is, do… I would prefer to just not allow attribute groups to start with, and yeah, that's gonna kill…
Liudmila Molkova 01:03:03 click.
Josh Suereth 01:03:03 That's gonna kill Except we have public attribute groups. Kill them. For now.
Liudmila Molkova 01:03:08 And, okay.
Josh Suereth 01:03:10 Even in documentation.
Yeah.
Liudmila Molkova 01:03:16 Okay.
Let's try, let's see.
Josh Suereth 01:03:18 Okay.
Liudmila Molkova 01:03:19 Alright.
Josh Suereth 01:03:20 I'll see you.
Laurent Querel 01:03:22 Thank you, buddy.
