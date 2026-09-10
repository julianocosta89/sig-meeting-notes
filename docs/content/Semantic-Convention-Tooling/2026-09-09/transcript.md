SIG: Semantic Convention Tooling
Date: 2026-09-09
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Laurent Quérel** 01:09 I guess?
**Josh Suereth (Google LLC)** 01:12 Hey, sorry I'm late.
How we all doing? It's been a while.
**Laurent Quérel** 01:18 No.
It's been a while, yeah, sorry for that.
**Josh Suereth (Google LLC)** 01:24 No worries, no worries, I,
**Laurent Quérel** 01:26 Yeah, there is a combination of, I had a lot of work, and it's 7 AM.
**Josh Suereth (Google LLC)** 01:34 You know…
**Laurent Quérel** 01:35 Does not… which is the type.
**Josh Suereth (Google LLC)** 01:37 You could… you could move to the East Coast.
**Laurent Quérel** 01:41 Mmm.
Yeah, indeed.
**Josh Suereth (Google LLC)** 01:46 Yeah.
I can recommend some lovely, lovely land around here with gorgeous trees and… you know, then it's not so early when you want to join hotel meetings as well.
**Laurent Quérel** 02:01 Yeah, that looks a good, a good motivation.
**Josh Suereth (Google LLC)** 02:07 Alright, I'm pulling up the notes, I don't know if anyone else wants to run this. I have a topic I didn't add that, is… basically a bunch of shenanigans I was working on. Okay.
C8.
Oh, come on.
our document's too big, so JavaScript doesn't load for me until, like, 10 minutes later.
Come on, give me the dates.
Alright, actually, I have two topics.
We'll do the easy one.
I don't know if anyone else has anything else they want to add that's higher priority, but I want to continue the discussion around getting, you know, getting to the point where we mark V2 stable and all that, and I do want to call out, if we look at… Recent bugs coming in.
I think we're starting to turn a corner, which is exciting.
Is it the project board we want? Or… yeah, we'll try the project board.
There was a time when all the bugs we're getting in was about the data model being problematic and not having features.
Do you know what corner we've turned recently that I'm excited by?
**Liudmila Molkova** 03:54 You mean bugs and missing tiny little pieces of things?
**Josh Suereth (Google LLC)** 03:58 Yes, but actually, no, I think it's a sign… it, like, shows you what's landing over time, because it's, like, the second thing you want to use Weaver for.
Almost most of the bugs that I'm seeing right now, live check, live check, live check, live check, live check, live check, which isn't a sign that live check is the problem, it's a sign, live check's getting used hard, and I'm excited by that.
we're getting all the little tiny nitpicky things coming in now, and this is really good. So… Yeah, I think we turned a corner, and we're now on, like.
This is what I hoped, after your… the talks at, like, KubeCon and stuff about live check, I'd hoped that we'd be here sooner, but yeah, this is where I love being. It's, like, all of the polish is coming in at the same time. It's fun.
I don't know if there's anything you want to talk about there, Jeremy, but I was just… I noticed that, it's like, every bug is live-checked now.
**Jeremy Blythe** 04:52 Yeah, I… I wanna get on and squash them.
Right? But I just added… I just added for today, the big one.
For me, which is the… the mattress stuff, and it's… it's… it's the matches, but really what that's doing is it's making V2 Semconf actually work with LifeCheck at the moment. It's like, you can't really… it's not really usable.
**Josh Suereth (Google LLC)** 05:18 Gotcha.
**Jeremy Blythe** 05:18 Apart from in very, sort of, small, single registry cases, but none of the exciting, like.
Real-world multi-registry cases that we're now, like, using everywhere.
Right. So, I realize it's a giant PR.
But then, that's what PRs are like now, right?
**Laurent Quérel** 05:40 Indeed.
**Jeremy Blythe** 05:42 Well, that's hilarious.
**Josh Suereth (Google LLC)** 05:43 We're gonna do the thing where you send the PR, and then we have Gemini review it and send you feedback, then we have a human review it and send you feedback, right? Is that… is that our new lives?
**Jeremy Blythe** 05:53 Or now what you do is you have, see, PRs got so big that GitHub made, stacked PRs, right? So now we can have stacked PRs, which is the same big PR, but broken into mini PRs, so…
**Laurent Quérel** 06:05 Yes, which are also done by Gemini, or Cloud, or whatever.
**Jeremy Blythe** 06:09 Exactly, so something…
**Liudmila Molkova** 06:10 But then the stupid thing does the rebates, is wrong all the time.
**Jeremy Blythe** 06:16 I haven't used them yet.
**Josh Suereth (Google LLC)** 06:18 Yeah.
I don't… I kinda… yeah.
Well, let's just say, when you're working with agents, it's real easy to make a big mess.
And then, that doesn't mean it's easy to clean it up.
Okay, let's… let's get into the agenda quick. I want to talk about cargo dist. I think there were basically two… so this is, check GitHub attestations when installing.
Weaver, and then we have, basically, add validation to… Cargo dist as a… Explicit and fake step.
not a hackery workaround. I don't have a link to your PR, Ludmila, but thank you for fixing the build, by the way. It's kind of very disturbing that everything could pass and then be failing.
So I hate every time we find one of those, but we keep finding them. So cargo disc is nice.
Cargo Dist is now maintained. Cargo Dist is accepting PRs. Do we want to, like, is it worth us taking time to make changes to Cargo Dist? I feel like this certainly is.
like, I don't think this will… I don't know if this will get pushed back or not, but it feels like we could go to CargoDisk and ask for a feature that would say, like, we want to generate scripts that do… GitHub attestation checking. Of the downloaded artifacts, to make sure that they align to things.
The problem with that, I think, is how… like, GitHub attestation checking, I always use the GH command for.
which we can't guarantee is installed. There is, like, an API to download and stuff, so, you know, we'll have to figure out what the bare minimum is for our installation scripts. If you want context.
I can open up what our installation shows now.
How do folks feel, though, about, like, is it worth us going and… Oh, the second thing we want to do is… Right now, inside of CargoDisk, you can add additional Things to run that build packages that'll be included, but you can't create, like, a verification of the packages before everything's published.
You can make a post-publishing step, but you can't do a before-publishing run a test against packages step.
Because, you know, of course everything would work 100% and never be broken from cargo disc. You would never have to write tests, right? So I feel like that's a thing we need to add.
And I think it's probably worth actually making the changes in cargo discs, but I was curious what other folks feel, if we're okay still hacking around it on our side.
**Liudmila Molkova** 09:15 I don't have energy to go contribute there.
So… and things are not bad enough.
So I have to.
**Josh Suereth (Google LLC)** 09:29 Interesting. It does… so this, by the way, comes from CargoDisc, which is how to verify an artifact that you download manually.
So the GitHub attestation that you want to do.
what script are we actually talking about? Or are we talking about…
**Liudmila Molkova** 09:46 So I didn't really want to do a GitHub attestation, what I wanted is, immutable releases.
Yes. Because I realized we, the version was broken, and I realized I can actually go and push from my, even, home computer, the new version. And I shouldn't be allowed, none of us should.
**Josh Suereth (Google LLC)** 10:09 Yeah.
Okay, so that we can fix. This, I think, is actually the… code that resolves a version of Weaver, right?
So that resolves the latest version.
Restore Weaver from cache, or install Weaver. We have Linux and Windows. This is actually using the installer SH script that's in our download. And this is the one where you want to make sure GitHub attestation checking and immutability exist, right?
**Liudmila Molkova** 10:39 rejected.
**Josh Suereth (Google LLC)** 10:39 capability.
**Liudmila Molkova** 10:41 it can be inside the script. I… I guess that there is some configuration somewhere in the GitHub.
That prevents you from just publishing new artifacts, and it's not related to cargoist at all.
**Josh Suereth (Google LLC)** 10:56 Right, the reason we do the attestation is mostly just, it's hard to violate both of these things, to, like, hijack this URL and hijack the other one, but yeah.
If you're… if you're downloading them both remotely, it's not… I got what you're saying.
Okay.
So you're saying it's not bad enough to want to go fix cargo discs?
**Liudmila Molkova** 11:28 I mean… Well, so, the problem. We have the ZSmer pipelines, which are important in supply chain attack prevention, right, analysis, winter first, GitHub CAICD.
The PR that edited broke the thing.
Right? It will happen again, right? We will have more, like, shared workflows or something that will break it again.
So now we have, hopefully.
A smoke test that maybe will prevent something from happening.
But… no guarantees, right?
So Amy changed the pipeline.
this file should be verified, I don't know how, manually.
and… This is the problem.
So… We would need… we would either not merge this, or we will make the mistake again.
This is bad.
And this is something that would be cool to fix in CargoDust. There is an issue, nobody ever replied to it, nobody started working on this.
**Josh Suereth (Google LLC)** 12:42 Do you have a link to the issue? Do you know…
**Liudmila Molkova** 12:44 I'll find it.
**Josh Suereth (Google LLC)** 12:45 If you find it, put it there. I might…
**Liudmila Molkova** 12:47 Bye.
**Josh Suereth (Google LLC)** 12:48 I don't have a ton of time these days, but if I do find free tokens, that's something to just throw at it.
To see if we can make a fix that's not bad.
**Jeremy Blythe** 12:58 The other thing is, when I… when I was doing the scorecards stuff.
I had to put a bunch of patches into the release YAML.
that DIST creates, and then I made… A rather ugly thing.
That you could run, so if you did regenerate.
You could then go and reinstate all those little patches.
And it's really ugly and horrible, and you'd have to sort of do it a bit by hand each time, but at least it would mean that it was sort of documented, all the things you had to do.
Otherwise, we'd get the squad card failures back again.
**Josh Suereth (Google LLC)** 13:38 And, yeah, I need to look at what those were. That was basically around, version locking different Actions and components, right?
**Jeremy Blythe** 13:48 It's version-looking, and it was the, how privileged the… But,
**Josh Suereth (Google LLC)** 13:59 Oh, right.
**Jeremy Blythe** 14:00 Which is, like, read, write, and versus read.
So, just default to making everything read right at the top.
Of the whole, action flow thing, workflow.
**Josh Suereth (Google LLC)** 14:13 I feel like both of those are things we should be able to push upstream.
Right?
Like, that just seems like something Cargo Dish should support. Like, I… I… you know… We can't be the only CNCF that uses REST and cargo.
Or cargo discs. Okay, let's copy this here. Alright, I think that's as much energy as I wanted to spend on this topic, if that's okay.
But…
**Liudmila Molkova** 14:39 Maybe, Laurent, do you know if there is a problem in Hotel Rust? And in…
**Laurent Quérel** 14:46 Hotel Rust? I don't know. Hotel Arro… We are not using cargo discs.
**Liudmila Molkova** 14:56 Because you don't have installers, right? Yeah.
**Laurent Quérel** 14:58 No.
**Liudmila Molkova** 14:59 Sorry.
**Laurent Quérel** 14:59 No.
No, we… we… for now on, we can't.
Even if we won't.
No, we don't. No, we just published on Quiz.io. I think that's the only thing that we did recently in this space.
**Josh Suereth (Google LLC)** 15:20 Okay.
**Laurent Quérel** 15:22 But, yeah, otherwise, yes, I think we will work on that.
**Josh Suereth (Google LLC)** 15:36 Okay, cool. Let's move on. I think that… I do think we probably need to work on this. Lauren, if you're… if you're planning to use CargoDisc ever.
Maybe we should talk to Rust folks as well. I don't, I'm not sure who's the maintainer.
**Laurent Quérel** 15:55 I know a few of them. I think CGO is one of them. It could be something that's interesting, definitely.
So CJ, Lalit, but I don't think Lalit will, will… We'll work on that. He's, proceed on the Hotel Laurent right now.
Yeah. I can, you know, I can ask, I can do… at least I can do that.
So, I guess there is a… Oh, Oto Roswell.
**Josh Suereth (Google LLC)** 16:32 doesn't need to use dist, duh, because they're just crate, they're crate-only distribution.
**Laurent Quérel** 16:37 Okay, yeah, that makes sense, yeah.
**Josh Suereth (Google LLC)** 16:40 Yeah.
You're the only other binary in the OTEL ecosystem that would want dist.
**Laurent Quérel** 16:47 Yeah, if, if we can, yeah, in some way, name our thing, a collector, yes, for sure.
**Josh Suereth (Google LLC)** 17:01 We can name it a, preview executable. Alright, let's, let's move on.
**Laurent Quérel** 17:10 If they're somewhere, because I tried to follow, and I didn't entirely capture the… the entire problem there. Is there a description?
of the… of the problem, Liya or Josh, that, I can read again and… and see, if I can do, like, Josh, spend some, Some time and token to solve the problem.
**Liudmila Molkova** 17:39 Yeah, let me, find it. It should have… Some level of details… Okay, it's in the chat. There is a… it's a bug, and there is some…
**Laurent Quérel** 17:53 Okay.
**Liudmila Molkova** 17:54 Sorry, AI-generated analysis of the bug.
**Josh Suereth (Google LLC)** 18:01 I mean, AI's never wrong, so it's perfect analysis.
Yeah. Cool. I want to move on to V2 stabilization and manifest. This is the thing I've been trying to throw tokens at. So, with the split of V1, V2, I was continuing, I was splitting stability, I was splitting other things so we can actually have V2 completely separate from V1.
Ran into some fun things with manifests, okay?
So let's, let's talk a little bit about, Well, main differences. So, few things. We have registry underscore manifest.yaml, and then we have just manifest.yaml.
And then we have file format of manifests 2.0.0, Empty.
Question.
Which one of these… Is the old version of Manifest, and which one is the new version of Manifest?
Do you know?
**Liudmila Molkova** 19:01 So, either of two file names, and the empty file format.
**Josh Suereth (Google LLC)** 19:09 Yeah, well, I mean, like, just for file names, which one… do you know which one was the legacy and which one's the new one?
**Liudmila Molkova** 19:14 Oh, the legacy is register underscore, but…
**Josh Suereth (Google LLC)** 19:17 Yeah.
**Liudmila Molkova** 19:17 Yeah.
**Josh Suereth (Google LLC)** 19:19 And then, so what I was trying to do.
was actually make it so registrymanifestyaml always parses as V1.
And that has access to, like, name and version instead of schema URL, and we stop parsing name and version completely in V2.
Right? Because it's legacy. The other thing I was going… so that was, like… yeah, so basically, this… use access to name, version, deprecated fields. The other thing I was gonna do was I was trying to make a third here called, definition manifest, because we actually have a split now.
between… Oh, I can't spell definition, by the way. I'll spell it correctly when I make the PR.
Cause, you know, the agent will fix it for me, because my spelling's atrocious.
this was the next thing I was looking at, where I was gonna say, okay, if we have no file format.
That would be Legacy.
If we see this, that is the published manifest, and if we see this, this is the definition manifest that you use when you define a Semconf, and the definition gets turned into published. We already have this notion of published manifest and definition manifest in all the comments in code, and in how we parse it.
So it's not like a new concept, it's just it's not explicitly made.
Here's what I ran into.
**Liudmila Molkova** 20:44 We had Definition Manifest, and at some point, I remember removing it, and I remember having reasons for it.
because… I… but I don't remember which ones.
Generally, because it's kind of useless.
**Josh Suereth (Google LLC)** 21:01 Yeah, basically what we're doing right now is anything that is empty is treated as definition manifest, and we don't know what version, so we just guess based on the fields that are there.
**Liudmila Molkova** 21:12 Oh, because we wanted to support Like, we cannot be strict on the versioning.
No, because… We would probably support the wide range of definition manifests anyway.
Anyway, continue. I'll remember if it's as important.
**Josh Suereth (Google LLC)** 21:33 Yeah, well, that gets into the rub now. If you look at, like, OpenTelemetry Semconf that is using V2 for everything, it is empty on its manifest file format. It doesn't define a file format.
So if I were to make a change that said, definition manifest in V2 syntax must provide file format.
That would be a breaking change.
Potentially. Like, I think I can make it not breaking, where we just treat it as V1, And we allow, like, name and version in those, and then we have a warning that says, like, specified definition manifest here, because we found a definition manifest that isn't a definition manifest, and all that kind of stuff.
But it, like, the PR's getting somewhat large and awkward, and I'm trying to, like, make a decision.
**Liudmila Molkova** 22:26 We can make a breaking change in V2. There is one, maybe two, maybe already three repos that use it.
**Josh Suereth (Google LLC)** 22:35 Okay.
This gets in… well, this is why I wanted to have the discussion with Jeremy. Here's my… here's my straw mint, okay?
So, file name of registry manifest, okay? yaml.
always parses as V1.
Just, it's hard-coded to do that.
Every time.
Okay? And then if you're using that, we give you a warning that says this is a deprecated name. You should move to Manifest V2 with this new name.
Okay?
So, now we have… the file name is manifest.yaml, and now we have some… a decision tree. So what I was going to do was manifest.
2.0.0.
Always published manifests.
And I'm actually creating a type called published manifest, which we would use to know if something is published or in definition. And we might be more rigid around that in the Resolver engine in the future. For now, they all easily cross-convert, but actually there'd be a type that says this is a published manifest, not a definition manifest.
Published manifest has more restrictions. We can actually be tighter. We can say, this is an invalid published manifest, it doesn't have version, it doesn't have whatever we need for publishing, right? So we have more capabilities there.
Here's… here's the rub now.
Empty, right?
is assumed to always be definition manifest. Oh, let me add this. We would add definition manifest, 2.0.
Which is always… V2 definition.
manifest.
And empty is always definition V1 manifest.
Always, always, always.
And what… what we can do here, then, is… If you have the file name wrong, we recommend moving to V2 with the new file name.
if you have the file name right, but you don't define a schema, we'd say, hey, you don't define a schema, you're in V1 of the manifest, we'd allow name inversion, so we wouldn't break people willy-nilly, but we treat you as a V1 manifest, even if you're in the other file name.
My initial plan was to be super rigid and make all the file names require the file format for Manifestyaml, but that would immediately break, like, our nightly would break.
for, for SemComf Gen AI. So this is my current straw man, and I want to run it by you before I send you a ginormous PR with all the bullshit to make it work, because it's… it's a lot of weird… shenanigans.
Initially.
**Liudmila Molkova** 25:33 And you, you want explicit… So I… I'm kind of focused on VTU.
And whatever happens, like, we want just… we just don't break it, that's all I care about. For V2, is… we would always have it explicitly, and the reason is because it's symmetrical, and it's just good to have it specified.
This is their.
**Josh Suereth (Google LLC)** 26:01 I think this gives us more capabilities around evolution, yeah. Like, the reason we started adding the file format at the top was to have more capabilities, but then, you know, at some point in time, we change our resolution to basically pull in key-value pairs.
Or look at the file format, and then take those key-value pairs and Confirm them against a particular schema version.
and then load that schema version, and you get the, we can get more rigid reject or accept blocks, right? So I can actually reject things that have name and version completely in V2. Say this is not allowed.
So we drop name inversion completely from manifest, because it's only in the V1 manifest, and this doesn't break anyone, because right now, all the existing definition manifests are empty.
Whereas in here, it'll always be a full schema URL.
**Liudmila Molkova** 26:55 It kind of makes sense if we want to support the V1 schema.
For a while.
**Josh Suereth (Google LLC)** 27:02 Yeah.
**Liudmila Molkova** 27:05 and… Dan, yes.
if we want to say, okay, in a year from now, V1 will be removed, and only exist in old versions of Weaver.
then we would be able to do all that you want, and… by assuming it's V2. So if somebody uses manifestV2, We assume it's V2.
And then… Empty or not.
**Josh Suereth (Google LLC)** 27:43 That's… yeah, this is really the… this is really the bread, like, this is the hard decision here.
Like, if you want that to assume V2, that's going to break existing manifests, that are not on V2 yet, that aren't using schema URL, right? Like, Jeremy, does your company use schema URL, or are you still use a name inversion in your Weaver registry manifest YAMLs?
**Jeremy Blythe** 28:08 I'm still using the… 1… So,
**Josh Suereth (Google LLC)** 28:15 Earth.
Are you using the old file name at the same time, or have you moved to the new file name?
**Jeremy Blythe** 28:21 I moved to the new file name.
But let me just look in another place, because I can't remember exactly.
So, my manifest… Where is it? Here.
I have… So my manifest has, No file format, so it's your third case there, but empty.
**Josh Suereth (Google LLC)** 28:52 That's what I thought.
**Jeremy Blythe** 28:53 I'm using V1.
So I have name, schema URL.
dependencies.
And in the dependencies, I just have a list that only has schema URL and registry path, and that's it. I removed anything I didn't need.
**Josh Suereth (Google LLC)** 29:12 So, the… having just dependencies and registry path is actually fine for V2. You have schema URL, which is fine for V2. What would happen is, if we assume this is V1, you'd actually get an error that says you can't have a name there.
Because in V2, we got rid of names. Names are part of schema URL.
**Jeremy Blythe** 29:32 Which is fine.
I think that's fine. I think we need… when… when… when we do a migration to V2, which we'll do when I get my life check PR in.
Then… there's an expectation that you're gonna have to do some work, right? So…
**Josh Suereth (Google LLC)** 29:50 Well, this would make you do it immediately, because again, like, if this PR goes through, it means if you're using the manifest YAML, you would have to make that change now to your manifest.
**Jeremy Blythe** 30:03 Yeah, and I think that's… Mine.
Okay. Why wouldn't we, if we're being more explicit.
Why wouldn't we name the published manifest?
Publish manifest.
**Josh Suereth (Google LLC)** 30:17 Good question. It's currently called Manifest 2.0. We could change it to Published Manifest. We did have this decision a while ago, and I remembered we didn't want published in definition, because we thought it'd be too confusing for people.
**Liudmila Molkova** 30:33 Yeah, that's… that's why… that's where we removed definition. So, I… I… I prefer… to keep manifest slash V2, because this is THE manifest.
The real one. The one in definition is just the future schema URL and a list of dependencies.
**Josh Suereth (Google LLC)** 30:54 Yes, it's… which is why it's actually something different.
slightly different, but we still call it a manifest in code. Or no, we don't. We call it a definition manifest. We put everything… we have this giant… Yeah, Ludmila, you worked on this with me, too. There's this… we did this giant, weird mapping thing, where, like, we just take a look at what you have and sort of guess, and I'm trying to make it more explicit, and, like, something we could write down.
**Liudmila Molkova** 31:22 So, maybe you will do this. I, like, if Jeremy Laurent is okay, I think it's a good direction, I just want to remember why we removed it, because I remember doing it.
Yeah. And making the decision. I'll dig it up, I cannot just find the PR for some reason, but I'll dig it up, I'll figure out the reasons, and where we get it from there, but it kind of makes sense.
**Josh Suereth (Google LLC)** 31:47 Yeah, I can see us going forward with two possibilities here. Like, one is we make definition manifest explicit as a file format thing, so we're consistent in every file that we look at.
And that definition is different than publish, and we can actually have different schemas, we can support different things, we can have things in definition that get erased by the time you publish, right? Or we can have things that are in the publish that aren't in the definition because of convenience.
That… I'm 100% on board with that, I think that makes sense in the code.
So, option one is we give it an explicit name. Option two is, the absence of file format means you're a definition manifest, which is kind of how things are today.
In terms of how we infer it.
I'm not really super comfortable with that, because we're… we now have the V1, V2 hell just everywhere. Which is the way things are today that I'm trying to cut, right? So, I would like to make a formal divide, but Ludmila, if you can look up the rationale, we can take this offline and chat.
**Liudmila Molkova** 32:49 Yeah.
**Josh Suereth (Google LLC)** 32:51 Okay, but do those two possibilities Outside of, like, nagging concerns, is anyone against them outright as being bad?
If we pick one or the other in chat.
Okay, cool. So let's resolve that in chat. I don't think we have anything more we have to talk about urgently in this meeting around that. Let's move on.
Matchers and Live Check V2.
**Jeremy Blythe** 33:15 Let me share my… screen, if I can.
**Josh Suereth (Google LLC)** 33:19 Yep.
**Jeremy Blythe** 33:21 Hmm… Sorry, I'm on a different computer today.
Is that working?
Okay.
**Josh Suereth (Google LLC)** 33:44 tickets.
**Jeremy Blythe** 33:48 I'll try to be brief. I think we've spoken about this a few times. There's a bit of… on the, on the PR, there's a bit of commentary, and then what I did first was I made this file, which is checked in, which is called LiveCheckv2 SemComp. You can go… And take a look at that.
That has now been implemented by Claude and I.
And I've made another document, which is… which is sort of supposed to be the user… I guess the user manual for mattress that walks you through… An example.
And how you would then, use the matching concept to do things that you could never do before, like… Actually properly check spans.
And, and, and… a whole myriad of things. So… This document walks you through it.
essentially what… essentially what it, boils down to is I'm using Cell, To create these expressions.
that, you use to match your incoming sample.
with the signal And, optionally, attribute groups.
That you… that are, Associated… that can be associated with that sample as it comes in.
So, in the Weaver tunnel, you build these matches out.
You give each matcher an identifier so that you can see that in the output, so then you can see, oh, it was this matcher that meant that this thing happened, so then I can trace back to it, which is kind of nice.
You put the… you put the when, the cell expression, inside the when here.
And… I've… put loads of different ways of, being able to find things in that VIN, probably more than… more than people will ever use, but anyway.
And so if that… if that, evaluates to true, then I'm saying this is the signal that's in my registry that I want you to then, do the comparison with.
And it walks you through all the thing. You can also do attribute groups, so you can have the when expression again.
that's the signal, but I also want to look at the other sort of extra attributes that appear inside the sample.
And compare them against, this list of attribute groups.
So this is… Maybe, and Liudmila and I talked about this.
quite a bit, and I think a lot of this attribute group-y stuff comes from maybe what I call the messy real world, where we go, like, I just want to have a big list of attributes, and I want all of my log records to use these attributes, right? Or… I've got these spans, they're not very well defined, but I know that my attributes are quite nicely defined, so I want to just go, like, hey, use this big group of attributes as well.
Which is the kind of stuff that we do.
So this is, like, support for that, but also things like, oh, I could have an exception. Like, there's attributes groups, like, like the exception, group, right, that you'd want to put in there.
What else? Yeah. If you don't have a when expression, so like I was just saying for logs, you could just say, like, I want all logs.
To compare against this group, or these groups.
So, and log is different from event.
As we know.
What else? You can use it to override?
So even… you… You can have, so things like a metric and an event.
have what I call a natural match.
It uses their name, and it matches, and that works really nicely. But… maybe you want to go, well, I'm matching with that metric, but I want to augment it with an attribute… list of attribute groups. Or I could even go.
No, not that signal, this signal, for some reason.
So you can do that.
you can… Things that you could never match.
Before, sort of, In a narrow group of attributes, you can now do, because you can say.
I can have a when expression that's looking at my resource block.
And go like, well, when I found, you know, this particular service name.
Use these attributes to check against my resources, or for my instrumentation scope.
Anyway, there's a load of… it's like… Every which way you can think, hopefully.
I've got this covered.
I'll show you some actual output that you get from So this is the output of running one of the main tests that I've built into the PR that goes through and hopefully pretty exhaustively exercises Lots of different ways.
To do this tricking.
The output now… in the standard, you know, ANSI output template includes this These blocks at the top, which is the… it's a new it's a new object in the output JSON that is called the match info. So this gives you a clue… this gives you the information about, like.
What led to this being matched?
So it uses that signal… it uses that matcher ID, And then it says, because of this match ID, I chose this signal, or because of this match ID, I chose these attribute groups, and that was what was then tested against this resource, or scope, or span.
then you get fun stuff, like, well, I could have two matches that are conflicting with each other, because I have one that says use match with this signal, and then I have another one that says match with this other signal, so that… The first one wins, but it points out in the info that there was another one that was conflicting that it ignores.
Mmm… What else is worth showing in here? Oh, because you can now, say, match to the spam.
this PR also includes all of the things that you would want for span matching, so we didn't have that before because we couldn't do it. But now that you can, it's checking that the kind is correct.
It's able to say.
like we have for metrics, it's able to say the things that are required are there. The things that are recommended are, like, an improvement. The things that are conditionally required become, like, you know, so you get new findings for spans.
That you wouldn't have before.
What else should I point out? Oh, yeah, There's a new finding called an unexpected attribute.
So now I've got a span, I've matched it.
I have my, block of… Attributes that should be on that span.
And I've optionally said, here's a bunch of attribute groups that I want you to check against. Now, if it finds anything else.
It will go… There was another thing that wasn't the signal, that wasn't the things you optionally said, so those are unexpected. So you'll get a, why did I get this?
Acme Strayfield.
Right? So that's a new finding.
What else should I say? And so this one down here, you'll see it said there's an unexpected attribute group.
Which is the Acme tenant of the deal.
But, because I have a… because I have the, command line config option, which is to search all attributes.
switched on. It still comes in as unexpected because it wasn't part of the explicit set that I said to compare against.
However, it's telling me that Hey, but I looked through everything that's defined in your dependency tree all the way through it, and I found a thing called Acme Tenant ID.
And it's in this… it's in the registry with this schema URL.
So I can tell you that… That attribute is actually correct, but it was still unexpected.
Which I think is… that's helpful for people to go, like, oh, you know what, I am using that, I should probably update the registry to more explicitly include tenant ID in this, whatever it is.
And then at the end, you get statistics… You get this new block, which is about the matcha coverage, so it tells you, like, using the matcher ID, like, how many samples each one hit, and if they had any error in the expressions, because when they're evaluated, they might cause an error. It will tell you all the errors that happened in that run.
So yeah, so that's… That's what this crazy thing is all about.
That test… Was driven by these matches.
if people have a match… if people have matches like this, sometimes… I mean, never say never, but if you were to actually make a file with this many matches in, you'd have a pretty crazy setup, but… Anyway… And the cell language is really… It's really nice, and you can do all sorts of nice things in it, like, you can… you can use this got exists, it's got, like.
This, you can use regular expressions.
**Josh Suereth (Google LLC)** 44:09 Plus, now we have another language that Ludmila gets to learn, which makes her happy, right?
No, Cell is a lot simpler than Regal. I actually had, you can still find it. I had a proposal for the hotel collector to use Cell instead of OTTL.
**Jeremy Blythe** 44:26 Hmm.
**Liudmila Molkova** 44:29 I've been thinking about yet another language, but in 2026, it doesn't matter anymore.
**Josh Suereth (Google LLC)** 44:38 Well, that, yeah, that's like, it's interesting because we're using Rego for policy violations.
And we're using cell for matchers.
And, I still think that's the right choice, because I think Rico is a bit bloated for matching.
And I think Cell is somewhat minimal, and you can do a crap ton with the syntax trees if you need to, to optimize the heck out of it. It's just… that… literally, that was the only… everything in here is amazing, Jeremy. Like, I really like this. I think this is a great design. I think this… this is what I would say should be 1.0 for live check, right?
the… my only concern is that meta concern, which is soft. It is, like, a 5% concern, not a 100% concern, is we're introducing yet another language. But when you look at this, I don't… I don't know if people even, like, know there's another language, you know?
Like, we'll tell them it's sell, we'll tell them how to look stuff up, but you, like, they'll just read it, and, like, maybe an agent does it for them, and it's well documented. So I'm not, like, that concerned, but it's something I just wanted to raise in case someone does have major concerns about it, because my inkling is, it's okay.
But it's something we should watch.
**Jeremy Blythe** 45:53 Yeah, yeah, I get that.
**Liudmila Molkova** 45:59 I think matures are… Awesome.
And… They are pretty much the same… Extensibility point as annotations and some conf.
It's the features that we don't have structured, or the information we missed in the schema, or we'll never get, some edge cases, and they addressed them.
So, like, ideally, we want to grow semantic convention schema to the point where most of them are not necessary.
But, it will take us a long time, and there will always be edge cases, and even those edge cases, people need to Tell the AI to write another language.
Why not?
**Josh Suereth (Google LLC)** 46:42 A well… a well-documented, well-defined language.
**Liudmila Molkova** 46:45 Yes.
**Josh Suereth (Google LLC)** 46:47 That… that it probably already uses, because, for example, everywhere I've seen that Rego is used, guess what the other language used in the same place is?
Cell, right? Like, the OPA agent supports either Cell or Rego.
So, maybe it's inevitable that we have both, honestly. The thing I want to call out, Jeremy, too, you're, you make attribute groups useful here, and that makes me happy. Because when we first added them, I'm like, this is going to be insane, how's this gonna work? But this solves my main concern with them, of like.
cool, the notion you'd have a customer as an attribute group, and then have a matcher that says, I need this in every event of this type, or every span.
Yeah, I… I really want to see this land. I need to do the… the whole code review, and apologies, it's been… it's… it's just that it's large, it's not that it's, I have any problem with it, yeah?
**Jeremy Blythe** 47:38 Yeah, cool. Well, I'm also gonna set… since… since I wrote that, Fable 5.1 came out, so now I'm gonna have Fable go under the review.
And maybe it will come up with some other stuff.
**Josh Suereth (Google LLC)** 47:57 Okay.
**Liudmila Molkova** 47:58 We can't tell you what Germany thinks about Fable…
**Josh Suereth (Google LLC)** 48:06 Well, what's the new… is it Astros, the GPT one? We can just have them all fight. Why don't we just make a ring of agents?
That just yells at each other, right?
**Liudmila Molkova** 48:16 I have a subscription now, I'll ask it to review.
**Josh Suereth (Google LLC)** 48:21 Because what's… what we want to avoid, by the way, with that is, it's the thing in, like, creative writing where you workshop a piece too much, and then it just destroys it, because they… if you ask the agent to find feedback, it will find feedback.
No matter what.
Right.
Because it's trying to do what you ask it to do. And so, I think you could literally have an infinite loop of doom.
**Jeremy Blythe** 48:46 I've seen that too.
**Josh Suereth (Google LLC)** 48:47 Yeah.
Anyway, particularly if you're using Claude, and it's any of the five models, God, what did they do to their verbosity, Jeremy, and why does your command not work for me?
You know your thing that tries to make it less verbose? That has not worked for me at all, for Claude. At all.
**Jeremy Blythe** 49:11 it doesn't work for me either, I have to get to the… I get to, like, the end of it doing stuff for me, and then I say, hey, now go back and change all of those comments following the rules I gave you, and then it doesn't…
**Liudmila Molkova** 49:23 First, it spends my tokens on this… writing this useless thing, and then it spends my tokens and time on rewriting them a couple of times.
**Jeremy Blythe** 49:35 Yep.
I know. Yeah.
**Josh Suereth (Google LLC)** 49:40 I've been… okay, so what I do with Claude, by the way, now, and I don't know if this is reasonable for you, but you have it make the prompt for another agent.
And then I have all the skills and things set up, so the other agent pulls in the prompt. And… only for, like, large, well-thought-out tasks, where it can be very explicit, so that the dumber agent, like, gets something done and gets through the issues and calls back to Claude to figure out the problems.
That works really well for me, because the other agent will actually not be verbose when it writes comments and crap.
Right.
And whatever the hell… I don't know where they invented their vernacular for, like.
the way they say things, of, like, two things, and one was load-bearing. I'm like, God, like, please. It's, it's like… It's like I'm talking to someone who's full of themselves, you know? It's just…
**Jeremy Blythe** 50:38 Yeah, yeah, I was having this, discussion with someone at work, and they're into linguistics, and there's this… there's this whole, There's this thing in linguistics called, center embeddings.
It's where you go, you say, you start on a topic, And then… in writing, you would then go comma, and then put, like, a centerpiece in that maybe is changing the topic, and then you'd comma, and you'd come back out of it, or even worse, what Claude does is it does end dash, and then a centerpiece, and then N dash, and then the thing.
And so, what happens is it goes down… it goes down this, spiral of center embeddings, where it will go… I'm… this is the thing I want to tell you about, but by the way, there's this other thing, and then inside that other thing, there's another thing.
And as a human reading that, you've got no hope. As a computer reading it, that's, like, amazing. That's, like, so… no problem whatsoever. So it's great at talking to itself, but humans can't understand it anymore, because… This overuse of center embeddings.
**Josh Suereth (Google LLC)** 51:41 That's awesome.
I'll have to… it's called a center embedding, huh?
**Jeremy Blythe** 51:45 Enter embeddings, yeah, it's a linguist. There's a few other terms in… but that's the one that's… most memorable.
**Josh Suereth (Google LLC)** 51:52 Well, in other news, the last conversation I had with Gemini about Weaver was, hey, why didn't you follow the instructions again? It's like, look, all LLMs have this problem. I'm not the only one. And I was like, but why are you the only one I have this problem with?
Ugh. Anyway, that's, like, where it's like, hey, go run this verification, it just doesn't.
Alright, cool.
Do we have any other topics? We do have Laurent with Crates.io publishing. Laurent, the breakage I'm doing around, making V1 and V2, Weaver SemConf. I think when that's done, we can start thinking about crate.o. I'm just nervous, because we're literally breaking all of our public APIs all the time and not taking them seriously the way you would for a crate.
So there's, like, two things I think we could do to possibly solve that. One is not have so many crates.
We could blend some of our crates together.
So that we have less exposed publicly, right?
The second would be… because honestly, like, the one Weaver API that we'd want to give you is in the Weaver binary, not… it's not even in a crate. It's in the lib for Weaver.
It's the thing that and understands how to do registry and V1 to V2 conversion and all that.
like, we don't have a public API. So I think what I would ask for you is, if you say, like, what crates you depend on, I don't care about that. What I want is what functions you're calling.
what API you need, and let's make that be a public thing, and then figure out how to publish crates where that's public, and we're only exposing what we need to for downstream consumption, right? I'm just… I'm nervous about the… the… I'm nervous about the overhead and the level of detail we have to have that we're not ready to have yet.
Or I want to go through and make sure that we're happy with what we're exposing.
So that we don't have to do version breaks in our crates all the time. Like, I want version 1.0 of Weaver to be the 1.0 of the binary, and I want version 1.1 to be 1.1 of the binary, but if we make crate-based breaking changes to our public APIs that people depend on, we're gonna have to go 2.0. We're gonna have to go, you know.
Like, it forces a versioning thing that we're not quite ready for.
is my main concern. So, I want to resolve that first, or if you give us, like, hey, here's the API I want public, we can figure out how to make that happen, and maybe we blend a few crates together to do that.
Where we can still have rocks and crates, we just don't have them as separate crates.
**Laurent Quérel** 54:35 Yeah, yeah, okay.
Because your intent is to publish the crates in version 1, or… because if it's in version 0.something.
What that meant to…
**Josh Suereth (Google LLC)** 54:48 It's more about controlling what our public APIs are. The crate version and the binary version are the same at this point. Like, we don't have the ability to do… So that's what you're gonna find. Oh, okay. Yeah.
**Laurent Quérel** 55:01 Okay, okay, okay.
**Josh Suereth (Google LLC)** 55:02 We do have modifications, yeah.
**Laurent Quérel** 55:04 I can definitely give you the API surface of what we are using. We are still using V1.
That's easy. I just opened, the dependency that we have, it's not precise enough. I know the data type.
But I can go, yeah, I can definitely give you the… the API surface, the exact API surface.
**Josh Suereth (Google LLC)** 55:32 Okay. Because I wasn't… we had talked about this before, how sometimes the different crates are, like, awkward to work around. So, if we were to give you, like, here's the crate that you depend on that has public APIs, and all the other crates are kind of hidden behind it, not re-exposed…
**Laurent Quérel** 55:48 Yeah.
**Josh Suereth (Google LLC)** 55:49 I'm a law firm.
What was that? Yeah.
**Laurent Quérel** 55:51 Yeah, I can do that.
**Josh Suereth (Google LLC)** 55:56 Okay.
**Laurent Quérel** 55:59 Are we getting the…
**Josh Suereth (Google LLC)** 56:00 Oh, go ahead.
**Laurent Quérel** 56:02 Regarding the annotations, I think it's too late now, but, next time, maybe, we… I have the intent to use a notation for the traffic generator.
And, I'd like to follow some prevention. I don't know where we are in this space.
If we already have some prefix that we use and reserve for, but we've earned… If there is a way to declare them,
**Liudmila Molkova** 56:30 There is a list of known annotations, so I'll find a job posting.
**Laurent Quérel** 56:34 Okay. Okay.
**Josh Suereth (Google LLC)** 56:36 Yeah, Weaver Packages uses them right now, so you can take a look at what those are. But we have, like, code generation annotations, and we have… policy annotations.
**Laurent Quérel** 56:46 Okay.
**Josh Suereth (Google LLC)** 56:47 So… Yeah, but you're right, like, it'd be good to have those defined somewhere, have, like, ability to namespace, or conventions around namespacing.
**Laurent Quérel** 56:55 Exactly, yeah.
Okay.
**Liudmila Molkova** 57:00 I have a tiny announcement, So, we are at the bottom of the list in, things, we need to migrate in semantic conventions to SKU V2.
well, I mean, there is a PR for everything at this point, but the part that I discovered, that a bunch of entities don't, in V1, Don Tough.
identity attributes.
So, this will be… I will send probably a bunch of PRs to Semantic Conventions to add some minimal identity to all the existing entities, otherwise we won't be able to convert those to V2.
**Laurent Quérel** 57:43 Okay.
**Liudmila Molkova** 57:45 And then it will be the time for… The publication, finally.
**Josh Suereth (Google LLC)** 57:56 Okay.
**Laurent Quérel** 57:56 Okay, yeah, have a good day.
**Josh Suereth (Google LLC)** 58:00 Yeah, that's awesome.
**Laurent Quérel** 58:01 I have to go. Yeah, thank you.
**Liudmila Molkova** 58:03 Thank you.
**Jeremy Blythe** 58:04 Cheers.
