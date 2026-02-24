SIG: Semantic Convention Tooling
Date: 2026-02-11
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/9129nMbEGv18FabWe9iOdo7IhBMyizdNY3yhUOzgfyJdDdUaXf1nj4ZPpyDdw0De.BEdILkMD989pXmJv
============================================================

## Zoom Recording Transcript

Jeremy Blythe 00:02:52 Morning.
ariannavespri 00:02:57 Hello!
Jeremy Blythe 00:03:08 We've got bots in the meeting again.
Josh Suereth 00:03:18 How's everybody doing?
Sorry, I'm a little slow.
ariannavespri 00:03:23 All good, how about you?
Josh Suereth 00:03:26 Not bad, not bad.
somehow been the craziest January and February for me, work-wise, in terms of, like, things going on at the same time. I don't know how that happens.
Laurent Querel 00:03:42 I agree.
Jeremy Blythe 00:03:45 Hello.
Josh Suereth 00:03:47 Oh yeah, I have one other topic here, like, the doctor.
I don't know if you guys saw this, I'm just gonna briefly mention it if you haven't seen it. I asked the DocBot to write documentation on multi-registry, and I thought it did a decent enough job, but then Lydmilla said, hey, this is all V1 syntax, could you update the V2? And it went insane.
So, I'm just gonna put the PR there. You can take a look at this. I think it's kind of amazing.
alright.
Liudmila Molkova 00:04:27 Hello, good morning.
Jeremy Blythe 00:04:29 Hello?
Laurent Querel 00:04:29 Good morning.
Josh Suereth 00:04:30 I was a little distracted. We're gonna get started soon. I do want to spend a little bit of time in our project board.
But I'm going to do that at the end.
Okay.
Alright, let's get started. Let's talk about multi-registry manifests, dependency conflicts, and naming.
Alright.
So, Ludmila and I had a bit of a discussion on this issue. I didn't see if anyone else commented, but I'm gonna walk through the set of principles I put to see if we all agree to those first, before we go into the discussion. Because I think, Lyudmila, there's a principle I didn't write that you called out later and needs to get added to this. Alright. First…
I think we need to migrate from registry underscore manifest to just manifest. I think, like…
We don't have to.
It's like a convenience thing, but we should do it now or never.
You know.
Okay.
Second, we need consistency in referencing a registry.
So, what Lyudmila called out in the registry manifest resolver thing is that we have ID, we have URI, we have name, we have URL, we have schema URL, we have registry URL, like, we have a very confusing set of things.
And lastly, for dependency resolution, we need to understand if we have a diamond dependency, which means we need to know if references to two things are technically the same, but different versions. So we need some kind of an identity to represent a registry.
that is independent of how you get it. So it's independent of if it's in the zip, it's independent of if it's a, you know, somewhere else. So I think this means it has to be in the manifest.
Cool. Those are, like, the needs. So the set of principles.
We need this name, it should be unique across all registries, and it can be used to denote if we have dependency chain with the same thing.
Again, I think this implies it has to be in the manifest, but I don't think that's the important point. The important point is it has to exist, and no matter how you consume it, you have to be able to find it.
Second, we need a URI for the registry that is how we got it. And that URI can denote the manifest file or the directory, I don't care, but we need some way for people to tell us where these things are. And it's a Weaver URI, or a virtual directory ref, or whatever the hell we want to call it.
Okay.
And I should have called out those are independent. Lastly.
We need to know how to find resolved schema.
This… this is, like, how we denote where we load resolve schema after we've resolved the manifests. Like, it's a two-phase thing. So the idea here is, we first get access to this red… this manifest registry, and then we use that to determine how to do the further resolution.
I probably should have phrased this better, but that's, like, the last principle of, like.
When we do resolution, first is we get a manifest of some form.
Then we resolve either your definition schema, or your resolve schema, or whatever.
Okay?
Alright.
So my strawman proposal, and this needs to be fleshed out, because we're going to go through the millis comments.
We would… for now, we're gonna allow either registry manifest or manifest, because we don't want to break people.
If manifest exists, we use it instead of Registry Manifest, and if we see Registry Manifest, we issue a warning that this will no longer be supported, and you should rename it to Manifest.
Any, any concerns with that?
Okay.
Next.
We start… whenever we talk about virtual directory ref, we call it a Weaver URI.
As a terminology.
And this is where we can do the whole, you know.get, bracket.
directory and the Git name, or however we're going to do SHA references, and stuff like that. Like, that syntax we're gonna call a Weaver URI.
In docs, going forward.
Laurent Querel 00:08:45 Sojours.
Josh Suereth 00:08:46 Yeah.
Laurent Querel 00:08:47 Is it what we used to name, registry pass.
I think in the command line, initially.
Josh Suereth 00:08:55 Yes.
Laurent Querel 00:08:57 Okay.
Because I don't think we use the actual directory anywhere except in the code.
Okay, I'm fine with that.
Josh Suereth 00:09:07 Well, we use… we use that URI for… Weaver URIs are used for the package argument, and they're used… er, policy argument, I should say. I think for template package as well, and then for,
the registry. So it's used in, like, 3 different places, which is why I think it just deserves a name, and we can talk about.
Laurent Querel 00:09:29 Absolutely.
Josh Suereth 00:09:30 Go ahead, Lumbo.
Liudmila Molkova 00:09:31 Should Weaver be part of the name?
It's… it's the name of… sorry, the… the URI.
I think it should be a registry, you're right?
Josh Suereth 00:09:42 It's… so we use it for more than registries, we use it for packages, too.
It's because… yeah, like, if you, if you specify a policy package.
you do it in a special syntax, where we… I'm calling it a Weaver URI, because it's not a URI,
it's a reference to something that can be, like, inside of a zip file, or inside of a Git repo.
Liudmila Molkova 00:10:05 Yeah, but this is the same as registry URI, because registry URI can point to anything.
It's just from the principles of decoupling.
in my mental model, there is a SimConf problem, and there is a tool weaver.
And in theory, I'm not suggesting, but there could be another tool that's not Weaver that does the same.
Josh Suereth 00:10:30 Yeah, I'm suggesting that I don't think we need to use Weaver Your Eyes at all.
in Semcov.
the… like, a semantic convention URL would not be the same thing as a Weaver URI.
And we can get in the details about why, because I think we have some brief discussions about that, but I… I don't want to conflate those two things.
Liudmila Molkova 00:10:53 Okay.
but…
Josh Suereth 00:10:55 Yeah.
But the… okay, so this one has contention, so we can move on, but… but let's note that it's contention. The idea here is we need… I just want a name
That is, I can look up…
a thing that could be in a zip file, a Git URL, or an HTTP address, or a local directory. That's what Weaver URI means, that's all it is.
Laurent Querel 00:11:22 But what was the registry pass, initially?
Josh Suereth 00:11:25 Yes.
But when we started using it in policy, it became policy path. When we started using it in, in templates, it's now, like, the template path. So, like, I…
Laurent Querel 00:11:37 But with a different, with a different way of behaving.
We don't support, everything that we support.
For registry, for example, with templates, the… this, bracket blah.
was the… I don't think, was part of the…
a template pass, for example. So they were different, both in terminology and, in the code, I think.
Josh Suereth 00:12:05 Okay, I'll have to take a look. I thought you were using virtual directory ref everywhere now.
Laurent Querel 00:12:09 No, I don't see so.
Josh Suereth 00:12:11 Okay.
Right.
Laurent Querel 00:12:12 Maybe a lot of things change in between, and for the good, definitively, thank you very much, but I don't think that was the case. I don't think it's the case now.
Josh Suereth 00:12:23 If that's not the case, I'll look into making that the case, because I… what… I like the idea
And again, this might… this might be too much, just having… so having that syntax documented once in our documentation, so users know what it is, and then, the command line arguments at Weaver consistently use that when you have to specify things.
Whether or not that shows up in the manifest URL.
is an alter… like, that's a separate discussion, right? That might never… that syntax might never be used to manifest, and I think we can make that decision independently. And Ludmil, I think you're pushing for that, and I am with you on that.
Okay.
So, next.
We want to change registry manifest as follows, and for some reason, these are not tabbed appropriately. I'll fix that. Resolve schema URL becomes Resolve Schema URI.
It could also be resolved schema Relative Path, Resolve Schema path, I don't care. The idea is, when I resolve the manifest, there's a thing in the manifest that tells me if there is a resolve schema.
And how to get access to it.
that thing, like, in my example that I have right now, I'm using a relative path with the idea that, okay, if I need to publish this, I get a manifest and I get, a YAML file, which is the resolve schema, and I can just take that and publish it to a directory, and that's dead simple publishing.
and things work. I don't have to figure out how to, like, put a full URL or something.
there, I can make something that can move around to different locations and still be resolved.
Okay, and if I resolve it out of zip file, it still works.
Again, I don't care, really, what this name is, I just care that it's not URL.
That's the main thing. Alright, next, we remove name from registry manifest, and this is where things get contentious.
What I'd like to start doing is we use schema URL as defined in the specification.
Where when I make a registry, I pick a schema URL for that registry. And the definition of schema URL today in OpenTelemetry is there's a HTTP address.
The first bit should be a domain that you own.
All the slashes don't matter, but kind of are your name, of some fashion. And then the last bit is a version string.
So the idea would be, we can use the first bit to uniquely identify your registry as a name.
that will be consistent across all versions, and we can use to determine if two things are the same, right? And if there's a version conflict. And the last bit will be your version. So this schema URL provides double doot. That's the idea. Go ahead, Linmilla.
Liudmila Molkova 00:15:17 I see it could work, but I really don't like the assumption that the schema URL will have a certain
Format, and you can never change it, and… Unless you want to…
change your registry. I want people to be able to use schemas from GitHub.
And this will break this assumption of the format.
And I think we can't… we don't have…
Josh Suereth 00:15:49 Do you mean, like, in… in the OTLP that they write?
The schema URL would be a GitHub URL.
Or would it be the IP address on GitHub?
Liudmila Molkova 00:16:02 let's say.
somebody didn't publish their schema. They have it on GitHub, but they didn't publish it. I can use it as a dependency.
Josh Suereth 00:16:11 Yep.
Liudmila Molkova 00:16:11 Right?
Josh Suereth 00:16:12 Yeah, exactly. That would still be the case here.
Liudmila Molkova 00:16:15 Yeah, but, we'll… at some point, we'll get to my proposal, and you'll see what I mean. I… I…
thing.
We are putting too much into the schema URL format. It probably will work within OTL, but outside of the hotel, it would be hard.
Josh Suereth 00:16:40 Okay.
I will call out that telemetry schema's the stable part of it, actually specifies
like, a URI. It doesn't specify the open telemetry… well, it does specify an open telemetry, at a well-known URL.
Liudmila Molkova 00:16:57 I mean, that the version is the last bid. Yeah, no, that's literally specified here.
Josh Suereth 00:17:08 And this is marked as stable.
So, we already require this across OpenTelemetry. And if we don't think that that's gonna work, we're going to have to, like, actually push on the spec itself.
Liudmila Molkova 00:17:23 Okay.
Josh Suereth 00:17:24 OTEP would have to propose changing this.
Liudmila Molkova 00:17:30 Mmm, okay.
I see your point.
Then… Assuming we use schema URL.
In the… In the registry, what would it point to?
We use it not… it's not used in the manifest file, actually.
Josh Suereth 00:17:51 It's not… I'm suggesting that we would at least need… so, again, we can come up with terms and things for this. I'm suggesting that in the manifest file, at a minimum, I need this.
I do think it'd be better if we do the whole thing.
But think of, like, when I declare a package in Cargo, when I declare a package in Python, when I declare a package in Java, or Maven, when I declare a package anywhere, I say, here's my name and here's my version.
Exactly.
Liudmila Molkova 00:18:22 You don't say where to get it from. In our case, we need both.
Josh Suereth 00:18:27 Well, we're… okay, but, but, but, here, we're…
There is a default there. I mean, ignoring the fact, like, in my opinion, the schema URL is the name and the version in one string, and I don't care if the URL is legit, I'm still gonna work.
In my world.
It's ideal if the URL is legit and that's where you publish, and that's kind of the intention of schema URL, but pretend that it's not. Pretend it's just, like, a string that's the name.
Liudmila Molkova 00:18:52 Oh, then everything falls apart. Nobody can use your schema, right? You… we can still work with… no, we cannot work with it, because we cannot resolve it.
Josh Suereth 00:19:01 Right, and that's what we need to make the whole system work together.
But, but think of… okay, think of some of the benefits, though, of having it be an actual Euro, right?
I need the ability to publish that URL, which means I own it, which means I will be unique across the world.
Liudmila Molkova 00:19:21 Yeah, I think we… this debate is not important. I think we can work either way. I'm more interested in discussing how the final thing looks like, and how it would work with your proposal.
Josh Suereth 00:19:34 That… that sounds fun. Yeah, that's… because this… this is the… this is probably the big thing for us to discuss. Let's go through your proposal now, of, like, what… what we're looking at.
Liudmila Molkova 00:19:44 Can you scroll down to my last comment? It's actually… I've… I've made a long way.
Josh Suereth 00:19:50 This one here.
Liudmila Molkova 00:19:51 Yeah, so I think the key part, my proposal is different from yours, is that I…
as a part of the resolution process, we would need to go and download all the dependencies, all the transitive dependencies, and we will go to manifest file anyway. We need to manifest file anyway, and the name and the version could be there.
Josh Suereth 00:20:19 Yeah, yeah.
Liudmila Molkova 00:20:21 But I… I mean, I'm not married to it, it doesn't matter.
What I'm suggesting that we use this whatever term we have, in dependencies, we drop the name.
From it, it's just a list of dependencies.
And then, we put the same information inside the resolve schema, so we know what to resolve.
And then we essentially reference these dependencies, when we…
when we have attributes, signals, definition, and refinements. If it… oh, sorry, if it comes from the dependency, we reference the dependency. If it… it's part of this registry, then the top-level thing is the… the dependency. Whether we have name or version, I… okay, we can drop it.
Josh Suereth 00:21:12 Well, I like this, by the way, of, like, okay, so let me put a straw man out there. This I love, like, okay, so, right, dependencies is just a list of schema URLs.
Liudmila Molkova 00:21:24 Or GitHub, or whatever.
Josh Suereth 00:21:26 place you can…
Liudmila Molkova 00:21:27 get the manifest from.
Josh Suereth 00:21:28 Let's say it's just schema URLs, only schema URLs. Now, we have a separate mechanism. Most dependency systems have this as well. We have a separate mechanism where you can say, this schema URL is located at this
Weaver or I.
Like, when you see the schema URL, here's where you resolve it from. And we can have a config file where you can put that in. Or, like, this is where you can provide your own registry of things, if you have, like, private… right? Like, imagine that world now. This simplifies everything so much, because I get my identifier right here. I know the version, I know the name.
And if I need to resolve, from GitHub in various ways, and this isn't currently published, I have something that tells me how to get access to it somewhere else. So maybe we could even have that in our manifest as, like, a private thing that doesn't get published, maybe we have it somewhere else, but, like, I can see that totally working, and I really like the simplification.
Oh, go ahead, Lawrence, sorry, I didn't see your hand.
Laurent Querel 00:22:26 No, no problem. Yeah, just reacting to the removal of the name in the list of dependencies.
The initial intent there was to… optionally specify, an alias.
For, conflict resolution.
We don't need that right now, but at some point, I think we will have to reintroduce it.
Maybe not like a name, I agree, maybe like an alias, so it's explicit, but at least we could use this, the syntax that we propose at some point. When we have a conflict detected by Weaver, then we can use the alias to specify which registry explicitly we want to target.
An example of that could be…
I don't think there is any option to prevent someone using a signal exactly the same than another library order.
So we… we need this, conflict, resolution with an alias to let the, let's say, the person,
Making a dependence to these two libraries, specifying which one they want,
When there is a search complete.
Liudmila Molkova 00:23:48 Yeah, I think what Josh is suggesting, that it's, in fact, a part of this URL, it's everything before version.
Laurent Querel 00:23:55 Yeah, but it's too long, that's why, yeah. I think that the alias is there to avoid this gigantic,
Pass plus surname, in every place where you want to remove the conflict.
I mean, it's like the an alias for a use or an import in languages, it's nothing different.
Liudmila Molkova 00:24:19 And we can… there are ways we can work with it, but it's the schema URL, and if you intend to publish it, it should be short.
You wouldn't put a gigantic string in your schema URL anyway.
Laurent Querel 00:24:33 I mean, you… If you have the domain name plus the pass, I mean, it's…
I don't see why it's,
how that could be enforced to be small. I mean, for me, it's,
So, what is the problem with an alias, just to understand your point, Vimilia?
Liudmila Molkova 00:24:58 My main…
Laurent Querel 00:24:59 Fits of children, easily.
Liudmila Molkova 00:25:01 My main problem with Zalia is that it doesn't guarantee any uniqueness, especially global uniqueness.
Laurent Querel 00:25:08 Oh, it will. You will have, so, I mean, the dependencies will enforce the fact that alias in this list are unique.
Josh Suereth 00:25:16 No, so… so I don't think we need global unique lists. I'm gonna… I'm gonna… I… so, I think we need aliases eventually. I don't think we need them initially. I think we need them eventually. They don't have to be global unique, because what we can do is when we publish, we erase all the aliases.
Right? Like, again, this is a step for resolution. You need to know, like, when I publish what I've done, I have no… I have no aliases listed, because I don't… I'm not… that's an internal detail for how I implemented my registry. It's like an import statement.
I'm not going to expose my imports, right, when I publish. That's not necessarily needed.
unless I'm publish… like, republishing that data, maybe I… anyway, we gotta sort that out, but that's… that's a different thing.
Liudmila Molkova 00:26:01 You need global uniqueness because of the… you need global uniqueness because of the transitive dependencies, because you don't know what you take dependency on.
Josh Suereth 00:26:12 Which means both the things you're saying are true. We need a globally unique way to reference a specific, like, metric from a registry.
But the user might want to use an alias locally that only has to be consistent locally. As long as the resolution step erases all the local aliases to be global ones when it publishes, everything's gravy.
Laurent Querel 00:26:35 Yeah, that's lucky, that's… that's maintenance.
Josh Suereth 00:26:38 Yeah.
So, so I think, like, you're both 100% correct, it's just, like, I think they're complementary.
Right? Like, we can do both of these things, and that's what I'd propose going forward.
Liudmila Molkova 00:26:56 As long as we find a good name for it. If we call it name or ID, then I… I will complain.
Laurent Querel 00:27:02 An alias, I think that's what the ads in ROS, or the alias that we have in Go, I mean.
I think they are Namelias, or something like that.
Josh Suereth 00:27:15 Yeah, if you want to be really convoluted, we just say as.
Liudmila Molkova 00:27:20 S.
Laurent Querel 00:27:22 Yeah, that's also, okay.
Josh Suereth 00:27:24 No, no, I hate as. I was gonna, I was gonna say thingy as, like, another option to be terrible. That's worse than ID, right?
Anyway, let's, let's, let's move on. I think,
I really like what you're doing here, Lyudmila, and this does make me think that there will be a version of Manifest that is published, and a version of Manifest that is used for, like, resolution, possibly, where there might be some extra things that I use locally, like alias, that I would never put into published.
Liudmila Molkova 00:27:59 Yeah, I think that's what Lauren suggested in the Whatab, that we have a definition manifest and resolved manifest, and they are
different. So then, in this proposal, if we marry it with yours, instead of name and version, we would have schema URL as the
First, thing.
And then, for dependencies, we would repeat it, we would not have…
Anything like that. Okay, I'll, I'll update it. I think I, I, yeah, we can leave it.
Josh Suereth 00:28:33 Yeah, I… okay, I think that resolves this topic. That was good discussion.
Alright, do we have… are we gonna run out of time for everything else? Alright, cool. Next, file format definition 2 versus version 2.
Give up…
Liudmila Molkova 00:28:50 Yeah.
Josh Suereth 00:28:50 December here, not helpful.
Liudmila Molkova 00:28:52 Yeah, you… you reviewed my PR, and yeah, it's a… I used to have
somewhere there, and I think you're right, it's not… helping. It creates so much…
problems, that it's not worth it, and it's not common for definition languages to have… to support somber.
Josh Suereth 00:29:14 It's hella rare to change the version of your syntax, honestly, in a language. Like, think of Python 2 versus 3.
Liudmila Molkova 00:29:22 Yeah, and even when it's configurable, the Python 2 versus 3, yeah, but if you look into, let's say, C Sharp, it's just the major version. They never mentioned the… there is nothing like intermediary version. There is no patch you would send.
So… Let's just…
make the practical thing, let's call it definition slash 2. My main concern is around version, because version is ambiguous, we've used version everywhere.
We call it follow file format in different places, so let's use definition slash 2, and eventually it will become a default.
So nobody would need to write it.
Josh Suereth 00:29:59 That, okay, I'm fine with that. The only thing… the only caveat I'll have is,
How breaking do we want to make this?
Right? Do you think people are using version 2 syntax today? I know Weaver Packages is.
So, do you want to just, like, crack the world and say version is now definition slash? Or are we going to be flexible and say, if you see version of 2, we're gonna handle it for a while, and we're gonna have a migration period, all that kind of crap, right?
Liudmila Molkova 00:30:31 Okay, if you think it's important, let's… Here's,
Let's have the graceful period and support version as well.
Josh Suereth 00:30:43 Okay. Yeah, I'm just thinking we, for,
We should just be more sensitive, because we're starting to get usage, that's all.
Liudmila Molkova 00:30:54 It's an alpha, but okay.
Josh Suereth 00:30:56 I know it's an alpha, and I would be okay if you said, you know what, it's not worth it, let's just crack the world and break it, that's fine.
Like, I'd be behind that. We'll just announce it as a big breaking change. I think it's more important we get to the point where people can depend on V2 than anything else. So…
Thoughtfulness at work, really? Okay.
Yeah. Anyway, cool, I like this. This works for me.
Let's move forward.
Oh, next steps on V2 syntax. I want to have a brief discussion. Doesn't have to be terribly complicated. In the original proposal for V2 syntax, so I can wait for your change here, Lydmela, before I work on this, but, I'd like to change imports to be able to import spans, now that we have a span type we can rely on.
I would also like to change imports to include… What else is missing?
I think attribute groups.
Liudmila Molkova 00:32:01 We can't import attribute groups.
Josh Suereth 00:32:04 We can only import 3 things today, which I think are spans, entities, and events.
or not spent, sorry. Metrics, entities, and events. Those are the only things you can import. So attribute groups do not get exported.
pure attributes don't get exported. You can't import those. I don't know if we want to say, like, import this from the attribute registry.
And then attribute groups cannot be imported.
So, I don't think it's hard to add all 3 of those, and thank you, Jeremy, for your review. I didn't realize I left a bunch of to-dos in there, that is now cleaned up, so it's less ugly. But I think, like, adding those imports shouldn't be too hard.
we have the notion of public attribute groups, we can import those. I think that I'd like to add that in the syntax.
Just for consistency. When Jem and I wrote those docs that ended up derailing real far, the initial ones made me realize that the only way to include, like, SEMCOM in your registry today is by using the include all unreferenced flag.
that… I'm not super happy with that going forward. I kind of don't…
I want to talk about that flag later, not today, but I would like to get rid of that flag at some point.
So… okay.
Refinements. Any… go ahead.
Liudmila Molkova 00:33:34 We've had some concerns about attribute groups in general.
And I think we're…
if we still have these concerns, we might not need to import them, but I think they were important to Jeremy, if I remember correctly, for the importing purposes.
Jeremy, are you… are you here? Sorry.
Jeremy Blythe 00:34:00 I was… I was just about to type in the chat, got to go. But,
Sorry, what were you saying?
what…
Liudmila Molkova 00:34:10 We can talk about that, bud.
Josh Suereth 00:34:12 We can talk about it later, it's fine. I'll tell you what, for now.
We'll add imports for spans, and we'll skip attribute groups.
But we'll just… we'll just do it piece now, we can figure out as we go. There'll be separate PRs.
Jeremy Blythe 00:34:25 Sorry, I need to disappear.
Josh Suereth 00:34:27 Of course.
Jeremy Blythe 00:34:28 Cheers.
Laurent Querel 00:34:28 Yes.
Sorry.
Josh Suereth 00:34:33 Okay, refinements.
Cool. There's a syntax, I think, in the original proposal you had with Melan, for V2 that has refinements. I think I'm just gonna implement it, because the lack of refinements in V2 syntax is problematic.
I think we need it.
to actually mark V2 done.
Liudmila Molkova 00:34:56 Yeah, probably.
Josh Suereth 00:34:58 Okay. At least I'll open a ticket about it. I don't know if somebody else has time, feel free. But I think…
Currently refinements don't work, and importing
refinements, is the next question, but I… anyway, let's hold off on that. We'll move on to the next set of topics quick.
How do we feel about the DocBot?
I don't know if you were here when I was saying this, Lydmella, but I was saying… I asked it to go generate docs for multi-registry, and I think it did a good job for V1.
And then you asked it to do V2, and it just went off the rails.
Liudmila Molkova 00:35:39 Okay.
Josh Suereth 00:35:40 Like, just so… I love… I think you were asking us this question?
And I love that it gave you some random answer.
Yeah, like, do we… so I just wanted to ask, like, with this and how it went off the rails.
I could… there's… I could hold off the CL until schema V2 is better, and then we can ask it, like, re-prompt it to do docs for V2 and multi-registry, because I think it did a decent job with V2. And I think, you know, some of this…
this kind of change is important for us to do with V2, but just since V2 isn't stable, I think it's having trouble, and it's matching the rest of the docs and stuff.
Overall, though, Is this wasting our time, or is this helping?
Liudmila Molkova 00:36:34 I think this is helping, in a way that you initiated.
And I'm forced to correct its stupid mistakes.
Josh Suereth 00:36:45 Hopefully, I, I would do that. Where did spans come from? It's not quite useful here, right?
Liudmila Molkova 00:36:54 So, it was some iteration. I asked it to do some examples. Oh, actually, I wanted it to…
maybe we don't support it yet, that's why. I wanted to import the metric and refine it, and because we don't support it, it tried all the different things and tried to gaslight me that it did all the job.
Josh Suereth 00:37:17 Yeah, and it can't, because it's not actually supported yet. Yeah. The gaslighting it does is awesome. I don't know if you saw, the,
The files changed, but my favorite was you'd ask it to do something, and it would, like, modify something here, and just delete this entire section by accident.
And then you're like, hey, bring that section back. It's like, okay, sure. So, like.
What I don't want to do is turn our project into, playing with the bot.
What I want this to be is, like, okay, we find value in it, and I know that we have documentation gaps. Oh, I'm not… I'm not showing what I was rendering. Yeah, yeah. So it'd be like… I forget, I think it might have been this one, where, like, you made a change here, you asked for a change here, and it just deleted this for some reason.
So toying with the bot, I think, is fun, but the real need is we need better docs.
And what I'd love to do is have us focus on writing really good unit tests and really good features, and see if this can help us
you know, fix specific doc sections, right? Of, like, we're missing documentation on this thing, go write this, and it accelerates us. If it's not doing that, I will stop making PRs and sending them for review.
Oh, God.
Liudmila Molkova 00:38:37 I think we have actually… we will have actually good tests in the Weaver packages, where we have cleaner data, and it's end-to-end.
I would… you would run the actual CLI.
Josh Suereth 00:38:51 Yeah.
Liudmila Molkova 00:38:52 Today, we test Rust against Rust, right? And we miss, like, the end user part of it.
We don't even see the generated resolve schema. We don't even generate the resolve schema, we generate the materialized schema.
Josh Suereth 00:39:12 Or the bots.
Gotcha. So, that actually seems like this is a thing we could do…
just as a development practice, is basically, start making better end-to-end tests in Weaver. I think Jeremy mentioned this as well, the…
resolved manifest thing, where we're resolving V2 schema.
There is no way for you to use Weaver
And have a V2 dependency in real life. I manually wrote that file.
Myself, for the test.
Because we don't have the published pieces of done, so the whole end-to-end story.
That's why it was gaslighting you, because it literally can't verify.
Yeah, me… okay, I'm gonna… I'm gonna take that as a note. I… I still think we're finding valuable lessons when it hallucinates of things where our documentation's unclear, so I'd like to continue using it. I just wanted to do a quick vibe check of,
Do we hate it?
Liudmila Molkova 00:40:14 Or… Maybe we could… Yeah.
Josh Suereth 00:40:17 Go ahead.
Liudmila Molkova 00:40:17 Maybe, maybe we could, update the docsAgent file to tell it to document V2 schema only?
And, yep.
The other common comment I have, it's probably minor, that it over-explains, oh, this is how it's called in Rust. Who cares how it's called in Rust in the public user-facing documentation about schema?
Josh Suereth 00:40:41 you know, include now.
Rust memes things. What was the other one? Don't, use V2 syntax.
Liudmila Molkova 00:40:50 Yeah.
Josh Suereth 00:40:55 Yeah, I think that'd be good. So let's… let's update those instructions then and try again. Cool.
I… for this PR specifically, should we give up on it?
Or should we… I was thinking just…
Update instructions, give up on it, retry.
Liudmila Molkova 00:41:12 Maybe we should do your thi- the- the…
The manifest things we discussed today first, because it will be a big change for it anyway.
Josh Suereth 00:41:22 Okay.
Alright, so I will close that query. Close the current… PR,
Reopen with saved prompt once manifest changes land.
with better… End-to-end integration tests. Okay, cool.
That sounds like a plan.
I saw a hand there, but .
neil yashinsky 00:41:50 It was me, Josh. I was just gonna say, briefly, on your question about the bots and how much of a waste of time it is or not, I think it's important to have, and I think the bot will only be as good as, you know, the interactions with the users and testing, et cetera, that make it.
And so I think it's a… it is an important thing to include, not maybe more important than the docs to start, but, you know, programmatically, from an adoption standpoint, may be more important in the long term.
Josh Suereth 00:42:18 Yeah.
Cool.
That's kind of my intuition as well. I don't know if we need more bots as well either yet, but Docs is just the biggest gaping hole we need to resolve.
Cool. Let's move on to, our Weaver projects. So we have, I'm gonna ignore some kind of tooling. I think most of what we need from there is migrated over, some is not.
But I wanted to go through to consider for next release. Jeremy's not here, unfortunately.
And Lawrence, but, yeah.
This is one that I… my question here for… for you, Lyudmila.
Do you think this is important enough for us to figure out before we declare V2 stable, or is this something you think we can evolve?
Liudmila Molkova 00:43:08 It's important enough, but not before we finish with you.
Josh Suereth 00:43:13 Okay.
Yeah, I need to… I don't know what, if Alexandra's even working on it, so I'll try to ping her later.
Okay, receiver should resolve full URL.
Liudmila Molkova 00:43:27 This actually is probably impor- very important.
Especially in multi-registry.
Because you cannot even… Imagine.
Where the document came from.
Josh Suereth 00:43:43 Yeah.
This is in error messages, right? Like, you want the provenance to list out the full URL?
Liudmila Molkova 00:43:49 Oh, no, this is in the markdown, so when we run their markdown.
Josh Suereth 00:43:54 Definitely.
Liudmila Molkova 00:43:54 pass. We need the… Maybe we should have a policy that we overwrite this, to…
To the fuller result URL, right?
Josh Suereth 00:44:08 Yeah, I think we could have a policy there. What we need is… I remember this now. Our Markdown renderer is… is…
fun. We probably need some kind of configuration to say, I want my URLs to be, absolute, and here's the configuration for how to do it.
Liudmila Molkova 00:44:33 We have this configuration for… Generate Markdown.
Or for update markdown.
Josh Suereth 00:44:44 It… it's… it's… it's hacked in.
like, I did that. It is… there is a command line flag that you pass for what the base URL should be, and then all of our templates know to use that flag and do it.
What it doesn't do is when you get a URL in Markdown, like, like, nested, it does not change those. It only changes the absolute URL of things that it is creating in Jinja.
So we need something where when we say, here is a crap ton of markdown coming out of…
the YAML file, We need to parse through it and change all the links to be absolute, right?
We don't expose a way to do that in Jinja today.
Liudmila Molkova 00:45:31 Well, I'm in uke.
Someone can probably write the ginger helper, but should it be a ginger, or should it be a rust?
I think it's… So we shouldn't be arrested.
Josh Suereth 00:45:42 Rust, yeah. And it can be a Jinja filter, but it probably needs to be, Rust code that does that. It's gonna be… we have a… for context, we have a Rust library that does a crap ton of Markdown parsing today for the comment filter.
Do you remember the… all the bugs we had with Java comment formatting back in the day?
Liudmila Molkova 00:46:09 Yeah.
Josh Suereth 00:46:10 So legit… that was so annoying to fix. Legitimately…
we are… I think it's under extensions. I'll see if I can show this to you.
Is it under code?
Yeah.
Where is this? So there is a…
Let's test, let's comment, let's HTML.
Might be under…
Here it is.
Okay, so we have this Markdown render thing.
And what this actually does… We have one for HTML as well.
Where is the thing I'm looking for?
Let's try new, here's render, we render the markdown.
to Markdown AST. So, we get a markdown AST.
And then we take that and we fire it through a listener.
That will look at each possible node and render it back to a string.
And so, this is, like, some of the most insane things. Like, oh, if it's HTML, we do this. If it's inline code, we do this. If it's code, we do this, right? And there's… if it's a link, here's how we render links.
And so we have the capability here, where if we get a URL,
We have this shortcut reference links, which we support today.
We have the capability here to say, cool, We can change the link.
but the problem is, you know, right now.
This method and mechanism is only used in the comment filter.
And we're using it to make, like, Java not broken, and Go comments not broken, and Python comments not broken. I don't think SemComf uses it.
I… yeah, we probably need some kind of a markdown filter to say, here's a block of text which is markdown, go fix all my links in that markdown, and then feed it to the next filter.
Yeah, I'm not looking… maybe, maybe this is a good vibe code opportunity, because this is not particularly elegant code, but it's pretty rote and, like, dumb and, like, you know.
I think this… that might be a good opportunity for us to… to, describe what we want and give it to a…
neil yashinsky 00:48:47 bot, and see if it can do it for us.
Josh Suereth 00:48:49 It's gonna be a lot of code.
Yeah, go ahead.
neil yashinsky 00:48:52 Did somebody say rote and dumb?
Josh Suereth 00:48:55 Yes.
neil yashinsky 00:48:56 My ears perked up! Yes! I really wasn't looking to do too much contributions here, but I feel like this one might be, if you guys are okay with me helping out on this one.
Josh Suereth 00:49:10 Yeah, I'll tell you what, I don't know if I'll be able to do this right now, but,
we… We have a straw man to… this, this is not it. New proposal.
We should provide a Jinja template.
Virginia filter function.
I can take in Markdown.
parse it, and modify the URLs in links found Within it to be absolute.
To some base path.
Something like… Let's see… does Jinja work yet for syntax highlighting?
my field…
Liudmila Molkova 00:50:02 You're not sharing, by the way.
Josh Suereth 00:50:04 Oh my god, I'm sorry.
This one here.
something like my field markdown pass, you know, Mink.
Markdown.
links.
Absolutes.
And then… Bye.
Absolute path.
But, next.
Winter.
Something like this, right?
Yeah. Right. And so, if you want to look inside of, inside of Weaver, there's a Crates Weaver Forge.
And inside of We Reforged, there's this extension source, and a form… That's where we put all of our…
Rust code that does fancy things for Jinja, and that's how we expose templates. Yeah, if you wanted to expose a Jinja template that basically takes in Markdown, parses it, converts all the links, and then spits it back out, that's kind of what I'm thinking would solve this.
neil yashinsky 00:51:10 Yeah, makes sense. I've done something similar, I think.
Josh Suereth 00:51:13 Yeah. Yeah, so this is, $7.56, if you want to take it.
neil yashinsky 00:51:18 Sure, I will take it. It would be easier for me if you assigned it to me, but I can figure out how to do it myself if you need me.
Josh Suereth 00:51:26 Yeah, what's your…
neil yashinsky 00:51:28 I'm not in… it's N-E-I-L?
Dash the?
dash… Knowledgeable without the K in front. So, N-O-W-L-E-D-D…
Josh Suereth 00:51:43 Until you're… you're in the hotel aura.
neil yashinsky 00:51:45 Right, I agree.
Josh Suereth 00:51:46 I'm not gonna be able to assign it to you, yeah.
neil yashinsky 00:51:47 Yeah, exactly. So I can… but I can, create the code or whatever, I'll just watch this issue, and then I'll submit the code, which is totally fine by me, and then we can just get it merged however, right? It doesn't matter…
Josh Suereth 00:52:00 Yep, and then, that's impetus to join the community then, too, once you start making contributions like that.
Cool.
neil yashinsky 00:52:06 Yeah, that's, that's, perfect.
Josh Suereth 00:52:10 Alright, what else do we have here? Weaver should resolve. Weaver, registry diff, template extension, weirdness. This one, I think we figured out, Ludmela, do you know what the issue was?
Liudmila Molkova 00:52:24 No… Tell me.
Josh Suereth 00:52:27 Don't have a fix yet. When we render YAML,
We're using the Jinja template for YAML, which renders YAML that can render in HTML, not just pure YAML. So we're removing Jinja from YAML.
So that it goes not through Jinja.
Liudmila Molkova 00:52:45 I see, yeah, it makes sense now.
Josh Suereth 00:52:48 So Jeremy's working on that. So that, that will get resolved. Alright, strict mode for Jinja 2 behind CLI option. I think this, this was a great contribution. I don't remember what happened to this.
Okay.
Liudmila Molkova 00:53:02 There was no contribution, it was a bug.
Josh Suereth 00:53:06 It was just a bug.
Liudmila Molkova 00:53:07 Do we have an opportunity to… we have an opportunity to enforce it with V2. So if somebody uses V2, we can also enable strict Ginger, can we?
Josh Suereth 00:53:19 Do you think Strict Ninja's worth it?
I guess it's fine. There's just… like, sometimes I write templates that are supposed to not do anything when it references something that's not there for compatibility reasons, instead of having to if-else everything in Jinja.
But, yeah, that's fine.
Liudmila Molkova 00:53:40 I mean, if you feel, like, not strict is fine, it could be a flag, but then it's… it's… there is no urgency in this. It's just a minor inconvenience.
Josh Suereth 00:53:53 We can try it with V2 and see if we get lots of complaints.
That sounds fine.
So if the V2 flag is sent, we'll be strict in Jinja.
Liudmila Molkova 00:54:05 Yeah, we could do this.
Josh Suereth 00:54:06 Yeah, and then we can have a relaxed mode instead of a strict mode.
Liudmila Molkova 00:54:10 Yeah, good point.
Josh Suereth 00:54:11 Okay.
Cool. Weaver cannot load registry directory beginning with dot. This one…
Oh, this is about hidden directories, where we don't search through hidden directories.
Because we're actually pretty aggressive with hitting your…
File system, and so we don't want to overwhelm you.
Alright, that's gonna be a bug. I don't think that relates to V2 in any way, that's just a… that's a TBD.
Authenticate when using remote, again, not really to V2. Alright, figure out extends feature in V2 spec. I think this is the refinement stuff, and this is what I'm planning to work on next.
Where we were talking about having metric refinements.
So here's the strawman proposal. I was thinking that this might be a next good step outside of the resolution dependency stuff.
But I think this has to get in before V2 could be done.
Liudmila Molkova 00:55:15 Yeah, otherwise we cannot produce a good schema we would preserve, right?
Josh Suereth 00:55:22 Okay. So, Ludmila, if you're working on the,
manifest stuff, I'll work on this for now, because I think that doesn't conflict at all.
Liudmila Molkova 00:55:31 And then, when you're finished with manifest, I'll switch back onto dependencies.
Sounds good.
Josh Suereth 00:55:37 Great.
Okay, what else do we have?
Alright, so the… I wanted to do a brief… we have a couple things. We have to consider for next release. We have things that are no status, which have come in, that we can look at.
We have V2 schema-related work, which, obviously, I want to get this prioritized.
For V2, we only have 5 minutes, so we're not gonna do that right now. We have ease of use things. Go ahead.
Liudmila Molkova 00:56:05 Can we come back for a second to the multi-registry manifest? I wanted to…
Ask your opinion on something.
I updated the comment.
It's, 11, 97.
Josh Suereth 00:56:22 1197… is that in here?
Liudmila Molkova 00:56:25 I don't… I didn't know.
Is it? It is, in vitro schema.
Josh Suereth 00:56:30 Good.
Liudmila Molkova 00:56:32 Yeah, this one.
So, can you scroll down?
So I posted the comment as the outcome of our discussion.
So, what it would mean, initially.
That we also need the config to…
Say where the schema comes from.
Just for the development, because… Where…
won't be able… so if, let's say, if we use something as a dependency, we need it to be published before we can even test anything. So, like, for our current local and testing goals.
We need to… Developed this custom repository mechanism already.
Josh Suereth 00:57:22 Yeah, I think that's fine. You've seen how,
how that's done for, like, Rust crates, where you can say, cool, I depend on this crate, but by the way, grab it from this good repo instead of where you normally get it.
I'm fine… I'm fine with that. So basically, we'd have schema URL, and then we would have something that's like a… a definition time override of grab it from here right now.
Yeah.
Liudmila Molkova 00:57:48 Yeah.
Oh, it could be just another property here.
Cool.
Josh Suereth 00:57:56 Yeah.
Liudmila Molkova 00:57:57 Yeah, that sounds good.
Josh Suereth 00:57:59 Cool.
I like it.
So, I think this one's higher priority than at the bottom, and I think I want to get this…
V2 schema stuff sorted by priority of, like, what we consider
blocking, stabilizing V2, and what we consider something we can add on later in non-breaking ways. I… I still think ease of use needs to be highly prioritized across Weaver.
And, like, we need to make fixes, we need to get better docs, that sort of thing. So, I want to keep this here, but I'm curious how folks feel about, right now, the way we run the project is we have things that come in that need to be triaged, and we haven't triaged in a little bit, so there's a lot here.
We have things we're gonna consider to release next, and then when we do a release planning session, which we'll probably do in about a week or two.
We'll throw things that are still in progress into next release, so we can block the release until they're done.
And then we have these grab bag of, like, high priority, you know, our current efforts. And I think our major efforts are getting V2 schema out the door, and ease of use.
Are we happy with this, is how we run the project?
Like, I still feel like…
I feel like a failure as a product manager, generally, in open source. Because there's so many things here that, you know, don't make progress, but I do feel like we are making progress as a project.
And I do want to track this and keep this as our roadmap to, like, tell people what we care about, what we're interested in as a project. When you come in, I'd love for this to be, come in, look at the top priority things, grab one without a name, and work on it, right?
Liudmila Molkova 00:59:51 I feel like once we do the V2 and Federation, we'll spend the rest of the year
fixing issues and the usability problems of this. So, like, we are more reactive than strategic.
And it's probably fine, at least now.
Josh Suereth 01:00:08 Okay, okay.
Cool. Well, I… I do think I'm gonna propose at some point that we put a block here behind V2 for, MCP and the UI.
Because at least the current UI PR is huge.
And I think the MCP stuff will actually be pretty cool to flesh out, like, what we can do with it, and what,
What use cases we want.
Liudmila Molkova 01:00:40 I'm jealous. I want to play with MCP and UI.
But I don't get to.
Josh Suereth 01:00:46 To be fair, if you ask Jeremy and, and I think the contributor, they've been viboding the whole thing, so is that them playing with the UI, or, like, playing… playing with the code for the UI, or playing with the UI?
Liudmila Molkova 01:01:00 Okay, yeah, yeah, that's, that's separate.
Josh Suereth 01:01:02 Yeah.
Yeah, which one… which one do you want to play with? That's the question.
Liudmila Molkova 01:01:06 I want to play with the actual UI and see where we can use it and how we can build, all the other stuff we wanted to build on top of it.
Josh Suereth 01:01:17 I should give you a demo, but I… I don't… I don't have Weaver built right now in… in a stable state, but .
Liudmila Molkova 01:01:25 You know that you can JQ expressions. You know you can do JQ expressions in the UI today.
Josh Suereth 01:01:30 So you should try it.
Yeah, okay, alright. Thanks, everybody. We'll see you next week.
Liudmila Molkova 01:01:36 Thank you.
neil yashinsky 01:01:36 Thank you, bye.
