SIG: Semantic Convention Tooling
Date: 2026-05-13
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/UkZDQaP_Y35eN0zq2fkMK2gcaotRbUb0xYrUcDWrZ9w_MtO_WKfwfpz2KhJTc937._0NZ3ke4P8Ns0LWm
============================================================

## Zoom Recording Transcript

**Josh Suereth** 04:21 Ayy.
**Jeremy Blythe** 04:25 Nope, hello.
Hey, how's it going? You recovered?
**Josh Suereth** 04:32 Am I recovered? Mostly, mostly.
**Jeremy Blythe** 04:36 Okay, good.
**Josh Suereth** 04:37 I'm under a swamp of stuff, though.
Because, you know, Being out for a bit.
**Jeremy Blythe** 04:43 Yeah, yeah, sure.
**Josh Suereth** 04:49 I haven't opened the notes yet, let me pull those up.
**Ludmila Molkova** 04:58 Hello.
**Josh Suereth** 05:00 Hey!
Is that the Northern Lights behind you?
**Ludmila Molkova** 05:07 Yeah.
But… Actually… I'm in the California desert, as far as possible from the northern lights.
**Jeremy Blythe** 05:17 You won't get them there.
**Josh Suereth** 05:22 Ludmila, this, this, conflict resolution is on, dependencies, right?
Like, it was a discussion we briefly had in chat? Okay.
**Ludmila Molkova** 05:33 Yeah,
**Josh Suereth** 05:35 Yeah.
let me… And… the PR I have, Yeah, this is gonna be fun, is all I'm saying.
Okay.
Okay.
Should we get started? Do we need to do any triage?
I haven't… I haven't had a chance to look at, like, our project board or issues, but there were a bunch that you were reporting, Ludmilla. I was thinking it might be useful for us to kind of go through those and kind of figure out if any are urgent.
**Ludmila Molkova** 06:44 Yeah, sure, let's do it. So…
**Josh Suereth** 06:47 Okay.
**Ludmila Molkova** 06:48 You're presenting, so let's…
**Josh Suereth** 06:50 Yeah, I was just gonna go through the, like, normally what I do is, if you see, like, model or CICD enhancement, that usually means I triaged, so I was gonna go through the ones that don't have that.
Although someone else might have added the annotation. So, let's start with this. Grouped events filter does not work.
Is this with V2?
**Ludmila Molkova** 07:24 It'd be cool to include an error, at least?
**Josh Suereth** 07:28 Yeah.
You can add this.
Is this using dash dash v2, or is this something different? What do you think?
**Ludmila Molkova** 07:45 It's not used in VQ because there is no… V2 flag… I… I have a small suspicion that we don't even have this helper.
I think we only have the helper for metrics and.
**Josh Suereth** 08:01 For grouped metrics in.
**Ludmila Molkova** 08:03 Yeah.
**Josh Suereth** 08:05 I don't know whether to mark this as a bug or a feature…
**Ludmila Molkova** 08:11 I'm… I'm checking.
**Josh Suereth** 08:14 Okay.
**Ludmila Molkova** 08:15 Yeah, we don't have the method.
**Josh Suereth** 08:23 We don't have it. So I'm gonna mark this as a feature request.
Okay.
The thing that's interesting here is, when we move to V2, are we gonna… are we gonna have this or not? Like, what… how do… are you using the group stuff in CodeGen?
**Ludmila Molkova** 08:42 R.
Yes.
**Josh Suereth** 08:47 And grouped is grouped by namespace?
**Ludmila Molkova** 08:50 grouped by namespace. Yes, because it makes sense, right? You would want to… if we render event registry.
We would put it We would do this, and then… run their all events for the root namespace in one file. Or, if you generate code, that would also be something you could do.
**Josh Suereth** 09:12 Alright, I'm gonna put this in to consider for next release, then.
Correct.
**Ludmila Molkova** 09:20 That's a perfect pilot, I'm sorry.
**Josh Suereth** 09:23 What?
**Ludmila Molkova** 09:24 This is a perfect desk for Copilot, I'm sorry for the flood.
**Josh Suereth** 09:28 No, no, it's… it's fine, yeah. Okay.
Let's do, track parent UI packages for updates.
**Jeremy Blythe** 09:36 Yeah, that's just my thing to keep a note of, the override we put in.
**Josh Suereth** 09:42 Alright.
So this is a task.
**Jeremy Blythe** 09:46 Yeah.
**Josh Suereth** 09:49 Entity associations in the UI.
**Jeremy Blythe** 09:52 That should be a feature.
**Josh Suereth** 09:54 Yep.
Okay.
Panic when policy users commit SHA reference. This one looked like this is an urgent bug.
**Ludmila Molkova** 10:07 It's workaroundable?
But… it is a bug, yeah.
**Josh Suereth** 10:14 Okay.
**Ludmila Molkova** 10:15 there is a PR from Copilot, but that one, I don't think it did a great job, or…
**Josh Suereth** 10:24 No, I don't think it was right at all. I remember looking at that one. That's why I asked if you mind if I tickle it.
**Ludmila Molkova** 10:30 I don't mind if you take a look, but yeah, I will take a look if you want at some point.
**Josh Suereth** 10:36 Yeah, I'm gonna add this to consider for next release.
Yeah, okay.
Cool, what else do we have? Allow span refinement to override name definition. This one, Copilot, never… like, it added the optional name somewhere, but I didn't see where it was actually doing the override at all.
And I was very confused as to how the tests were passing.
**Ludmila Molkova** 10:58 It was… I think it was something else, but for this one, I… I think it's a feature, it's not even necessary right now.
But eventually it will be.
**Josh Suereth** 11:18 Let's see, this is Resolution Engine… This is a feature… okay.
I'm gonna add it to V2 schema.
**Ludmila Molkova** 11:27 Yeah.
**Josh Suereth** 11:29 Okay.
Cool real quick, Linux release artifacts have unknown in the name.
**Jeremy Blythe** 11:37 This needs to be closed, honey.
**Josh Suereth** 11:41 Yeah.
Yeah, this is just… this is just how Rust names things, right?
**Jeremy Blythe** 11:50 Right? I just thought it was… I thought maybe it was a joke.
**Josh Suereth** 12:02 Okay, this… for any version of Linux.
Not specifically.
For example.
Yeah.
Right.
What else do we have? No, it's not true, I think it's just unfamiliarity with the Rust ecosystem.
Like, they didn't know that that wasn't a choice we made. Okay, last refinement. Move SSL dependency decisions into features. I haven't had a chance to work on this. This is an enhancement. I'm gonna put this on to consider for next release as well.
I don't think I'm gonna have time to get to it, but… yeah.
Okay.
And I think that's… that's it for, like, recent things.
Unless we want to do… live check custom policies…
**Jeremy Blythe** 13:10 Yeah, that's.
**Josh Suereth** 13:11 Is this a bug?
**Jeremy Blythe** 13:13 Maybe you could class it as a bug? It's a bug feature.
It's not really remote. It doesn't work the way… That the other way we use policies works.
**Josh Suereth** 13:29 Yeah, which… which… so it's an inconsistency, which…
**Jeremy Blythe** 13:32 Yeah.
**Josh Suereth** 13:33 We could classify as a bug or a feature, it's fine. Okay, I'll mark it as a feature for now, and we'll assign it later. Okay, I think that's it for stuff that came in.
I still… this one from, Michelle, I don't know how to read this one well. I need to actually… I read through it again, and I don't know.
Okay, cool. And I saw this one you actually have a patch for, right?
**Jeremy Blythe** 14:03 Yeah.
**Josh Suereth** 14:04 Yeah, that's awesome.
Okay, let's go back to the notes then, and let's talk about… by the way, I have a hard stop at, 1130… or 10.35.
Or 7.35, depending on what time zone you're in.
**Jeremy Blythe** 14:20 I think.
**Josh Suereth** 14:21 Jeremy, you do too? Okay. So let's talk about conflict resolution forward compatibility.
**Ludmila Molkova** 14:26 Yeah, so I'm curious what your… Think.
And why do we need anything complicated there? Like, what is the good scenario for granular overrides?
**Josh Suereth** 14:43 What's the good scenario for granular overrides?
**Ludmila Molkova** 14:46 Yeah.
**Josh Suereth** 14:47 like, what are you disallowing? And I think you're… like, I don't think dependencies work otherwise, but we can… talk about that. Like, so… you're allowing somewhat granular overrides, but not very granular overrides, right? So you're saying, like, deprecation overrides. But to me, that's confusing as hell.
It's particularly… it makes sense only if you're thinking of, like, SEMCOM, where you're moving something to a new location. It doesn't make sense in the general case at all. If I have SEMCOM, and I have some other thing, and I allow the deprecated to override the other thing, that is broken as hell. Like, that… that just doesn't make any sense.
**Ludmila Molkova** 15:31 Yeah, so what I'm trying to understand is what is the good scenario for the future? Imagine this is not a problem. We solved it in some way.
**Josh Suereth** 15:39 Yeah, yeah, yeah. Okay, so there's a few things I've been thinking about here. Like, one is, I want to have a discussion about what a dependency actually means.
You know how right now we, like.
Over… like, import the dependency things into your local schema, and by… there's a flag that puts them all there?
I'm starting to really question that… myself. I'm wondering if we should actually keep them in their own namespace, if you will. So when we resolve a dependency, you would actually get, like, here's your locally defined things, and then here's the dependency. And you actually can see both.
Like, there's a place for them in your template engine.
and then we had this notion that we talked about where imports will be kind of, late-bound.
That is a language term. What's about… maybe consider them pointers, right? So an import is a pointer, where if I change the version of the dependency and dependency resolution, I'll point to the most recent thing in that dependency thing.
Imports are the way that you would say, okay, my conventions are Semconv plus extra things.
And so… what I'm required to do at that point is resolve all the scenarios that I need to make this be a consistent singular schema URL.
four things, so I would import the things I'm using from Semcov.
But I'm still an independent thing.
Hold on. Okay, let me go to principles, because I'm… I think I went… I went the wrong direction. Let me restart.
Okay.
Principle number one that we want is all data that's generated in OTLP annotates schema, right?
So we know what it is.
That is schema your own.
There will be one.
for that. So what I'd like to have is an instrumentation library has one schema URL that it can write.
That will dictate everything that that instrumentation library is generating.
So let's go through, now, the logical conclusions of that, right? The next thing would be, if I have GenAI semantic conventions, and I want something to use GenAI semantic conventions.
I'm depending directly on GenAI semantic conventions, as opposed to having my own sub-thing.
I should be able to import the upstream SEMconv that I need for that to be a holistic schema URL, where everything is included in its schema URL, and those imports, you know, are kind of, like, locally available.
And I don't need to, like, look at dependencies at all. I just look at that URL for everything.
Okay.
**Ludmila Molkova** 18:32 Okay.
**Josh Suereth** 18:33 For that instrumentation.
Okay.
Then, if somebody in Gen AI is doing GenAI SEMConf, but is making some extension, they make a new URL that they have, they would import you, and implicitly, that would import just the pieces of SemConf that they need, right?
Okay.
Cool.
So, what this means to me is I need a way to have these downstream things be fully resolved, everything within them that you need, but only the things you need for that instrumentation.
And I need the ability to resolve conflicts there, at that point.
So, downstream dependencies, work.
But now I have this… I have the deadly diamond I have to sort out. So there's, like, a few ways we can… Deal with this.
But effectively, I'm thinking we have conflict resolution capabilities built in when you import.
**Ludmila Molkova** 19:37 So what I'm… why are you losing me in what I'm saying, that it's not valid to have one Thing.
was identical OTLP identity.
in two different registries. You cannot depend on something.
Was that unless we find a way. It's not a valid scenario. It's a temporary problem that we have with moving out.
**Josh Suereth** 20:06 Well, yeah, the other thing we could do, though, is we could just delete it from Zenkov.
**Ludmila Molkova** 20:13 We can! It will have an interesting set of problems, because everybody who caught Jan SEMConf will need to urgently fix it, and we will need to do the same for mainframes, for GraphQL, and so on, every single time.
**Josh Suereth** 20:33 Yeah, but it's also, if they code Gen for SEMCOV and they see everything is deprecated, that's gonna cause huge confusion for the community, too.
**Ludmila Molkova** 20:40 Confusions, yes. Breakages, no.
**Josh Suereth** 20:46 I, I honestly think it'd be better if you didn't deprecate in SEMCOMF.
At all.
And you just extend those things… When, like, in your sub… like, just treat them as kind of given, and extend them in your local.
**Ludmila Molkova** 21:02 So then, we would have to leave in the two repos all the time if we need to change a base node.
We would need to work here and there.
**Josh Suereth** 21:12 Yeah, that's correct.
**Ludmila Molkova** 21:13 Possible, but the… Sorry. So what I'm thinking, if we have a principle that conflicts Like, collisions are not allowed, period.
Well, they could be allowed with some additional hint, on the… on the core repo, in your dependency. Your dependency can say, okay, I'm not exporting it, it's there for docs.
For whatever reasons, but it's not.
**Josh Suereth** 21:41 Like, it's private. Yes.
**Ludmila Molkova** 21:44 Kinda.
**Josh Suereth** 21:46 Okay.
That… that, I think, would be okay.
The, the other…
**Ludmila Molkova** 21:58 or annotate them somehow, so that during dependency resolution, you know to ignore them. This is your fine-grained dependency conflict resolution, but in the dependency, not on the other.
**Josh Suereth** 22:11 Right, so the dependency, if I use it as a dependency, I can't see these things, they're invisible.
But, on the local schema, it is visible because, we still need to keep them in some fashion.
**Ludmila Molkova** 22:24 Right.
**Josh Suereth** 22:26 Yeah.
**Ludmila Molkova** 22:26 At least temporary.
**Josh Suereth** 22:29 Okay. I can see that. That could work.
That does actually solve the issue pretty well for us, if we have that as a capability.
Now, what… what is that thing? What do we call it?
**Ludmila Molkova** 22:46 Annotation.
Resolution excluded, or annotation visibility internal.
**Josh Suereth** 22:56 Yeah, yeah… Okay.
Yeah.
Maybe resolution excluded. That shouldn't actually be too hard to add.
I… we still have this issue, though, We still have the underlying issue in myPR, if you look at the failing test case.
of, what to do if we have Deadly Diamond.
**Ludmila Molkova** 23:27 I like your idea, if it solves it, of, using the pointers to the… Like, to the dependency, so that you resolve to a specific version, and then you always… Refer to the specific version.
**Josh Suereth** 23:43 Yes. It will take me quite some time… well, I should say, I ran into the limits of what agents can write for me.
So I'm now writing that code manually, or at least I'm writing the architecture for it manually to get… to get it kicked off, and then I'll have, you know, an agent help me finish, but it's, that will take some time, just word of warning.
**Ludmila Molkova** 24:04 That's… there is no burning need in the multi… Dependency things right now.
**Josh Suereth** 24:13 Yeah, do you think what we have in Weaver today is good enough?
**Ludmila Molkova** 24:19 It's good enough for, I think, for hotel purposes.
For now. Okay, so what happened? What will happen next?
somebody will create an Uber registry for GenEI, and… core repo, and this is where they will face the… limitations.
But… I would offer to help you. We're currently setting up all the GenAI Python things, but maybe in a month, I would have more capacity to help you with this.
**Josh Suereth** 24:55 No, no, we're dividing and conquering, like, we're… It… totally fine.
I think we need to divide and conquer. I'm just, I… I'm worried about all the other crap that's coming in at the same time, and trying to figure out when when do we need the deeper context resolution, and can I work on other things in the meantime, or do I need to prioritize getting this out as soon as possible? My intuition doesn't give me an idea for the priority here. Like, I feel like you're gonna run into a problem where if we don't have this fine-grained resolution stuff.
we're gonna be dead in the water, and so that's why I'm, like, nervous about it and want to work on it really hard, but the solution I proposed is actually rather difficult to implement. It's taking all of my brainpower to do, which I don't have a lot right now. I'm, like, at an all-time low. I need more coffee, possibly, but, Yeah, so that's my fear, is like, when are you gonna hit a wall, and am I gonna be there in time?
Okay.
**Ludmila Molkova** 25:56 I, I think, like, I don't feel it's a burning need.
**Josh Suereth** 26:05 Okay.
**Ludmila Molkova** 26:08 I might… Make a stab at this one.
And so they're…
**Josh Suereth** 26:16 I think… this, I think, is easy… much easier. This, this, yeah, I think you could actually just define it and then, have AI build that without it making a mess. I think you're fine. Yeah.
**Ludmila Molkova** 26:29 Yeah.
**Josh Suereth** 26:30 Like, that's probably an hour of work, with AI doing all the heavy lifting, and you prompting it and yelling at it that it's done. Yes?
**Ludmila Molkova** 26:39 Right.
**Josh Suereth** 26:40 Yeah, so this sounds like a reasonable thing for us to do. Cool.
I… let me, let me… let me try to elucidate my… my fear.
When we pull out mainframe.
or CICD, or whatever we pull out second.
When someone tries to depend on both GenAI and that thing, that is when I'm afraid.
That's when I think my PR is really needed, yeah.
**Ludmila Molkova** 27:13 It's sooner. It's when somebody wants to build an artifact with GenAI and the Quora repo at the same time.
**Josh Suereth** 27:21 That's fair, yeah.
Which might be almost immediately.
Okay.
If that's right, I think probably I should spend time, I should keep this as my top priority, of if you want to do the visibility thing, that'd be awesome, to kind of work around the current issue, and I will work on refactoring, the… how dependencies work.
The thing to talk about there is, I might have to change the resolution schema.
So, the res… the resolve schema might not… might not include the imports, it might include the imports. I need to figure out what I'm doing there.
But the resolution step right now, you know how we have, we have the definition schema that has your dependencies, we go through this resolve step, we get a resolve schema, the resolve schema expands into your, render schema. Okay. The resolve schema today Erases all the dependencies you resolved.
Like, they're ignored, they're gone.
I think I actually need Resolve schema, and I don't know if I need to serialize this or not, but I think I need to have it have all of the resolve dependencies in it.
to do this… to do the resolution effectively. Or I need to make yet another structure to confuse the crap out of all of us for resolution.
That stores all this data temporarily.
It's getting, like, the, like, the… that architecture's getting really awkward.
**Ludmila Molkova** 28:59 I see, you need it in memory, in runtime.
**Josh Suereth** 29:03 I need it in memory at runtime for sure.
But yeah, for doing this, like, pointer-based lookup.
effectively, we're erasing the dependencies very quickly. Like, we're doing almost like a linear linking.
Of, we load in the dependency, we link in the imports we need, we erase it, drop it, you know?
**Ludmila Molkova** 29:22 Yeah.
**Josh Suereth** 29:24 So I need to be less lazy, and that's where I started running into problems.
Okay. Alright.
I will… I will get a better architecture for you all and send a CL, but… but that's… that's where I'm at.
Would anyone be sad if I actually just removed or deprecated the import all flag?
**Ludmila Molkova** 29:48 I mean, include and referenced?
**Josh Suereth** 29:51 Yeah.
**Jeremy Blythe** 29:55 I use that all the time.
**Josh Suereth** 29:57 Would you be willing to move to import star?
Either that.
**Jeremy Blythe** 30:05 Who's…
**Josh Suereth** 30:06 Either that…
**Jeremy Blythe** 30:07 achieving the same thing, I don't care, but I don'.
**Josh Suereth** 30:09 If you use the flag, here's the other option. Here's the other option.
if you use that flag, are you okay if I change your, your Resolve schema to have import star commands. So basically, if you use that flag that implicitly forces import stars.
on that dependency Or on all your dependencies.
**Jeremy Blythe** 30:33 Like… I personally don't care, provided the end result is the same.
**Josh Suereth** 30:41 Okay.
What I need is, when you use that flag, I don't know that the import exists. So when I resolve a downstream dependency of you, I don't know that you include it all.
**Jeremy Blythe** 30:52 Yeah.
**Josh Suereth** 30:54 And so I can't do the pointer. It dies. Everything's broken.
But if, if, when you use that flag.
I am literally changing your definition to force import scars everywhere as, like, a convenience. Great.
But I… I still think it's ugly as sin, and I'd like to deprecate it and just tell people who need it to… put import stars.
**Jeremy Blythe** 31:17 I think that's fine, you can deprecate it, like, don't… I don't see that you need to do that step.
**Josh Suereth** 31:24 Okay.
**Jeremy Blythe** 31:24 But what… Where do I have my import star?
**Josh Suereth** 31:30 in your definition. So when you define a dependency, you then would say, import, you know, metrics, star, spans, star, attribute group, star.
**Jeremy Blythe** 31:41 Okay, because I don't think we did imports for attribute groups.
**Josh Suereth** 31:46 I thought I added them, but if not, I'll make sure they exist. I'm gonna send a CL specific… a PR specifically for that change, and Jeremy, like, I… if you could help me evaluate that, that'd be ideal.
**Jeremy Blythe** 31:58 Yeah, I do know that… like… I've offered that out in Slack and conversations to… People?
To go, oh, and while you're developing, this is really handy, because you can, like, look up things and do a live check against the whole library and all that stuff.
So I know it's not… it isn't just me using it.
**Josh Suereth** 32:23 I know it's not just you, but, like, because you use it, rely on it heavily…
**Jeremy Blythe** 32:27 Yeah, yeah, oh, I'm happy to test it.
**Josh Suereth** 32:28 gonna be able to find more bugs than I would, yeah.
**Jeremy Blythe** 32:31 Sure.
**Josh Suereth** 32:32 Yeah, that's all I need. I… and again, I'm not gonna remove the option, I would maybe just deprecate it and explain what it does, for people, yeah.
Okay.
But that… I… I'll send that PR first. Alright, we're almost out of time, we have, like, 30 seconds. Sorry, Ludmila. Forward compatibility.
TLDR. I read a bit of this, but I didn't have a chance to go into details.
**Ludmila Molkova** 32:56 And take your time.
**Josh Suereth** 33:00 Okay.
Is this where you have, like, an unknown fields, field in all the things, and then all the unknown fields get bundled into that, or is this… you went a different direction?
**Ludmila Molkova** 33:11 And now this is the direction. So, we have unknown fields on everything, we… allow them, if we know the version, we complain. If we don't know the version, We… Aww.
Leave a warning, saying… just a log warning, saying that we don't recognize this field, maybe you should update.
This is…
**Josh Suereth** 33:38 Yeah.
**Ludmila Molkova** 33:39 The stricter for results schema and manifest. For definition, we support the… Just major version, and also a major-minor version, and we… use different logic for different complaints if we know the minor versus don't know the minor. This is what we discussed in the past, and this is the same direction.
**Josh Suereth** 34:05 Yeah, awesome. Okay, so it's just ready for review? Beautiful.
**Ludmila Molkova** 34:09 Yeah, so the second one is stacked upon the first one, so it's hard to review it without merging the first one.
**Josh Suereth** 34:18 Yeah, the second one's the more complicated one. Okay, cool. I will review them as soon as I have a chance, then. Awesome.
Yeah, thank you. Thanks. We'll see.
**Ludmila Molkova** 34:27 Have a good day.
**Josh Suereth** 34:28 You too.
