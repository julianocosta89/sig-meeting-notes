SIG: Semantic Convention Tooling
Date: 2025-07-03
Duration: 69 minutes
============================================================

## Zoom Recording Transcript

Josh Suereth 00:00:13 I can't hear you once can gonna try again.
Laurent Quérel 00:01:14 Can you hear me now?
Josh Suereth 00:01:18 Yeah, I can hear you now. Cool.
Laurent Quérel 00:01:21 It will.
Strange! I can't tell you.
Josh Suereth 00:01:31 You can't hear me at all.
I can hear you.
It says I'm talking.
Liudmila Molkova 00:01:51 Hi folks.
Josh Suereth 00:01:53 Hey? How's it going.
Liudmila Molkova 00:01:54 Good! How are you? Thanks for setting it up.
Josh Suereth 00:02:00 No worries. I'm just looking at your your proposal here in problems.
Liudmila Molkova 00:02:06 Yeah, I didn't do anything smart. I just generated with what we have. And yeah.
I did another pass. I have a Pr to remove all the optional properties. It reduces the size by 30% of the resolved schema.
Josh Suereth 00:02:26 Oh! By not filling them out to null .
Nice.
That's fun.
Yeah.
okay.
Oh, I'm not sharing the tab I'm looking at. I'm just looking at your files changed and things.
Laurent Quérel 00:02:56 Can you hear me? Now?
Yeah, yeah, please.
Liudmila Molkova 00:03:06 You're still not sharing, Josh. If you wanted to start sharing.
Josh Suereth 00:03:10 I mean I can. I just I'm it. It'll it might make everyone seesack if I show what I'm looking at now.
Liudmila Molkova 00:03:17 Okay.
Josh Suereth 00:03:18 You made a dev and a normal schema.
Liudmila Molkova 00:03:23 Right, and I was thinking we should do the same for diff. This is where I got stuck.
Yeah, I'm thinking there are big things we can discuss, and they are somewhat separate.
The manifest right? What we want to see in manifest, but it's probably not so big and trivial. Laurent has a proposal, I believe the other part I wish we could touch upon is, hey? We're changing schema, right? We we need to change schema.
So can we design how it looks like and clean up all the stuff.
Josh Suereth 00:04:14 Yeah.
Cool.
I'm just copying what you have over here.
okay.
And did I put these right? Lots of meaningless? No.
Liudmila Molkova 00:04:46 So I think everything except 1st one is is a small fix in this set of problems.
Laurent Quérel 00:04:59 Yeah.
it's an annotation super easy to fix lineage. You can already remove it if you want. There is a flag for it.
Oh.
Liudmila Molkova 00:05:09 I'm doing. Actually, I'm doing the register generate. Why? Because I need to massage, anyway.
Laurent Quérel 00:05:20 Oh!
Liudmila Molkova 00:05:23 And I need to sort.
I think, that the resolve should sort, but it doesn't.
But anyway, also, resolve cannot filter unstable.
So I'm doing some massaging anyway. So I can remove lineage, do we?
The question is, do we need it like if we need it, let's keep it. But do we need it?
Laurent Quérel 00:05:47 I think for that, that depend for what? If it's if you are talking about I think there are situations where the lineage matter.
So, for example, if you want to expose the the reserve registry to an enterprise at the caterogy.
definitely read the lineage matter for this specific case.
if you just want to use the reserve registry to do some. Let's say schema transformation like like the schema processor.
that doesn't really matter. In that case.
if you want to do some filtering stuff on registry, I think registry matter. So, for example, the what telecat is doing with the the Ui that they could plug on top of Weaver registry will matter. Lineage will matter. In that case.
Josh Suereth 00:06:49 Because that will add
Laurent Quérel 00:06:51 70 convention order to under, to understand from where it's why the attribute or signal is coming, and how that has been transformed with the values.
overriding rules and external and blah! Blah!
So that's why it's a flag. It's a it's a flag, so you can. You can generate it or not.
Liudmila Molkova 00:07:13 I understand. So we are going to publish it for the world, right?
And we need. There are scenarios where it's important.
There are scenarios, where? Where? It's not.
where do we put the line? And probably if we don't provide it, then someone can use the manifest to go figure out which registry to resolve and resolve it to get all the lineage information for their custom case.
Josh Suereth 00:07:43 Yeah, it's it's kind of a debugging feature.
But I I'd be fine if we put it somewhere to the side. But I I would kind of like it to be default. So it doesn't have to be recalculated repeatedly. I think that there's danger in trying to re-resolve and assume that you can debug from re-resolving it might be safe in this case. I just I know that in the past, when I've tried to do that, we've run into problems right? I don't resolution engines where you have like dependencies, you're resolving and picking particular dependencies. If you don't find a way to like lock them down and make them unimpotent.
So it's I. I'm more of a fan of recording the information somewhere.
maybe not in the same file as the rest of the stuff like maybe we should have lineage get written to when we publish files, lineage can be consumed separately from something else. Right?
Laurent Quérel 00:08:44 That could be the an option. I agree.
Another thing is to consider is because there is one feedback about the size.
So I I guess what you are using. Julia is not really the result.
there is, in fact, in Weaver for for values, reason to version of the reserve registry.
There is one that is consumed by Jq. And and Ginger or Jq. And the police engine.
It's what what I named the materialized reserved schema materialized meaning that we we don't care about the size we care about. The ease of Everything is is, let's say, fully materialized.
Now, the the resource schema as it was defined in one of the documents that could be published self contained.
This one is slightly more optimized in terms of size because there is this concept of catalog inside the reserve schema.
And so basically, the catalog is a collection of unique attributes where the the full definition is defined and every signal part of the the reserve registry reference internally to this catalog in fact, the resolution process is producing directly that there is a deduplication of attributes. Because if you imagine that you have even, for example, for the semantic convention, the open telemetry one.
we have many, many times the same attributes here used again and again.
So if we materialize everything that will that will end up to a huge amount of duplication.
and that's, in my opinion, not necessarily the best approach. If we want to package and publish something, because the size of this thing will matter. So I guess the the screen gigabytes that you mentioned into one of your comments.
I think, was the materialized version, and not the the the resolved one with the the catalog. But.
Liudmila Molkova 00:11:12 Yeah. So maybe we can park this. I think we can shrink it down and optimize it. It's not that important. At least, I think we have bigger problems to discuss.
Laurent Quérel 00:11:23 I agree. But it's we were talking about lineage.
Okay, but I'm saying, and and you were saying that it's taking volume.
I'm just reacting to that saying that it's not so big. If you have this concept of catalog and the duplication.
Liudmila Molkova 00:11:44 Okay. So I don't think 3 MB is a big deal. If we need all this information, I'm more curious what information we need, and then we will figure out how to publish it.
Josh Suereth 00:11:54 Yeah, I put a link to where we use it in semantic conventions. But we're using it to do cross linking for attributes to the group that they came from.
Hey!
There are other things that we can use lineage for. I do think that we should take an I. I let's open a ticket. Let's do an optimization pass. Let's see what we need and make sure that we have the right use cases. But the there's a debugging use case. And then there's just a general like Ui rendering use case of of making sure we can link cross link docs. Right? So I think we need to have something for that. We can optimize it.
I also feel like to what you were saying, Lawrence. Imagine if the registry were separate documents. Imagine if we had a lineage registry separate from, like the resolve schema registry. So if I'm doing code, Gen. And I don't need lineage, I can consume that document right and get all the things I need. And there's a separate document I can also consume to get lineage and pull in together. That's another option to think about.
Laurent Quérel 00:12:58 I agree, and also lineage matter for the in the registry scenario. Even if we are not talking about that directly right now.
it will, it will be a shame not taking that into account into this new version of the schema and And and if you read again the the document I created for the meteor registry, the the resolution process. When we have trees of some multi conventional history with dependencies, this information is used.
Josh Suereth 00:13:37 Yeah, I should put a link to that. You put that in chat somewhere. Right?
Where was that.
Laurent Quérel 00:13:43 Yeah. Copy past some elements of the document. Sorry for that. I will do that right now.
Josh Suereth 00:13:56 Is, is is the document. The document is in weaver or.
Laurent Quérel 00:14:03 It's in the docs.
Let me copy past that. That would be.
Josh Suereth 00:14:08 Schema changes, exploration for future evolutions, or the resolved telemetry schema proposal.
Laurent Quérel 00:14:14 No, that's the the one that is part of Doc. Slash pecs. Slash material.
Josh Suereth 00:14:20 Registry got it? Yeah.
Laurent Quérel 00:14:22 That's the most recent one and and that's where we define initially the registry manifest that we are already using.
Josh Suereth 00:14:30 Yeah. But it's just a small version of.
Laurent Quérel 00:14:33 What I define into these documents. And that's also where we have this concept of registry packaging.
I think that's what we want to discuss right now, in my opinion, but.
Josh Suereth 00:14:46 Yeah, yeah, we we do, we? I think we wanna start going through practical things, too. So anyway, let me, I'll share this cement register changes. We have a directory structure with the roots, domain resources. This is what you're proposing.
Laurent Quérel 00:15:04 I think the so. The the.
Josh Suereth 00:15:05 No no sorry.
Laurent Quérel 00:15:06 The organization was what proposed Remilia, the logistic manifest. What was I proposed?
Yeah. Also mentioned the fact that if we want to enter into multi registry. We need to to be able to have references to group.
That's what we introduced recently with the import.
It's not the end of the story, because we also need to be to support, override.
we already support, override for attributes, but we don't really support override for groups.
And and then we. I discussed many things like registry packaging registry publication, how to retrieve the latest version.
Also the the resolution process.
We don't have to talk about that right now, because it's like a next step after what we are discussing, but definitely what we we want to discuss, as also to take into account this future scenario of a version, 2 of the mutility support, because right now we have a a baby step where we just have one layer.
But yeah.
Josh Suereth 00:16:14 Yeah, that's I. I get it. The the thing I I do want us to ask.
I think I mentioned this before right now, this assumes we're publishing one file.
And I think to Laudmila's point, like we might want to consider having multiple files to support different use cases. Not everyone is going to want to consume everything. And so we need to sort out what those use cases are. And I think that was the discussion. We were just having a little bit about. Lineage is like, what's the use? Cases for lineage? And I think ui and debugging are prime. So like documentation, ui diagnostics and debugging for what came from where absolutely needed for lineage. However, not every use case is a ui use case, so I think it would make sense for us to possibly tease those apart into separate files, and that's the like litmus test we should have here for what we publish like. Let's figure out our use cases. Let's figure out what those use cases like, let's let's walk through what we need in each file. Let's make small minimal files, if possible.
But I just want to like, entertain. You have a lot of stuff in here that I don't disagree with, but there are things I think are still flexible in the design like this right?
Resolving down to one consumable file per registry. I support with the caveat of this multiple use case thing where there might be a registry file that.
Laurent Quérel 00:17:33 I agree.
Josh Suereth 00:17:34 That makes that everyone uses. Then there might be additional files, kind of like symbol tables, if you will.
Liudmila Molkova 00:17:39 That's exactly what I thought about the debug symbols.
Josh Suereth 00:17:42 Yeah, yeah. Cool.
Because I do think lineage is more like a simple table, and it is highly useful, and we should not drop it. But okay, cool. So this one, let's open an AI to figure out how to optimize it.
Thinking of this like a symbol table.
All right? So we have some problems with 2 Yaml filter and Janja Jinja. That is just 2. Yaml is a little weird, isn't it?
Liudmila Molkova 00:18:11 It creates something scrambled. But in some cases I'll create the bug. I'm currently just generating Json. I don't think at this stage we care much.
Josh Suereth 00:18:21 No, no, I let's let's stick with Json for now, too, just to not fight. I? Yeah. Okay. Anyway.
Laurent Quérel 00:18:27 Did you create a Github issue regarding this problem that you you okay.
Liudmila Molkova 00:18:35 I'll create one.
Laurent Quérel 00:18:36 In which context do you observe that.
Liudmila Molkova 00:18:41 So if I do registry generate, and I do, and ginger file, and it does ctx to to Yaml.
Laurent Quérel 00:18:54 Then it creates something scrambled.
Okay, and that was to generate the the gold in that case was to generate the schematics version that was in into this specific task that you you were trying to to achieve.
Liudmila Molkova 00:19:12 So I want to have resolved Schema in semantic conventions. 3 point published right? So I need it massaged slightly. And this is why I use weaver Yamo, and that's why I need ginger template.
Laurent Quérel 00:19:25 Okay.
Liudmila Molkova 00:19:27 We can think about doing the resolve with filtering mechanisms right. But I like the one thought I had. I really don't I see how registry resolve is helpful, but the moment you need to do anything else on top of it, it becomes not so useful.
and I don't really think there is a need for for.
or both the register generate and register resolve. They are kind of the same to me.
Laurent Quérel 00:20:01 Very often when you are in a debug mode, for example, and you want to see what is generated. That's also.
Liudmila Molkova 00:20:13 Yeah for the humans. Yeah. But like, okay, let let's, I don't think it's a. It's a in scope of this discussion we're having. Let's take it separately.
Josh Suereth 00:20:23 Yeah, let's let's talk about this. So discrepancies in weaver commands. Do do you? Is there an AI just to open some bugs here.
Liudmila Molkova 00:20:29 I think this is to the same point that we had before. We need to have templates being the same everywhere. The output.
like, for example, the output for register generate as a directory, and it's it makes sense. But it's the file for resolve, which is also makes sense. But it's yeah, and sometimes output is minus minus output, and and so on. I think we have an action item on this one, and we will resolve it altogether.
Josh Suereth 00:21:03 Yep.
Okay. So then the meaningless null s. Is there any contention with us? Just removing null values from the generated?
No change ourselves?
Yeah. Okay.
Liudmila Molkova 00:21:15 To go and approve my Pr.
Josh Suereth 00:21:18 You already have a Pr for it. Beautiful?
All right. So then, diff. Data has no stability properties. This is the thing I want to talk about. Okay. So 1st of all, Lawrence, if you haven't seen this already in semantic conventions, we're splitting stable versus unstable kind of distributions. And so for every version of semantic conventions. We want downstream instrumentation generation to generate only a stable library.
and then the bits that are considered unstable. You would generate, in addition to stable. So you'd have like an experimental library that has everything, including all experiments. And then you have a stable library that only includes stable.
That's the thing that we want to do. And so the question is, when we publish a registry, should we publish.
you know, to make sure that people are doing this and choosing their distribution right? If they want stability, we kind of want them to only pull a registry that only has stable things, whereas the dev would be like, Okay, you want to be on latest. You want to see what's coming. You can pull from Dev. But you have to manually say that in your version of like I want the dev components.
Laurent Quérel 00:22:30 And it.
Josh Suereth 00:22:30 Have a different schema, URL, if you use dev versus. If you use the stable one.
Laurent Quérel 00:22:36 Okay, okay, that's I mean, depending on the low wage. So, for example, for us, they are not leveraging feature that you, you consider that that will be 2 crate and not one crate with feature. Dave.
Josh Suereth 00:22:53 Good question. It.
Yes, because of the way the way that stable version bumps happen.
even it. So even if they're using a feature. You don't make breaking changes on the crate.
To the feature, whereas in this case dev allows breaking changes.
Laurent Quérel 00:23:14 Okay. So that case, we in that case we need to be able to generate 2 versions. 2 set of schema related files, one for Dave, and one for the the stable. One.
Josh Suereth 00:23:28 Yeah, it. It's also possible that this might be a centcom specific thing where the way I would model this today.
I would have a stable semcom version that's released, and I would have development. Semcon depend on the stable and publish that.
Like. That's another way to think about this.
Laurent Quérel 00:23:54 Version. We will contain the the entire thing right, the content. Stable and unstable stuff.
Josh Suereth 00:24:03 Yeah, that's how we've been doing it. Now. Yeah, I think there are some like, there's some weird problems with this. For example, what does schema rail look like on the wire?
If I'm using, you know, version dot dev with stable things, do I get version dot dev or version.
Liudmila Molkova 00:24:29 You. You have to be deliberate. Right? You need to say, Okay, and we're using the stable one or deaf one.
Josh Suereth 00:24:37 Yeah. Like, when we do Cogen, you mean, right?
Liudmila Molkova 00:24:41 When you do coaching. Yes, when you do anything with instrumentation.
Josh Suereth 00:24:50 You'd have to do it.
Yeah.
Liudmila Molkova 00:24:53 You deliberately put one or another.
Josh Suereth 00:24:56 Right? So it it's basically it it is.
what what do you call it? Sticky.
Liudmila Molkova 00:25:04 If I decide to depend on this when I do code Gen. All my instrumentation has this as a version.
right.
Josh Suereth 00:25:13 Yeah, I think that's that's exactly kind of what I want to see here. So you're opting into the unstable channel or a stable channel.
Liudmila Molkova 00:25:20 Right.
Josh Suereth 00:25:22 And we. So so for context, I think if we look back at Laudmila's Pr, and you look at the where's your templates that we're doing this.
Is this it here?
No.
Liudmila Molkova 00:25:35 This in attitude.
Yes. Oh, this thanks, AI for helping me write this. I wouldn't manage it on my own.
Josh Suereth 00:25:46 All of the else dot, just yeah, it's fun, anyway. So so this is, this is an example Lauren, where basically we're we're we want to only keep stable members. And you know, there's a stability column on groups and attributes and fields any news. And so we're saying, like we. You know.
we have a stable channel which should only be the things that have been marked stable and everything else is pruned.
This might want. We might want to have this as a weaver feature.
If if we need to do.
it's also possible that we find out that only semantic conventions is publishing things the way it is. But it's a bit of a legacy for how semantic conventions has evolved, and how we've done our stability guidance and our fine grain stability across attributes and groups.
As opposed to like big blanket. Hey? Here's version X, you know, this whole package is unstable. We do it fine grained in the same registry. And so the this is something I think we need to sort out and I again, I see 2 ways forward. One is weaver has 1st class support for for stability filtering, which I think it it needs. I think that that's that's easy. But we, that 1st class support also means that I can publish these 2 registries right? And when we figure out what that looks like in that world.
The second way we can do this is, we can basically we can, we can do that.
pretend like one can depend on the other.
So instead of having them completely divorced, we can basically pretend like, the development depends on the stable.
Liudmila Molkova 00:27:39 As a separate registry.
Josh Suereth 00:27:41 As a separate registry. So if I opt into dev, I can use stable attributes, and they remain from the stable registry.
Laurent Quérel 00:27:48 With the condition that they should be the same version, otherwise.
Josh Suereth 00:27:54 Yeah, yeah, like, you would have to. Your dependency should be the exact same version. Basically.
Laurent Quérel 00:27:59 Yeah, which will when you are linking. So let's say you are a user of those things.
How do you check that and how it's enforced. It's not that easy depending on the language. And so for me, this solution is a little bit more brittier than the other one.
Liudmila Molkova 00:28:22 Yeah, we're force a hard separation.
Think Java and Python already do it in a different manner. And Java pop like in a manner that they.
these 2 artifacts, are completely divorced.
Josh Suereth 00:28:35 It's yeah. It's really odd. In fact, let's look at that. It's a cement conventions, Java. I think I can show this cause. I worked on that code a little bit, too. Hold on.
where is their things? They have some kind of incubating.
And if we look at incubating, this is all the unstable stuff, right?
And it tells you I thought it had deprecated. Use the stable version.
Liudmila Molkova 00:29:01 Yes. So when something becomes stable.
Josh Suereth 00:29:05 Oh, we need to look at the Http. For that right.
Liudmila Molkova 00:29:06 Yeah.
Josh Suereth 00:29:08 Telemetry, incubating, perhaps.
Liudmila Molkova 00:29:10 So they are having deprecated property, saying, Go, use the stable one instead.
Josh Suereth 00:29:17 Yeah. Right? Here.
Liudmila Molkova 00:29:18 Which which is honestly better than a dependency. I I would like dependency would be a huge source of yet another issues.
Josh Suereth 00:29:27 Right? So so it sounds like we shouldn't make it a hard dependency. We should literally keep them separate and do the the hard divide.
I'm fine with that.
Liudmila Molkova 00:29:40 Be easier, I'm thinking, if we can change our mind at some point.
Josh Suereth 00:29:45 And optimize further. I don't know.
We probably could like we, because again, people are gonna be opting into one or the other. And if we make one depend on the other, we probably can make that change in the future without it being a massive breaking change.
I at least I think so like if if in Java this this was deprecated and actually pulled in the value from the the stable component like, if it if this was a link to the other attribute on the other thing that would not be a breaking change.
So yeah.
Liudmila Molkova 00:30:22 Right, yeah.
Josh Suereth 00:30:27 Okay, since we think we can change it.
Let's regarding the the.
Laurent Quérel 00:30:44 The fact that the filtering for stability could be a first, st let's say, function that is implemented by and not by filter. I agree with that. I think it's a reliable for me. It's a mechanism. It's something that is where that makes sense to have that as a 1st citizen function part of river that we maintain against the values potential evolution or future evolution of the semantic convention format.
So I I will find that normal to have a dedicated parameter across all the the we recommend where we can say I'm only interested by stable or only interested by unstable.
Liudmila Molkova 00:31:43 I think this is usually needs more processing. And I would actually prefer us to focus, let's say, on days of use rather than adding new parameters. We already can do this. We already have Jq. Filters for code generation. We could reuse them here.
Josh Suereth 00:32:03 Yeah, we can just add.
we could add it to the Jq to to start with, to to be minimal. And then if we wanna. If we decide we need it as a top level parameter, we can add it later, like it's that's also not a 1 way door.
Laurent Quérel 00:32:18 Okay. So just to make sure I understand. What what you are saying is we we continue like we we do. We use a Jq. For now and you're proposing, not going into the the direction I was describing. First, st okay, but that's fine.
Liudmila Molkova 00:32:34 We can always start going to this direction once we have nothing else to do, or less important things to do.
Laurent Quérel 00:32:41 That's okay.
It for me.
Josh Suereth 00:32:45 Yeah. And if I recall correctly, Weaver already has like stability filters in Jinja, we just we need that in Jq.
Liudmila Molkova 00:32:58 We have stability filters in Gq. The thing is that they her ideas something slightly different. I think they they group things right. This is where we group individual signals.
Josh Suereth 00:33:14 This is the Simcov helper. You need just a generic filter that works on the raw Duvor. Yeah.
Liudmila Molkova 00:33:22 Across all signals at once, and does not go rub down by the root namespace. But let's talk about it. I have some point on this to make.
Josh Suereth 00:33:30 Yeah, we we. The thing I was thinking of is, we have a test for stable experimental and deprecated in Jinja.
But yeah, what what do you? What do you want this to be?
You said. Let's talk about it. Let's what what do you want to.
Liudmila Molkova 00:33:47 So I would need maybe 15 min to get through it. Would you be fine with this.
Over.
Josh Suereth 00:33:56 Yeah, that's fine. Go ahead. Oh.
Liudmila Molkova 00:33:57 Yeah, thanks. So I've been thinking about all the different things that are related and how we can fix them so essentially, what the outcome of result schema should look like.
This is something we can.
Some would easily change. It's harder to change the simcom schema. But I think we can also change it as well.
And it's the big one.
So we have a bunch of problems right with the naming. I. I have this table showing all the different names we have for things that and how they're called in Prada.
So we need to fix this.
I don't think we can be super consistent.
There is no way we can call span, name and name we can. There is no way we can call span identity, and Id either.
Neither is the known name work for Spence.
So we will need to harmonize those things. And I'm thinking, name everywhere.
But maybe type for some special cases like Spence.
So.
Josh Suereth 00:35:21 Do, do you? I know this sucks, but if we just call it name on span, how bad is that?
Laurent Quérel 00:35:28 You know.
But if we, it's type, in fact.
Liudmila Molkova 00:35:33 Let's let's so. The problem is this, I see that we need span identity over the wire as well.
Josh Suereth 00:35:40 And there is already spend name over the wire and spend Id over the wire.
So entity already the name is actually type in the proto. It's already stupid, awkward, and that confuses people.
So if we're going to deviate for span, we would should deviate for entity as well, because it's all.
Liudmila Molkova 00:36:04 Absolutely. Yes.
Josh Suereth 00:36:05 Okay, I guess this is where and don't hate me. I want to change the gamble.
Liudmila Molkova 00:36:16 Sure. Yeah.
Josh Suereth 00:36:19 The fact that we try to make everything a group, I think, is problematic, Laurent. I know you had a Pr to have it instead of have, like one group type that shares all the attributes together, we actually have different variants for all the different signal types that are specific to that signal type.
Yeah, you you have schemas here. I I like this like, if we if we get to the point where that's also how you would write the groups that go into weaver attributes, metrics, events, spans. I think that's good. The thing I will caveat, though.
is, remember the whole refinement versus definition that I was working on.
Ids are valuable to know if something is a refinement when it comes to groups. If we're going to do that.
Liudmila Molkova 00:37:10 Yes.
Josh Suereth 00:37:11 Yeah.
Liudmila Molkova 00:37:13 So I was thinking that for this the name and Id are the same for the original definitions, we can explicitly quote it. We can also omit it. No strong opinion for refinements.
I think this is a separate type of the group or type of the thing, and you have to have id, that's different than the name. Both go over the wire for all signals, for identification purposes.
Josh Suereth 00:37:45 Why would you put both over the wire, though.
Liudmila Molkova 00:37:48 Remember the Span identity discussion.
If we need to validate spans or do any special treatment for spans, you also need it over the wire and metrics would not be different.
Josh Suereth 00:38:05 The the only, the only cave that I have. So like.
All right, let's let's think about this in practice. I have a database semantic convention for Msql.
or or even like Postgres or something right There's An Id for postgres.
Liudmila Molkova 00:38:22 That.
Josh Suereth 00:38:24 That metric abides by the same metric defined in the generic metrics.
Right? But it's a refinement where I refine it and clarify this attribute will be exactly this. This attribute will be exactly this.
It's worse than that.
It's worse than that.
Liudmila Molkova 00:38:45 Because, let's see. So this is the the generic metric that we have for everyone. Right.
Josh Suereth 00:38:53 Yeah.
Liudmila Molkova 00:38:54 But here is the cosmos refinement version for it.
It says, Okay, this is this, are the attributes. And you would see the cosmos specific attributes on that metric.
Josh Suereth 00:39:07 Yeah.
Liudmila Molkova 00:39:08 So it's not. It's not a, it's, it's an extension, right? It's a it's a different metric. But it it has the same. You can use it in the same manner, you would build the same dashboard for this metric, the generic one.
Josh Suereth 00:39:26 Right. So I guess then the question is, what are you gonna put over the wire for? The Cosmo metric? That's different.
Liudmila Molkova 00:39:36 The the name is the same. Right? It says, Okay, you can build that. You can treat this metric as generic database metric.
Josh Suereth 00:39:44 Yeah.
Liudmila Molkova 00:39:44 But you can also treat it as something else. This is part of the lineage, right? It's it's also.
Josh Suereth 00:39:52 What is what is on the wire? No, Tlp, that lets me know it's the Cosmo version.
Liudmila Molkova 00:39:57 So I would want to put this this Id over the wire, or however you call it the the identity that maps this metrics to something very specific and semantic conventions.
Laurent Quérel 00:40:09 And why not having a different approach where the name contains azure?
So let's say you, you you refine something, so you have to rename it because it's not exactly the same thing.
Then we have this resolved schema somewhere accessible. That will give you information. If if you are back, end, or whatever is the intermediary stuff consuming this Otlp traffic?
There is a schema here, and we have the name. From that we can identify what was the the exact definition and the inheritance between these refined metric and the original one.
That was the the dB duration block that you you mentioned.
Liudmila Molkova 00:40:57 So my main goal that somebody who has a generic database dashboard, let's say, shared the Grafana dashboard. You give it the azure cosmos dB. Telemetry, and it shows meaningful dashboard right.
Laurent Quérel 00:41:12 Yeah. And that's exactly what will authorize what I'm I just I just described, because the this dashboard system could look at the name. Okay, as you or something.
Liudmila Molkova 00:41:23 No, no! The name must be that metric name.
Josh Suereth 00:41:29 So.
Laurent Quérel 00:41:30 I understand what you are saying. I'm proposing something different.
Liudmila Molkova 00:41:36 Isn't it unstable?
Laurent Quérel 00:41:39 Let me, I mean, maybe I didn't explain that. Well, but at the end of the day what you like is a dashboard where you are able to reuse some element, that matter for this generic metric. Right?
You want to be able to leverage the the fact that for the dB blah blah duration metric. You want to get the corresponding behavior.
I think that's entirely feasible.
If we have the semantic convention, the resolve version where we have all this lineage properly defined.
and you can have a name for the metric that is not the original name, but something that is meaningful for azure.
and still be able to do the the correspondence between the 2. That was the.
Josh Suereth 00:42:31 What you're saying, Lauren, but like, there's so many systems that are stupid right now that we need to interact with so like the idea behind having the same name like, think of it more from an alerting standpoint, with alerts, you basically make a query against time series. And then anything that's above whatever threshold you define or anywhere you get a 1. Basically, in the resulting query, you fire an alert. And so the reason we want the metric name to be exactly the same is so that that query for your alert is the same for every database, and I can make a generic threshold, for when I have slow queries.
Laurent Quérel 00:43:04 But in that case, in a realistic domain, a realistic system, you could have different processes using this exact metric, but with different set of attributes, because they are basically what on one side it's azure, and on the on the other one, it's aws.
Josh Suereth 00:43:23 But but there's a.
Laurent Quérel 00:43:24 But they have the same name.
Josh Suereth 00:43:27 A consistent set of attributes within it that you are grouping by or or aggregating in some way right? So like, if you're if you're doing some of our recommendations for like stable attributes. Right? If I'm grouping by database operation name, all those other ones are basically erased for the purpose of this generic metric.
Laurent Quérel 00:43:49 Okay, so but people, how can how people can use the azure metric as is, I mean the those.
Josh Suereth 00:43:57 No.
Laurent Quérel 00:43:58 Think it matter right?
Josh Suereth 00:44:00 There's 2 use cases. There's 2 use cases. There's a generic use case. Of what observability do I get where I don't have to care about it being azure. I just want to know if my database connection slow, that you don't need those attributes, for then this is the whole T-shaped Api thing. I have a Pr about this right? So the generic use case. I don't care if it's azure or not. I just want to know if the database is slow. Then when I go to investigate, I might look at the azure specific dashboard that uses those attributes, and that's a different dashboard.
or it's a subsection of the dashboard that gives me azure based information. But the idea being like someone throws a random workload at you. And I want to say, hey, I can at least tell if database queries are slow.
Looks like this one's having trouble with the database. What database are you using? Let me open the appropriate dashboard for that. Right? It's not like a you need to use all things at all times, everywhere, generically. There's a generic set of alerts I have. Then there's a deep set of things I have. That's how we've designed this. I see what Ludmill is going after I do.
I am nervous about the amount of stuff we're throwing on the wire here.
Laurent Quérel 00:45:09 Not only that, but also I mean the stupid system that you mentioned. They will have to evolve significantly to support that the protocol.
Liudmila Molkova 00:45:19 They don't. It already works.
Laurent Quérel 00:45:21 Protocol does not contain this Id. For example, you you are oh, they can ignore it.
Josh Suereth 00:45:29 So those systems don't need it.
Weaver would need it for for live check.
And yeah, the system, basically the way the way most of these dashboarding systems work are. If the labels don't exist, you don't find anything right, or it fills an empty label there, and you.
Laurent Quérel 00:45:47 The Id will not be on the wire. My understanding was okay. We need to introduce on the wire a new idea, a new id, in addition to the name.
Liudmila Molkova 00:45:59 So my goal that it's over the wire. Right? So let's say, we look into Spence.
We have different flavors of spans that are pretty much the same. We have no idea over the wire for spans today.
It is a problem. We cannot live, check them. We cannot like the way people identify spans is by looking at combination of attributes. They have some heuristics, and it doesn't scale. Well, I would imagine the same problem will exist for the matrix flavors.
If you have your company extension of dB operation duration, you would want to validate that it confirms to your company's conventions.
and it's 1 more id that goes over the wire. It can be in metric metadata. It can be super efficient.
It does not have to be.
Laurent Quérel 00:46:57 Well, it will be super efficient with definitively, because that will end up into a dictionary in pure Tlp, you have to work on that definitively, because I mean, it's it's not. It will be replicated for every data point.
Liudmila Molkova 00:47:13 Yeah. So maybe we can park the over the wire discussion. We need Id for identification purposes. We can tackle the over the wire separately. It's the spec discussion, not the semantic convention tooling discussion.
Josh Suereth 00:47:26 Yeah, I I think there might be. We'll we'll have to talk about this, because there might be other things we can do around refinement. I I like that. I like the proposal. What you're getting after like, if we go back to that right.
Id is only used for refinement.
we have explicit refinement of attributes and groups.
and refinement means something specific of. I abide by everything in my parent, and I might have additional restrictions or additional things, and we can put policies on that.
I like this. I think this is a good direction to go generally like from. If you think about if we think about this purely from weaver and and semantic conventions, I think this solves the business of defining telemetry right? We need to sort out what goes on the wire. What we can do with policies, what we can do with live check. I think there's a lot of things for us to follow up on that. But I do like when I was trying to go through the attribute registry Pr, and the refinement versus you know, definition thing. I was fighting all this. So I think we're in better shape.
If you can scroll back up because we have imports, we have attribute. Okay, with attribute.
Liudmila Molkova 00:48:39 Go ahead.
So I wonder if we can just start by resolving this shape of schema.
So we don't.
Josh Suereth 00:48:52 Span id.
You want span id to be the effectively what the name is. Other places, or you're going to have name, reference attributes, or what like I saw that. But what was the plan for span?
That's the one I want to know right now, like everything else moving metric name to be. Name.
I think, is trivial. That's fine, not a big deal right?
What do? What do you want to do with Span immediately? Let's let's sort that out.
Liudmila Molkova 00:49:21 Yeah, so let's pick a name. So that's what we have, right?
so we need the the span Id and name are near and dear to span. So where the wire we I that's why I would like to maybe use type the 3rd word, but it sucks.
Josh Suereth 00:49:40 But oh, so honestly. Look.
if you call it spans instead of groups. Type is now open and available. So entities can use type. Span can use type, because that's literally what we would put on the wire.
Does that? Does that make sense like entity? Already? It's called entity type.
But in in Weaver. It's called. It's called name, because we're using this groups thing right?
Liudmila Molkova 00:50:10 Okay.
Josh Suereth 00:50:11 Is no longer needed, because at the top level we define the type of the thing we type is now available as a keyword.
Liudmila Molkova 00:50:21 Wonderful.
Laurent Quérel 00:50:22 But don't you think that having span type and span kind.
Josh Suereth 00:50:27 Is not confusing for people.
Liudmila Molkova 00:50:30 Absolutely confusing.
Laurent Quérel 00:50:31 Yeah, I'm not a big fan of that.
Josh Suereth 00:50:34 As a type, as a type theory person. I, you know, types have kinds. So it doesn't bother me.
Laurent Quérel 00:50:41 Yeah. But I think for a lot of people that will not be the case. To be honest.
Josh Suereth 00:50:44 Like like, that's why they're called higher kind of types when you have a type that takes a type because a type has a kind. And so, having a span, have both the type and a kind just doesn't phase me in any way, because it even makes sense in that light. The kind of the span is client or server. The type of the span is this is an Http client, right?
So it's like a refinement of kind. So I actually, if from a type theory standpoint, I'm totally fine with type and kind, I think it actually fits well. But I understand that that people 1st time people find out about kinds and higher kinds. Yeah, your head explodes. So I get it.
Liudmila Molkova 00:51:21 You know what? From what I know, people overload kind today, not on the over the wire, but they report span kind attribute. That is an extension, and actually breaks down the client into, let's say, Gen. AI call or something.
Laurent Quérel 00:51:39 Yeah.
Liudmila Molkova 00:51:39 So we, yeah, it. There will be confusion. But what can we do at this point.
Josh Suereth 00:51:46 Yeah, we'll do it for you.
Okay.
Liudmila Molkova 00:51:50 So type wonderful last taste check, actually.
Josh Suereth 00:51:54 To this, to this your example here just add entities. So we know that entities.
Liudmila Molkova 00:52:00 Sorry. Sorry, I thought. That's the sorry.
Josh Suereth 00:52:03 No, that's fine. I just wanna make sure that like, oh, that, yeah, that was that was events. Yeah.
Oh, entities are 1st in the alphabet compared to events. Wow!
Liudmila Molkova 00:52:23 Yeah.
A quick taste check attributes have key over the wire.
Should we use key for them instead of names?
Josh Suereth 00:52:33 I'm fine with that. Honestly.
Liudmila Molkova 00:52:35 Do you like it?
Or do you think we would rather stick with name.
Josh Suereth 00:52:41 No, the key looks good to me like it fits otop better. Yeah.
Liudmila Molkova 00:52:46 Oh, cool, cool.
Josh Suereth 00:52:48 Now this is majorly breaking.
Laurent Quérel 00:52:52 Yeah, in many direction. In fact.
Josh Suereth 00:52:56 Massively.
Laurent Quérel 00:52:58 Template everywhere.
Josh Suereth 00:52:59 This is almost as expensive. I don't know if I told you I started working on my
Laurent Quérel 00:53:05 Actually no.
Josh Suereth 00:53:07 Yeah, I started working on a parser for special syntax that was trying to get away from Yaml. This is like half of what I was trying to do is just having names, you know.
I think we have 2 options. With this right one is, we can make a v. 2 schema, where you actually at the top of the yaml, you have to say this is v. 2, or something or or or or we have to find a way to like resolve. Groups resolve this and migrate groups into this in Weaver. Right? Like.
Sorry I'm saying this really stupid. We resolve.
Liudmila Molkova 00:53:43 Port them side by side.
Josh Suereth 00:53:44 What?
Liudmila Molkova 00:53:45 We can support them some side by side, because they are non non conflicting with each other.
Josh Suereth 00:53:51 W. There is one conflict which will be so. We can convert type from entity to name of entity.
But what do we do about spin type.
Where do we put it? In the existing group?
I think we'd have to put it in group.name.
And then, in terms of our output. We have to decide if our resolve schema reports, groups, or reports this and that probably needs to be a feature flag of whether we resolve down to groups, or whether we resolve down to something that looks like this.
Liudmila Molkova 00:54:23 The good news that nothing uses span id today like nothing can use span id really, except the the Markdown generation. So whatever break in there will be. It's it's self contained within ourselves.
Josh Suereth 00:54:35 It can't be I. The way we use id internally. It can't be id. It'll have to be name.
It'll have to be the name column. We can hide this from people.
but we'll have to put in the name pot column of the group like I don't see how we can use id the way the way that weaver is written right now.
Liudmila Molkova 00:54:53 Okay.
But it's it's it's our code. And I get that. We would like to have the generic transformation, the the the stupid thing we can do. It's just the code that we write that if the the group type is spend, then per, like, really does this and transform it into that.
Josh Suereth 00:55:15 Yeah.
Liudmila Molkova 00:55:16 And the type is, this is Id, the current group. Id.
but we will change it everywhere, because currently they are not not cool. We will change all of the group ids because they are currently metric dot food, dot duration.
Josh Suereth 00:55:30 I see what you're saying. Yeah, okay, we do. We do require unique ids in some in Weaver, though so like, we will have to do that translation in Weaver, or something like. Again, there has to be a translation from what you've defined here to the existing group syntax, and then weaver will continue to produce the existing stuff. It does.
and then we'll have to have a feature flag where weaver will resolve into groups and then write this back out like we have to have a bi-directional transformation.
Liudmila Molkova 00:56:00 Right.
Josh Suereth 00:56:02 Before we can finally get rid of the current group syntax for this.
So there'll have to be a transition period. It'll take a bit.
Liudmila Molkova 00:56:09 Right.
Josh Suereth 00:56:10 I'm amenable to moving this direction. Just we have to sort out the details to make sure we don't break everything and everyone.
Liudmila Molkova 00:56:16 The worst thing we will break is the resolved schema, because it's used by the Cogen. I'm not worried about breaking semantic conventions per se, we will figure it out.
Josh Suereth 00:56:26 Okay, I am worried about breaking coach, and that's actually my main.
Liudmila Molkova 00:56:29 Concern.
Josh Suereth 00:56:30 Yeah.
Laurent Quérel 00:56:31 Yeah.
Liudmila Molkova 00:56:31 So if we create a feature flag, then existing commands that resolve, the schema would just generate. This is the only one that's actually used.
Josh Suereth 00:56:44 Yeah.
Liudmila Molkova 00:56:45 Well have a feature flag that opts you in into a new schema.
Josh Suereth 00:56:50 Yeah.
Laurent Quérel 00:56:52 We could to serve the.
So for Codegen, we have this weaver dot tml, file that describe the what you know. We could imagine that in this file we express to either that either we there is no specific argument. And we we generate what we generate today.
Or there is a mention. Okay, we want to use schema version 2, and then people can start to create templates for this new version. But by default, it's just doing what we do today.
Josh Suereth 00:57:28 We? We also have to do it for policies. By the way.
Laurent Quérel 00:57:31 Yeah, yeah, sure and same same approach could be used.
So we yeah.
Josh Suereth 00:57:39 Mimila, can you write this? I mean, it's already written down. Can you throw in a bug like a like a like a feature request? Template.
Liudmila Molkova 00:57:47 A feature request template to Swever to support new schema behind the feature flag.
Josh Suereth 00:57:58 Yes.
yeah. And we can. We can get folks opinions here. But I anyway, I really like what you're doing here. Glad we're finally being aggressive on this. And I think it's going to be a lot of fun code to write, Lauren. I know you're really busy, so we'll probably have to split this up.
Laurent Quérel 00:58:17 Yeah, yeah, I.
Josh Suereth 00:58:22 I also want to see if maybe.
Laurent Quérel 00:58:24 This one to the new one. I'm I'm totally fine with that. If we have a good story regarding the transition.
Josh Suereth 00:58:34 Yeah. The the question I have for Weaver itself is, I think I think we're going to have to take this in phases. But step one would be. We add this to the Yaml schema that we can support, and ingest.
and we take things that we ingest here and convert them back into raw groups and continue with raw group resolution, as is right.
That would be, I think, phase one phase 2 is where we get more aggressive, where I actually want to.
Allow we. So so phase one is is ingest only the definitions in that format that unblocks a lot of stuff.
Then we need to start having this feature flag where we can export in the new format.
But there's a level of fun. We'll have to do So yeah, phase 2 would be export in the new format, although I don't know it.
If we should export first, st or if we should modify our entire resolution algorithm to be on the new format.
Laurent Quérel 00:59:36 Personally, I will. I will peripheral to generate, to export into the new format.
That looks like and and smaller effort, and and less than risky effort. Also.
Josh Suereth 00:59:56 Yeah, so basically, we start ingesting the new thing and convert into groups. We take groups and we have a thing feature flag which turns them into the new format. On the export side, resolution remains the same, and then the last thing we do is is gut, the resolution engine to only be the new format.
Is that fair.
Laurent Quérel 01:00:13 Yeah, that's that seems a better position. And also it's it's more line with what we want to.
because we start to advertise much more semantic convention, multi-age history, weaver. Now we should deliver the this schema version 2 as soon as possible.
So the export is what matter today?
In my opinion.
So delivering this new format. So we have just have to write the the translation from what we have to to this new one. So it's more a matter of exporting to a new format, and then we can do the the internal stuff later.
Liudmila Molkova 01:00:58 Interesting. Go ahead.
Josh Suereth 01:00:59 Good.
Liudmila Molkova 01:01:01 The interesting thing that we already was the Gq. Filters. We actually produced something like this for the Codgen.
Laurent Quérel 01:01:10 Yeah, I agree.
Liudmila Molkova 01:01:11 And 90% of cases. Roughly, we can handle all the breaking changes in this Jq filters or around this layer.
Josh Suereth 01:01:23 Yes.
so, Lydmilla, if you can throw this on that issue, then I think we also advertise this in Maintainers to tell people this is coming.
Liudmila Molkova 01:01:33 Okay. Yeah.
Josh Suereth 01:01:37 Yeah, I I might jump on this and start working on it if you're not already working in in Russ to do this, Lyudmila.
Liudmila Molkova 01:01:48 Yet. So if if you start working on something, feel free to throw some individual pieces to me, I'll be happy to help.
Josh Suereth 01:02:00 Yeah, I'm not sure how much of this is going to be fragmentable. But yeah, I think that I think we need to jump quickly, and I think I can jump quickly. We'll see. I did just pick up a bunch of entities work, but I I can defer a little bit of that.
I think this is a bit more urgent.
Laurent Quérel 01:02:22 So for them the reserve schema, so that this format and the the concept of catalog that I mentioned before, and the fact that we we could have Oh, we have the attributes. So then we let's play the role of the catalog for the gate.
for the attribute.
Josh Suereth 01:02:41 Yeah, scroll scroll down a little cause, Lauren, I think what you're talking about is, see how we have a ref section here.
Laurent Quérel 01:02:50 Yeah, what I, when you import a schema.
Josh Suereth 01:02:54 and you're leveraging things from it, or you want to like, show them like, say, Hey, I'm using this from that schema. That whole imports thing we had. I actually would prefer to see metric refs where you have an id, and you extend the other thing.
Or if we make a simple way to do the to do it in metric refs right? So I can ref things from another schema. So you had mentioned before about having an the Ids say that they're coming, or having some way of referencing the other schema in the Id or the name. So I think we'd want to do some kind of name, not name mangling, but name thing of like, you know, schema imported schema name pound, and then name of span or name of Metric, or whatever.
Yeah, something like that.
Laurent Quérel 01:03:41 Yeah, double.
We had a single room. But yes.
Josh Suereth 01:03:47 Sorry.
Liudmila Molkova 01:03:51 I don't know what's the rest way, but anyway, we'll pick.
Josh Suereth 01:03:54 I don't. Actually, I think I think Russ just uses dots for everything. The the Colon Colon is a anyway. That's like a class thing.
Laurent Quérel 01:04:02 Yeah.
So just one thing. We we all agree that in the the result version of the schema with the format that put in place there. It's a single self-contained document where matrix or any kind of signal can make reference to attributes that are defined on the top section.
But there is no other references, no other external. No, I mean no complicated things, right?
We all agree on that.
Liudmila Molkova 01:04:37 What do you mean by now? Complicated things.
Josh Suereth 01:04:40 Extend.
Laurent Quérel 01:04:41 There is no extent, there is no external references. There is no resolution, in fact, to implement as a consumer of this file what I want to avoid at any cost is having to reserve this file. So the file that we are discussing there is fully reserved.
This is their business currencies.
Josh Suereth 01:05:02 Yeah.
Laurent Quérel 01:05:03 Okay.
Josh Suereth 01:05:04 You should put attribute references in there to show that Ludmilla, and like, what do you want to do about attribute group extends.
Liudmila Molkova 01:05:13 It does not exist.
Josh Suereth 01:05:14 Good.
Okay.
Liudmila Molkova 01:05:16 At least not in the well. So the reason it exists is to avoid copy paste right if we.
Laurent Quérel 01:05:23 External attributes. Right? We agree on that.
Liudmila Molkova 01:05:27 No extends for attributes.
Laurent Quérel 01:05:30 The. For example, you have 2 metric, the the reference in in the semantic convention you have 2 metric. They reference the same attributes, but they do some differences in terms of overriding we we can't in the, in the resolved version of this entire thing.
what we we will end up into 2 attributes, into the attribute list that are slightly different in terms of definition. And then the 2 metric will reference 2 things, 2 different things, in fact.
Liudmila Molkova 01:06:03 Yeah, so you can still do the reference for the attributes right under specific metric. They're scoped to this metric.
Laurent Quérel 01:06:12 Oh, okay, so we, that's where I disagree because we.
Josh Suereth 01:06:18 Let's sort this out.
So so, Lydmila, I think you're changing the definition format and the resolve schema format you're proposing kind of both here. Is that correct?
Liudmila Molkova 01:06:28 Yeah, we need to break them down. So this is the result, schema. And we need something to very similar for unresolved one.
Josh Suereth 01:06:38 Okay, I let, I think from a friction standpoint, we need both a lot of what you're proposing to me. Let's we can actually pull the trigger on that on the unresolved schema almost immediately of making those changes for the result. Schema like to to some of Lauren's points, Having refinements of metrics in the resolve. Schema is awkward as hell for us.
Laurent Quérel 01:07:08 Yes.
Josh Suereth 01:07:09 That's why we have lineage, and that's why we have literally separate attributes and a whole registry of them.
Liudmila Molkova 01:07:17 So this one. It's only unresolved, schema when you reference something right. And there is right.
Josh Suereth 01:07:26 In the resolved, it would literally reference an attribute, and that attribute would have everything it needs in it, and you would see the same attribute name twice.
right.
Laurent Quérel 01:07:36 That's why it's number in my my proposal, and.
Josh Suereth 01:07:39 That's why that's why we have an Id for attribute. Yeah, we'd have to have an attribute Id or something to say, you're using this version. Yeah.
Laurent Quérel 01:07:48 Automatically generated by Weaver, because there is, I mean, you could have, in fact, multiple times, the same or very similar attribute, but with some variations.
and the duplication process is currently done by weaver. So we know that we we don't have 2 times the same attribute.
Josh Suereth 01:08:08 Yeah, that that's why we have that notion of refinement versus source. That's why we have Ids and name.
Right is the idea. Is that like, if you have an override, the Id gives you the identity of that override.
whereas the name is unique in a namespace that is like the on the wire thing. So that's why I wrote that whole document about why Id and name both need to exist, how they work and all that kind of stuff. We'll have to sort that out and resolve Schema. I do think what you propose for unresolved schema. We could just start executing on right now, and I love it. It's like way better than what we have today.
For for resolve, schema. We probably need another discussion. I do need to drop. I have to go.
do some stuff at home here.
if you open this Pr. Or sorry an issue with this that's awesome, we can start executing, I might start executing on resolving unresolved schema with this format.
Because and I like it that much. I wanna have that work immediately. And I think there's a lot more clarity on what that'll look like. So I'll start working on that as a proposal.
Get that into Weaver, so we can start changing what looks like in terms of the definition. And then we'll start working on resolve Schema. Maybe next week we can have another one of these. We'll either talk Wednesday, or maybe we talk 2 days in a row again. Doesn't matter to me.
Laurent Quérel 01:09:30 Yeah. So during the next 2 weeks I will not be available.
Josh Suereth 01:09:34 Okay, I'll try to speak on your behalf. Then Lauren.
Liudmila Molkova 01:09:39 Yeah, enjoy your time off.
Josh Suereth 01:09:41 Yeah. Have a good vacation.
Liudmila Molkova 01:09:43 Thank you. See you around.
