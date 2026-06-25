SIG: Semantic Convention Tooling
Date: 2026-06-24
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:02 Recorded.
**Liudmila Molkova** 04:36 Hello! Hi, John.
Sorry.
**Josh Suereth** 04:40 No worries.
Might be a one-on-one today.
**Liudmila Molkova** 04:45 Okay.
So… We can figure everything out.
**Josh Suereth** 04:52 For what?
**Liudmila Molkova** 04:53 Oh, doesn't matter.
**Josh Suereth** 04:56 Cool. So… I have two things.
Actually, I have three things, because I was actually going to look… I was looking at, Yeah, good question, right?
Okay, so, release process, we broke… all of the tests on Weaver packages, even though all of the Weaver packages are still fine, because we added a new error.
And since all the tests are about Weaver policies, it actually looks at each individual error, and since a new error showed up, it's not in the filter.
So they all fell.
Like, all the builds are now failing, so all the dependency upgrades. I can show you.
**Liudmila Molkova** 05:58 Yeah.
Is it the requirement level warning.
**Josh Suereth** 06:03 Yeah, I mean, it's… we didn't… we literally didn't break anything.
We just broke the tests.
Which tells me we have either flaky tests, or we have to do something here. I'm not 100% certain what, but, So, we have… like, when we're testing a policy package, I'm thinking… that I might want to change the test suite.
Today, it ignores, like, V2 tests.
But maybe we need to change it so that, The policy error test only looks for things that come from policies?
because this is a little frustrating, right? Like, I don't want to have to go upgrade everything Or go change expectations every time we add a new error message in Weaver that's out of the box.
That seems like that's too flaky, because the policy is still catching… if you… I mean, you can't tell, but with a diff, but here's a policy finding, right? So the policy is still catching all the errors it's supposed to, everything's working, it's just the new warning is showing up in the list of errors it checks to see if it, you know, if it… and it does a direct diff, it doesn't do, like, a fuzzy match.
**Liudmila Molkova** 07:20 Oh, so if we parsed the…
**Josh Suereth** 07:23 Yeah, I'll show you.
we have, I'm doing some shenanigans here, so, you know.
This, this is, this is a fine hack. But when we… when we… matches test filter… where is it? Checkout book.
So what we do is we're actually grabbing… We're grabbing all the diagnostic messages.
Or, sorry, we're grabbing all of the errors that come out, and we're ignoring ones that don't contain is not yet stable.
as the, like, get rid of Weaver out of the box errors, but that filter's bad.
So, what I'm thinking about doing, and I'm curious how you feel about this, is right now… We also normalize all of them, but I'm thinking about getting rid of anything that is not a… that doesn't come from policy.
violations. So I think that we have a type exposed, I need to go look at it. And so that we only, when we do a policy test, we're only looking at errors that came from the policy, we're not looking at things Weaver has out of the box. So if we make a change in Weaver, we're not breaking all the policy package tests.
**Liudmila Molkova** 08:35 Okay.
Alright.
**Josh Suereth** 08:37 Reasonable.
**Liudmila Molkova** 08:39 Yeah. How do you feel about rewriting those tests in something?
**Josh Suereth** 08:45 I had proposed that initially.
And everyone was like, okay, we'll just throw it in a big shell script, because we can get it done quickly. I'm like, fine. I had an agent write up the shell script, I validated… well, actually, sorry, I wrote a crap ton of the shell script. I had an agent do all the annoying tidbits.
And I was like, fine, we're good enough, right?
If we want to rewrite it, that's fine. I don't have time to at this point. Like, I did when we first wrote it, I don't now.
**Liudmila Molkova** 09:17 I mean… It's, it's PRI, birth.
But it won't change things. If we were to rewrite it, it would be… I don't know, we can do it in Regal, right? Because we use Regal for semantic conventions.
And it would not Fail, would it?
It didn't fail.
**Josh Suereth** 09:41 we… we could… I mean, the difference is, I'm actually trying to run… so if you look at… if you look at a test harness, right?
Let's pick a policy, kind of know backwards compatibility, right?
There is some sophistication here, so if you look at, like, metrics.
it actually supports having multiple registries, right? And then it has the expected diagnostic output. So this is the output that we are normalizing with JQ.
Where we're trying to only pull out diagnostics that make sense. But I think what I can actually do… is I can look for, I can ignore diagnostic… well, no, diagnostic message is fine. I can actually, I think, only pull out policy finding types.
Because… those are the only kind that get exported by a Weaver pack, and then we're fine. And I think I can update the shell script, it's literally that one-line JQ expression.
**Liudmila Molkova** 10:36 Okay, yeah, that's cool. So this is unrelated. Maybe I'll create an issue here, asking to convert it into… some human language? Well, not bash, And we decide which, and if somebody wants to contribute it.
will support, but I think we need to decide which language.
**Josh Suereth** 11:03 Yes. Agreed.
We did get some template output changes, though.
And I'm not sure why.
So we're getting TBD for spam names.
With the latest.
**Liudmila Molkova** 11:18 Oh, because it's a fix.
So we have, we have a span… Name property.
And it is TBD in the schema.
But we used to, instead of using this property, we used to fall back to the span type.
**Josh Suereth** 11:41 Okay, okay, I see.
So we actually… we're actually using the span name now instead of following the span type. Okay, gotcha. So that was a fix. So this is legitimately a… this is a legit fix breakage that we need to go update the templates for. Okay.
Cool.
**Liudmila Molkova** 11:59 Yep. I can do this if you want.
**Josh Suereth** 12:02 Yeah, if you do that, I'll do the other side, although, we kind of probably have to do both of them together.
Because you can't see one or the other, because the tests are broken, yeah. So, it's easy to do either one. Like, this one… this one's easy, because basically you just rerun the tests, and then you can copy the output into the expected, and you're good to go, you know? Because we know that this is the… this is the behavior we want. So, that's the other thing you want to check up on.
**Liudmila Molkova** 12:29 Just change CBD to something more meaningful.
**Josh Suereth** 12:32 I mean, I can… I can…
**Liudmila Molkova** 12:34 Okay, yeah, whatever.
**Josh Suereth** 12:35 meaningful to me, that's fine.
**Liudmila Molkova** 12:37 Okay, okay.
**Josh Suereth** 12:38 Like, as long as testing the behavior's correct is what I care about. Anyway, I'll get that updated, because we have… we just have some minor things to fix here. It is interesting, it updated Weaver immediately. I thought we had to do one of these before it would actually merge things in, right?
So… Anyway… Maybe I will merge this PR with my PR, so we get everything up to date all at once.
**Liudmila Molkova** 13:06 Yeah.
Okay.
**Josh Suereth** 13:08 Alright.
Sounds good. Let's go back to some discussion, then.
Definition manifest versus resolve manifest. Oh, maybe, maybe I'll put this at… this… this can be a sub-discussion, actually.
I do want to have some friction discussions on manifests, but… a few things in here that I made changes to. I'm gonna mark comments resolved. I didn't have a chance to do it this morning. I'm, like, behind on everything. Okay, where are your com… actually, we'll go to conversation to get to your comments. So… I had a panic here where there's a degenerate case where someone overrides a schema UR… like, I assume that when you resolve a schema URL, the thing you resolve has the same schema URL in it.
**Liudmila Molkova** 14:03 Okay.
**Josh Suereth** 14:04 And if that doesn't work, my whole algorithm falls apart and dies.
And Jeremy, correctly, pointed that out, right? So what I'm doing now, this now issues an error.
wind.
You can try to resolve a schema URL, but get different.
URL, run to the location, we resolve it.
So you're not able to override and say, I want to grab, you know, schema version X from schema version Y. You're not allowed to do that right now. And I think that's a good step one. We can figure that out and loosen that restriction later.
But that, just for context, that's one of the things I did.
The second is, We have this issue with the tests, where we're trying to allocate ports, and we were allocating ports semi-consistently, but I ran into this issue where, on my machine, somehow, I would always get tests running in parallel that had the same port, and then the test suite was always crashing.
And Jeremy was not getting that issue.
So, just slapped up a real fast file system lock. Tests are run in different processes, so effectively, you try to grab the lock, try to grab a port from the file.
And then, if you can't grab the lock within, I think it's, like, 2 seconds or something, because someone forgot to unlock it, you kill the file and… Or try again, something like that. Which actually doesn't work in Windows, by the way. If you're in Windows and someone kills the file lock, you have to reboot, last I checked.
**Liudmila Molkova** 15:45 Oh, wow. Okay.
**Josh Suereth** 15:47 like, it might be, like, maybe in, like, 5 or 10 minutes it unlocks, but I… yeah.
Oh, that's from Built Cool Fund.
**Liudmila Molkova** 16:00 The test never passed on Windows, anyway. There is a sim link test that always failed, and I… I never…
**Josh Suereth** 16:08 Even in the.
**Liudmila Molkova** 16:08 investigated it. So, I think if nobody complains, then nobody cares.
**Josh Suereth** 16:13 Yeah, I started using junctions in Windows, and I hate myself for doing it, but I don't really want Weaver to do junctions. I don't know if you're familiar with those.
**Liudmila Molkova** 16:22 No, I'm not…
**Josh Suereth** 16:23 It's… it's the Windows equivalent of a SimLink.
**Liudmila Molkova** 16:26 Oh, I see.
**Josh Suereth** 16:29 Yeah, so you can do swim links in Windows, they're called junctions. I'm using them for my, like, one of my personal projects, and it's, It's exciting.
I'll just say that.
**Liudmila Molkova** 16:43 Yeah.
**Josh Suereth** 16:43 Okay.
So, that was that, okay, fix this to have hard timeout. The other… the other thing in this was… some of your questions. I added, a normalized schema thing. All it does is actually just get rid of slash on the end.
I don't know what other normalization we want to do, like, if we want to add, you know, whatever, but I did a bare minimum of normalization, and I think we should follow up on this. So I'm gonna mark this resolved, yeah.
Minimum.
Normalization. I do think we probably need to, like, come up with a normalization standard for schema URL. I tackled normalization when you instantiate schema URL in Weaver. So anytime you call new schema URL with string, it normalizes as it grades it.
Okay.
Cool.
Yeah, this is, this is something I do want to add in config. Are you okay if we resolve this later?
This is the notion… this is explicit location overrides. Right now, I have it tested, I have the core doing explicit location overrides, so you can say this scheme URL is actually found here, and we can have, like, you know.
all that. It's tested. I didn't actually make the user-facing part of this anyway. Like, this doesn't change… There is no user-facing aspect of this whole new thing. It's just replacing the core so we can build out those features.
So, are you okay with that if we start using the config way in the future?
**Liudmila Molkova** 18:26 Yes, I am okay with it.
**Josh Suereth** 18:29 Cool.
I'm gonna leave that there. And then, This is the last good question. What happens if a dependency with registry path and overrides, are configured at the same time?
My thinking here is override path always wins.
**Liudmila Molkova** 18:49 Yes, so you over, like, right, you overwrite, which… Yes, okay, sounds good.
**Josh Suereth** 18:56 Yeah.
Okay.
Cool. So if those are okay, I need to clean up, Yeah, frickin' check external types. What did I expose this time?
**Liudmila Molkova** 19:08 And do we have public API check?
**Josh Suereth** 19:11 We do, yeah.
Oh, I should… Okay.
We need… we need this public. Okay, so I'm just gonna update the… I need to update the external type allow list. This is, like, what our crates are allowed to publish. This is just a Rust convention that Lauren set up when we first set up the project, but it is… when you expose things from a crate.
You can't expose your dependencies without purposely doing so.
And I think server is a important enough dependency that we're gonna expose it publicly.
I… Unless you have concerns, I'll just fix that. Okay, cool.
So then, next steps on this. My next step that I wanted to do was, fix the, like, start to fix the dependency diamond problem more, so that we can do resolution. If we have a diamond, and the dependency in the diamond is different, start to fix that problem.
I had a PR before that did this, that I have a failing test that I cannot fix.
If you remember.
**Liudmila Molkova** 20:26 No, I don't.
**Josh Suereth** 20:27 Yeah, okay. This was a while ago that I had that. This is what led to me doing this refactoring. But there's a failing test that I couldn't fix with the current design, so that's why we refactored the resolver. And then I'm gonna go take that test and try to make it pass. That's the next step.
**Liudmila Molkova** 20:49 Okay, and you also have the PR that's supposed to simplify some of the things for the imports?
**Josh Suereth** 20:57 I have a PR that simplifies inputs.
**Liudmila Molkova** 20:59 What drops the include and referenced?
I think it's good to go.
**Josh Suereth** 21:08 Which drops me.
**Liudmila Molkova** 21:09 Gene 42.
**Josh Suereth** 21:11 Oh, that one! Yeah, yeah, yeah, that's also one. I need to actually move that to master.
So… It's okay.
**Liudmila Molkova** 21:20 The one above.
**Josh Suereth** 21:24 Yeah.
Okay, so this one is good to go?
**Liudmila Molkova** 21:31 Yeah, I probably need some rabesis.
**Josh Suereth** 21:33 Yeah, let me, let me do that. So, we'll say next steps.
Next steps.
Fabase Bank.
And… dependencies… or schema… From Ash.
So this is actually for your rendering in, like, SimComp Gen AI?
inside the forge schema, I'm gonna actually add the full schemas of every schema URL, so you'll have a map that is, like, schema URL to fully resolve schema for the dependency list.
In a dependency section.
That way, if you need to, like, look up things as you render, you have access to all of it. I'm worried I might be throwing way too much JSON at you, but hey.
Unless we try it, we don't know.
**Liudmila Molkova** 22:22 Yeah, that's fine.
**Josh Suereth** 22:24 Okay.
So that's… that's one of the… oh, I'm not showing this. So that's one of the things I want to do. And then, candle.
Diamond. And let's see… Virgin Conflict Resolution. So that's the last thing. Once this is done.
I want to do, a release and, like, a validation with, GenAI to make sure this is all working, because I think In my mind, that's the bare minimum for us to stabilize V2.
Like, to actually mark it stable, make it default, that kind of stuff.
But, wanted to run that by everybody.
**Liudmila Molkova** 23:07 Well, we need some minor stuff for V2, the… Ability to tolerate unknown… The forward compatibility.
But that, that's…
**Josh Suereth** 23:23 Oh, right.
**Liudmila Molkova** 23:24 That's… that's… I have PRS, it's just they need some reviews and, maybe some updates, because it's been a while.
But yeah… I've… I'm removing hacks we have in SimConf, in GenAI.
Yeah. And… I think we… I think I removed the lust on yesterday.
Okay, great. I would be… yeah. So maybe one more thing I will add.
Okay, there is one more hack.
In the Markdown and the dogs generation.
I hard-code the… Bays… URL to prevent for docs, like the repo, yeah. What if we put it in the config as a part of overrides?
**Josh Suereth** 24:27 I mean, I'd be fine with that. That makes sense, too. Yeah. So doc generation, it would be another thing here.
**Liudmila Molkova** 24:35 Right.
**Josh Suereth** 24:35 doc generation.
You know, boy.
**Liudmila Molkova** 24:39 Where, if we added it in the definition manifest.
Well, should it be in Manifest? I don't know.
**Josh Suereth** 24:46 That I'm not sure of. Maybe it can be in manifest of, like, a published manifest. That gets into this discussion here. Sorry.
I… This is… so, so… That is part one, like, you doing dock generation is part one of what I want to do before we resolve fully and say V2 is stable. The second part, though, is actually code gen.
Especially given, like, what Tyler was saying yesterday, I think once we get some Gen AI code gen in some other languages.
We… you have it resolved for Python.
Do we need to look at Go specifically, or are you not worried, I guess, would be my question. Like, given that you have it working in Python, do we think we know enough about how CodeGen works in this, dependency world where we could make a generic CodeGen thing that can work and generate Semcov, and GenAI Semcov, and other federated repos successfully.
**Liudmila Molkova** 25:49 Mmm, yeah.
I… Think one language is sufficient, but we didn't prototype it.
Like, the dependency resolution part, like, generating two different artifacts at the same time. So, I don't now go well enough. I'd rather try it, let's say, in Java.
**Josh Suereth** 26:12 Okay, okay.
I know enough about the Go version and the Java version, I could do either. I would be happier, I think, doing it in Java, but I can also do it in Go. The main thing I have with Go is, Go format is a pain in the ass to make it not needed.
coming out of Jinja. Like, whitespacing is so important to go. Jinja is so bad at giving you exactly the white space you want.
So, it's, like, really infuriating to, like, make those two work together, yeah.
**Liudmila Molkova** 26:48 You know what, I've been doing Jinja with AI, of course, and I've been looking at Perklaude, trying to figure out ways spaces in Jinja and going in loops. It was so funny.
**Josh Suereth** 27:02 Okay, so I… let's say this, I think… I don't think we can do the cogent thing until this is done, this here, the… where we have dependencies and forward schema, because, if we need to reference things from a dependency.
Right?
What does that look like?
Are we going to… you know, this is what I was saying, where I think the current plan, and I still think this is the right way to go, is we basically vendor all the things we need in the code we generate.
But if they wanted to have.
some sort of dependency between the two so they're compatible? I don't know how to do… like, does a dependency in SEMCOM lead to a dependency in CodeGen as well, is the question.
**Liudmila Molkova** 27:49 Yeah, so… Trask had thought that, yes, for Java.
Right.
**Josh Suereth** 27:55 And go once this is well.
**Liudmila Molkova** 27:58 Umber, probably.
And for this, we would also need… Some overrides to say, to explain the package name.
**Josh Suereth** 28:11 Yep, I think this is where we have some sort of code gen config, right?
**Liudmila Molkova** 28:15 Yeah. Or, like, the civil rights thing is just a bag of properties of params that… repos can provide.
**Josh Suereth** 28:25 Yeah.
Alright, I'm gonna add that.
**Liudmila Molkova** 28:32 I don't even know if GenAI is a good test for it, because if you have one package.
You'd rather… Hand… Like, manually do the dependency, you won't update it, you wouldn't need to do much about it.
Right, and it's only if you do something very complicated, like the Uber package.
**Josh Suereth** 28:58 Yeah.
Okay.
Right, I don't even think we can start to tackle this until this is done.
So, we know it's a problem, we know we need to address it, but… just in terms of making progress, I'll get this added first, we'll keep focus on the dock-related stuff, and then we'll get Cogen next. Like, I'm not… I think we have ways to solve it. I'm not worried about solving it, I just think it'll take time.
**Liudmila Molkova** 29:32 be a…
**Josh Suereth** 29:33 Cool. I don't want to hold us up too long. Last question is about definition manifest versus published manifest.
So, in your PR to SEMCOM, let me just show this, because I made a comment.
Right?
Submit conventions… Let's see… I love that we're down to 20 pull requests. I don't know if that's, you know, a sign we're moving faster or less PRs, but it's still kind of fun.
**Liudmila Molkova** 30:03 We moved Gen AI out.
**Josh Suereth** 30:05 Oh, that's… that's for all the time.
**Liudmila Molkova** 30:07 There are more PRs and Gen AI than here.
**Josh Suereth** 30:10 Interesting, okay, got it.
Alright, so… This is where… I have a concern with just semantics. If we look at the manifest here, it has a specific version.
Right? What is this version? Is this the target version of the… tag?
Like, so, so, like, is this the version of the… Is this the version that will be released?
Is this the actively developed version? You know what I mean?
**Liudmila Molkova** 30:50 Oh, I see, yes, so this is currently the version of what was released, because it's also used everywhere in this repo.
But yeah.
**Josh Suereth** 31:03 So, like, this… what a… like, if we were doing this the way that we had our old thing, this would be slash next or something, or, you know, slash 1.43.0 dash dev, or dash alpha, or dash, you know, in progress or something.
**Liudmila Molkova** 31:21 Right.
**Josh Suereth** 31:25 And then when we…
**Liudmila Molkova** 31:25 No.
**Josh Suereth** 31:26 At least we tag with it being a normal version.
**Liudmila Molkova** 31:31 Would it pass the checks?
Or should we change the property name?
I mean…
**Josh Suereth** 31:40 There's… I think there's two things we could do here. One is, we could make it so a definition manifest doesn't have a schema URL.
But… And you're expected to get that externally?
**Liudmila Molkova** 31:58 Mmm…
**Josh Suereth** 32:00 Oh, I see what you're saying, yeah. If it doesn't have it, then we don't know what it's compatible and what it's not compatible with, yeah.
The problem with this here is we might think it's version 1.42 if we resolve it, but we are actually resolving the, like, in-development 143.
**Liudmila Molkova** 32:18 Alright.
**Josh Suereth** 32:18 Great bullet from Maine.
**Liudmila Molkova** 32:21 Right.
Okay, I will try to replace it with something like next. If we don't have the schema URL, Done.
**Josh Suereth** 32:34 everything fell.
**Liudmila Molkova** 32:35 And it's… everything fails, but it should be possible to provide it.
To the package.
What identifies manifest? Just the file name?
**Josh Suereth** 32:48 what identifies manifest is the file name, yeah. So we give, like, when we resolve things, we say, here's a location to start resolving, and it looks for manifest in that location.
Yeah, like, I think this is a deeper discussion about What I want to do is, what behavior do we want? Let's start from there, and then we'll work backwards into how we change Weaver.
So, like, in my mind, I think we could go with one of two things. One is, we could just not have it here in development, and when you call Weaver Publish, you provide a schema URL that we insert into the manifest of, like, here's the version you're releasing, right?
We could say, in development, instead of schema URL, we say schema name, and it is just this portion of it.
It doesn't have a version.
Because, by definition.
If it's, you know, the development repo, there is no version associated yet, you haven't released.
The weird part about that is, there kind of is aversion, Right?
And the ver- but the version's a development version, like, you're still working on the next one.
So.
**Liudmila Molkova** 34:01 I'm thinking, since we use this manifest, As a source, like, you can use it inside your dependency.
Right? Somebody can depend on you.
And… They need to know what they depend on.
Since we are allowed to depend on definition.
We should have schema URL here.
And it should be reasonably… Well formatted. It should be valid.
Europe and everything.
**Josh Suereth** 34:34 That's… that's why I'm kind of thinking we give it some sort of pre-release thing.
**Liudmila Molkova** 34:40 Right.
**Josh Suereth** 34:40 Or, we could even give it, you know, a dash dev plus, if we want, Or something, to denote that it's currently in development, you know?
**Liudmila Molkova** 34:52 And it's the next person.
**Josh Suereth** 34:53 And it's the next version, yeah.
**Liudmila Molkova** 34:56 Right.
**Josh Suereth** 34:57 So, so the version that you would submit wouldn't be… yeah, if we go back to this, instead of using 142, you'd say, like, 1.43.0-dev plus, you know, in dev or something, or dev… or just dash dev, yeah.
**Liudmila Molkova** 35:12 Unrealist.
**Josh Suereth** 35:14 Oh, yeah, Dash Unreleased, I like that, yeah.
Because again, it fits in Conv, and because you're using the pre-release dash, I think the version conflicts will all work correctly, it'll never take precedence over an actual released version, like, that gives us what we want.
Okay.
**Liudmila Molkova** 35:33 Okay.
Cool, I'll do this.
**Josh Suereth** 35:37 And when… just to confirm, too, when we call package in Weaver, I can specify the actual version number, and it'll, like, overwrite it, right? Or do we not do that yet? Is that a feature we should add?
**Liudmila Molkova** 35:51 Can we override it? I don't think we can.
But we can also safely ignore… well, okay, so maybe my comment was not right. So, when you use a dependency, when you use definition manifest as a dependency, you must also have a schema URL.
In your manifest.
And this comes to a pass.
And then, maybe it's not required Here.
And if we… Remove it.
**Josh Suereth** 36:31 I guess another way to think about this, not to derail what you're thinking is, in our release script.
Right? We would… when we bump the version numbers for everything, we would bump the version number of manifest to 1… from 143-in development to just 143.0.
we'd commit that and tag it as the version. So if you grab the GitHub, you know, tag, you're getting that. And then when we package, we just use the version from the manifest exactly, so that the Git tag and the packaged version have the same contents. That… that feels right to me, that's fine.
**Liudmila Molkova** 37:13 Okay, so then I would prefer to keep schema URL here. I have no good reasons for it.
**Josh Suereth** 37:20 No, no, that… it makes sense to me. I think, let's keep… so… so, to confirm, we're gonna keep Schema URL here, but we're gonna have it be the next version dash development.
In development.
**Liudmila Molkova** 37:30 Dash, dash, unreleased.
**Josh Suereth** 37:32 Oh, dash unreleased, sure. And then in our, in our release process, we remove the dash unreleased.
Make a commit, tag the commit with the release number, and then bump it to the next version dash unreleased as, like, a process we have to go through.
**Liudmila Molkova** 37:48 Yeah, like, after the release, we will need to have a workflow that bumps it to the next version.
**Josh Suereth** 37:54 Yep.
Okay, cool.
Awesome.
I think that's everything I had.
Were there any other topics?
You wanted to talk about?
**Liudmila Molkova** 38:06 No, I've been slightly distracted from Weaver lately.
All of us were… Yeah.
**Josh Suereth** 38:18 Yep.
No worries, no worries. Okay.
**Liudmila Molkova** 38:25 It sounds like… once we do everything around V2, and the… Depend… the diamond dependency problem is the last big rock.
And there is a little bit of minor stuff.
We'll probably declare the schema… the V2 schema stable, right?
And… we will… maybe even release Weaver 1.
Something?
**Josh Suereth** 38:49 I think we should think about a 1.0 at that point, yeah, yeah.
**Liudmila Molkova** 38:52 Yeah.
**Josh Suereth** 38:53 Yeah.
I almost wonder if V2 Stable and 1.0 should be the same thing.
**Liudmila Molkova** 39:01 Right, yeah.
**Josh Suereth** 39:02 Yeah.
I'll follow up with Jeremy on the future of… live check with this new resolver, because I think with this, he should be able to support federated SEMCOF, where LiveChat can actually grab multiple registries.
At the same time, and check all of them.
Okay.
**Liudmila Molkova** 39:27 Right. And then, it would… the… The dependencies should also be available, not just in the forge schema, but for the viewer life checks.
Yep. Yeah.
**Josh Suereth** 39:38 Exactly.
Yep.
Cool.
Alright, let's call it there. I think, I think that's… that's good for the day. If you have a chance to, I don't remember if the refactoring… oh, it has approval from you already. So, refactoring Weaver Resolver to use the cache. I will, fix up the dock error and external type crap, but if you're okay, I'm probably gonna merge that today, so I can start with the next stuff. Okay.
Awesome.
Alright, we'll see y'all.
**Liudmila Molkova** 40:15 Thank you.
**ariannavespri** 40:16 Bye. Bye.
