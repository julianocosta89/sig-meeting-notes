SIG: Semantic Convention Tooling
Date: 2026-03-11
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/w46VrNeWx6Z79f0COV5KHkSc5a99cfBwVFNF4ljGvBgT1wh-V7AwjzN0aM8kBEnZ.rzRIVf7VAD3YOQ24
============================================================

## Zoom Recording Transcript

ariannavespri 00:01:24 Hello?
Josh Suereth 00:01:26 Hey.
I wonder if this waiting for host permission thing is, A lie.
Like, if I were an AI,
that's what I would do, is I'd just say, hey, I'm waiting for your permission before I do anything, but I would just still be doing everything.
ariannavespri 00:01:53 Yeah, yeah, frames are.
Yes, then there are so many different rules, like, depending on where you live. Like, Europe is one thing, America is another thing, but Europe is, like, highly regulated in any case, but… but maybe it's like, you know…
Josh Suereth 00:02:09 Yeah.
Yeah.
There was a time where I thought we were gonna go closer to the way of Europe, but we'll see.
ariannavespri 00:02:17 Yeah, yeah, yeah. But also, like, I'm in Europe, but I'm not in the EU, so that's yet another story, so…
Josh Suereth 00:02:24 Oh, yeah.
ariannavespri 00:02:26 in Switzerland, so…
Josh Suereth 00:02:28 Swissland's not part of the EU, huh?
ariannavespri 00:02:30 No.
Josh Suereth 00:02:31 Wow.
ariannavespri 00:02:32 Nope.
Josh Suereth 00:02:34 Huh. Okay. I know that it's the Swiss franc, right? But I didn't.
ariannavespri 00:02:38 Yes.
Josh Suereth 00:02:38 Not part of it at all.
ariannavespri 00:02:40 No, no, it's like, but the, like, as you, as you, as you noted, there are, like, countries which are part of the EU and have not adopted the Euro.
Josh Suereth 00:02:49 Hmm.
ariannavespri 00:02:51 But now Switzerland's never been part of, you and never thought of.
Like, you know, most of them never thought of being part of it, and I can understand why.
Josh Suereth 00:03:01 Yeah.
ariannavespri 00:03:01 No, yeah. Also, Norway's not part of the EU?
So… Iceland, yeah, yeah.
Josh Suereth 00:03:09 Huh.
Men.
Things, things I learned, yeah.
ariannavespri 00:03:15 I'm sure you were asleep better tonight.
No, indeed.
Yeah, yeah.
Laurent Querel 00:03:24 With this one?
Toy?
ariannavespri 00:03:28 I'm sorry?
Laurent Querel 00:03:28 Hi, everyone.
ariannavespri 00:03:32 I didn't understand, sorry.
Laurent Querel 00:03:34 I was seeing what happened during the night.
ariannavespri 00:03:38 No, no, no, nothing, it's just that we were, like, while waiting for the others, just telling… I was just telling Josh about what countries in Europe are actually part of the EU, and what others are not, and so he was quite a silly, so I… just a joke, yeah.
Laurent Querel 00:03:54 Okay, okay.
ariannavespri 00:03:55 It was.
Laurent Querel 00:03:56 I'm worried about some big event during the night.
ariannavespri 00:03:59 No!
Laurent Querel 00:04:00 I just.
ariannavespri 00:04:02 You just wake up, and I didn't read any news. No. Oh, thank you.
You know what?
Josh Suereth 00:04:08 I don't know these days, there could have been something, and we just aren't aware of it, yeah.
Laurent Querel 00:04:11 Yes.
Josh Suereth 00:04:13 Yeah. I'll just end that brief discussion with, I think Switzerland is my favorite country in Europe. I didn't realize it wasn't part of the EU. I've been there a lot.
But yeah.
ariannavespri 00:04:25 Oh, nice.
Liudmila Molkova 00:04:27 It's on the continent, and it's in Schengenzon, right?
Josh Suereth 00:04:31 It's Braden.
Laurent Querel 00:04:31 Yes.
Josh Suereth 00:04:32 too, yeah.
But it's gorgeous. It's one of my favorite places to go. Anyway,
Let's… let's move on. I wanted to have a discussion about what we think we need before we cut a release. So in terms of things that have been added.
Let me… let me take a quick… Look here…
Where's our… I didn't add my own release notes in the changelog, because I am super bad about that.
But, yeah, we have,
I mean, it's a good… it's a good set, right? So we have get references.
Liudmila Molkova 00:05:13 Oh, you're not sh… Oh, you're typing, I'm sharing.
Josh Suereth 00:05:18 Yeah, I'm pulling over, like, major things, live Check Health…
We have, the thing that I added, which is V2 refinements.
Working in definition syntax.
Kind of events.
we have…
Set output HTTP and stop. Basically, a whole bunch of stuff around live check, being more useful in CICD.
Oh, we have the unified output handling, which fixes a whole bunch of wonkiness with JSON and stuff, right?
We have… schema URL,
The manifests. Thank you, Lyudmila.
We have… Auto-skeeping is off by default now.
Then template, auto escape false. Yeah, okay.
We have, the change from version to definite file format definition V2, which is breaking.
And… Weaver Registry Package.
Right?
My thinking is, I really want to get…
For the most part, these are kind of… well, let me put these together.
Laurent Querel 00:06:53 There is also the registry infer.
Josh Suereth 00:06:58 I don't think that one… oh, that is in… there's a PR to move it, yeah. Registry Infer.
Let's talk about V2 syntax.
out, data.
I think these all, to me, constitute, like.
we're almost to the point where I think we can start stabilizing, and I really want to get these out to try.
And then we just have general goodness that people have been fixing over time, right?
Let me also make the… Stable by default.
No, we'll call it Weaver Packages.
Git reference is part of that, but I don't think we've done anything else.
Okay, anyway.
just to collect this list here, right? I think…
The only thing we have in the hopper right now…
sorry, the only things we have in the hopper. Let's take a… we'll take a look at the PRs.
We have, V2 lineage, which I think needs a lot of discussion, is not ready, and I don't think we're… we want to put that in.
We have a bunch of dependent bot problems. Moving in fur to its own crate, that's the one that…
I think is cosmetic right now.
Jeremy's package versus project, which I think we need to discuss more, but I don't think that's ready to go.
Finding override, this is… these are related. These are basically the same set of work.
The dog fooding one?
I think we had a bunch of discussions last week. I don't know if Jeremy had, time to work on it. He said he had work things come up, so I don't know if that one's ready yet. And then…
Multi-registry documentation, which I think I just want to redo this PR once all the V2 stuff lands.
What do you think?
Liudmila Molkova 00:09:01 Yeah.
And I think it landed. We can redo it now.
Josh Suereth 00:09:07 Okay.
Should I just re-prompt it from scr… the get-go?
Liudmila Molkova 00:09:12 Yeah, I think so, because it will… it doesn't make sense to… But it did…
first time, with V1 schema.
Josh Suereth 00:09:20 Yeah.
Okay, come on. Come on.
There we go.
You know, spend a little… 3 bikes… There are no doubts.
I'm just trying to fix this in court. I think this can wait till after the release, too, that doesn't have to happen immediately.
Close.
Okay.
Alright.
So, is there anything else we think we need
Before release, because I'm pretty sure this is… this seems pretty healthy, as of, like, an offering.
Liudmila Molkova 00:10:03 We need to fix resolution bugs, even for one… like, even without… like, with one dependency, we already have a bug, and from definition schema.
I can…
Josh Suereth 00:10:17 Oh.
Liudmila Molkova 00:10:18 Update my branch to not do crazy things with multiple dependencies from resolved schema.
But anyone who would take dependency on Auto would get random stuff.
Today. And this, this fix is trivial.
Josh Suereth 00:10:35 Okay. Do you have a PR for that?
Liudmila Molkova 00:10:38 No, I don't, but they have a branch that they shared with you, I'll send a PR from it.
Josh Suereth 00:10:44 Okay, yeah, I can take a look at that. I think you sent me the branch, I didn't have a chance to actually download it myself.
And take a look.
Okay. What I want to make sure we're doing with that is,
One of the things I saw, we… Have an issue with imports.
This is basically… If I have a transitive dependency.
Right? Should my transitive dependency be available for me to import locally?
Liudmila Molkova 00:11:21 That's so good. Yes, why not?
Josh Suereth 00:11:23 I think the answer's no.
And I think you always run into problems when you do that, yeah.
it's… this is… this goes into, like, API design. I would rather have you actually declare it as your own dependency instead of allow transitive dependencies to just invisibly show up as dependencies, unless you use the import syntax to re-export it.
think about a library, right? I'm using, an HTTP library that depends on some Network socket library.
I don't implicitly get access to the network socket library, unless that HTTP library, like, says, hey, I can… you can access it, you know?
Liudmila Molkova 00:12:03 You, you do, in most languages.
Josh Suereth 00:12:06 In… okay, in, like, Python, sure.
Liudmila Molkova 00:12:09 Python, Java.NET…
Josh Suereth 00:12:14 I… I see what you… yeah.
it…
We literally have a thing to, like, prevent that, because it's risky when you do that. Like, when you're depending on a transitive library without explicitly saying, I depend on it, right? It means that you have a potential, like, flakiness thing going on.
Liudmila Molkova 00:12:35 Okay, it's… it's easier.
But large documented, then.
Josh Suereth 00:12:43 Yeah, okay.
I don't know, I don't… we should probably go back and forth and discuss that. I'm willing to entertain allowing it to be available transitively to import. It's just,
It does make me pretty nervous with what we have right now.
Liudmila Molkova 00:12:59 No, I… I like being… I like… Having a simpler design, and…
Josh Suereth 00:13:05 Maybe eventually we could even…
Liudmila Molkova 00:13:08 Do this, because it's… it's all… it won't be breaking if we find it important.
Josh Suereth 00:13:14 I mean, the… the resolution algorithm today, if we… like, what you're suggesting we do.
Resolution won't handle published repositories correctly, then, that have a dependency.
Because if a published repository has a dependency, you have to re-resolve the published side. And we actually stop when we hit a resolved registry now.
We don't go further and deeper in the dependency chain.
Liudmila Molkova 00:13:37 I think we will have to.
We'll have to resolve dependency resolution problems. Oh, you're saying since everything is declared explicitly.
Then, we just ignore dependency resolution problems, they don't exist for us.
Josh Suereth 00:14:00 Right.
I… I agree with you, we have to figure out dependency resolution problems and fix them, and we have a bad… like, we don't have sophisticated, handling of it today. What I'm saying is, is physically, the way that we implemented the multi-registry thing, like, the way that's implemented today.
When you hit your first resolved dependency, you stop going down that chain.
Liudmila Molkova 00:14:23 Oh, and no, my rancher reproduces it.
Josh Suereth 00:14:27 Yeah.
And your branch, I think.
what I was worried about was, are we going to be exposing that previous thing all the time, or are you, like, resolving the upstream thing again? Like, are you making it so it goes deeper and resolves the transitive dependency as well?
Liudmila Molkova 00:14:44 My plan was to, say, here is a list of my dependencies on the resolved schema.
And those are the… List of all. It's flattened list of all dependencies, resolved… oh, sorry, immediate and transitive.
Josh Suereth 00:15:01 Okay, and it's, like, the schema URLs and where to get them.
Liudmila Molkova 00:15:06 schema URLs, and where to get them, yes.
Josh Suereth 00:15:09 Okay.
Liudmila Molkova 00:15:10 And it will be necessary… it's like a question of what should be in this list, but it's necessary for the,
for the resolution, because we need to say in the lineage, right, in the provenance, where this stuff came from. And I think this part, the provenance is important in the result schema. Less lineage, I… I still don't understand.
Josh Suereth 00:15:37 Let's, let's, I think I'm with you that we could probably start going to Providence. What I have concerns about is if it's both, like, the schema URL and where to download it, the problem is then publish is not mobile.
I think it can only be the schema URL.
Liudmila Molkova 00:15:55 Okay.
Yeah, I like it.
Josh Suereth 00:15:58 Yeah, and that means that resolving the transitive dependency is now a problem.
Where I might have to tell it where to find the schema URL.
Right. So, yeah, imagine I… I'm… I'm project B that depends on A.
Okay? Locally, I say, here's where A is, and here's the schema URL for it.
Right? To resolve. Because I have a local copy of it, or I'm in a proxy, or I'm in some sort of, like, safe thing. Okay?
I publish, and I say, cool, here is the schema URL that I'm depending on. I depend on A, the schema URL.
I can't… I can't… I shouldn't necessarily publish where I got it from, because where I got it from might not actually be publicly accessible to you.
Or there's risk there. So instead, I'm just gonna say, here's the schema URL.
And then we assume that you have some way of finding from schema URL to package.
Right.
Liudmila Molkova 00:16:57 Yeah, I'm probably with you, but I feel it's really weird to depend on something that depends on something that came from somewhere you could not access, and you don't know what's in it.
Josh Suereth 00:17:12 No, it's not, it's more the way that Project C that depends on B, gets Project A might be different than the way that Project B gets Project A.
Liudmila Molkova 00:17:22 This is awful. No. We should not. We should resolve one… one word.
Josh Suereth 00:17:27 of…
Liudmila Molkova 00:17:28 Project A.
Josh Suereth 00:17:29 Every dependency manager does this. Every single one. There's a way that you can proxy your dependency chains, so that I can have a registry that's local to my company, so I'm not hitting the public internet to get things. Every single register… every single dependency manager I'm aware of has that capability in some fashion.
Liudmila Molkova 00:17:49 Right, but, it still will resolve one thing.
One instance of specific dependency with a specific version, and it came from
somewhere, and you should still… like, do you need to access it? It's a separate question, but should you be able to access it? Yes.
Josh Suereth 00:18:11 Yes, however, what I'm saying is the only way I should get access to it is via the schema URL.
Liudmila Molkova 00:18:17 Okay, yes.
Josh Suereth 00:18:18 Yes. Like, I don't want to transmit anything else, and so.
Liudmila Molkova 00:18:21 Yeah.
Josh Suereth 00:18:21 That way, if we have some sort of abstraction layer from schema URL to where to really find it, with a proxy system, great, we're fine.
But only schema URL is actually transmitted.
Liudmila Molkova 00:18:32 Sounds good, yeah.
Josh Suereth 00:18:33 Okay, cool. Alright,
Let's… let's… so basically, before we cut a release, let's start fixing some of these resolution bugs.
I will, if you send your PR with some of your fixes, I'll take a look, and then I might start adding a bunch more tests and hammering on that, because as you saw, I think there's only about 3 multi-registered tests total.
in Weaver right now. So we probably need to really hammer the crap out of it.
Okay.
Cool.
I think that means we're not releasing this week.
Liudmila Molkova 00:19:09 Yeah, I don't think so.
Josh Suereth 00:19:11 Okay.
Given all this that's pended up, I do want to try to get a release out soon, so let's see what we can do, and see if we can get a release out next week. And let's move on in the topic. Sound good?
Okay.
Lineage. Here's a fun one.
Ludmili, you had a bunch of really good comments, and
Yeah, so basically what I did was do a very naive implementation of lineage for V2.
Super naive. So basically…
Why did this change? Oh, is this…
I need to take a look. That might be… testing V2.
Liudmila Molkova 00:20:00 Why your UX looks completely different grouped by Copilot?
Josh Suereth 00:20:05 Yeah, this is new.
It was, it was there last week.
Liudmila Molkova 00:20:10 Not for.
Josh Suereth 00:20:11 Okay, yeah,
Basically, it groups all the changes by Copilot, so you can look at, like, thematic changes, which is pretty fun.
It's… it's partially useful and partially really annoying. When it gets it right, it's really right. When it gets it wrong, it's really wrong, you know? But that's AI overall.
Confidently getting things done.
Regardless of whether they're right or wrong.
Okay, here we go. So, basically, it just adds lineage, and there's two types of lineage. There's signal lineage and attribute lineage. This just adds lineage to, like, event, attribute group, all that kind of stuff. What is lineage?
I'm actually keeping track of where an attribute came from.
Although I don't know if I frickin' need this anymore in V2, right?
The reason I'm keeping track of this is because of when we were due V1 to V2 transitions, I had so many exceptions and explosions and weird oddities.
that it's… that I have a big to-do of, like, how much of V1 to V2 do we want to support? Or do we just make this work in a V2 to V2 case?
And if you go from V1 to V2, we know things will be broken or weird.
And that's fine, and we don't care.
Because that's… if you want to know, like, why is attribute source just not the attribute catalog? Or, like,
you know, it came from… and I only have to track lineage of a refinement to say, this span refines this, so therefore this attribute came from the refined thing. It's because of shenanigans I ran into with the actual resolution engine being in V1.
Okay.
Laurent Querel 00:21:59 At least, don't you think that you should keep it optional?
Just for the same thing, for debugging purposes.
Josh Suereth 00:22:09 Oh, Lauren, I'm not seeing…
Laurent Querel 00:22:10 future.
Josh Suereth 00:22:11 rid of it, I'm saying I think I can actually shrink this down dramatically.
Like, I think we can… Same level of sophisticated tracking, with way less pieces of information.
Laurent Querel 00:22:22 Okay.
Josh Suereth 00:22:23 And so I want to go through a compression kind of thing of.
Laurent Querel 00:22:26 Yeah, like we did for the… Yeah.
Josh Suereth 00:22:29 Yeah, because there's a whole bunch of implicit assumptions in the model around refinements, where we don't have to track everything. We could actually say, attribute source either came from the refinement.
Or it was an added thing from this source.
If that makes sense.
So I think I can actually shrink this down dramatically.
Because we have ref group, where we can ref an attribute group to pull in something, and we have ref of an attribute, where we can reference the catalog, and then we have this came from the actual refinement itself. So I think attribute source can turn into a much smaller thing.
And we might not need to track… like, we might not need to keep lineage if it's from the implicit lineage, too. That's another thing I think could optimize this. Alright.
The other thing we have for attribute lineage is we have this notion of inherited fields and locally overridden fields. I… I think that we only need one of these two, because the other one should be inferred.
Liudmila Molkova 00:23:30 Why do we need them at all? Can you help me understand?
Josh Suereth 00:23:34 This is the part I think can be optional.
This is… this is, like, in Laurent's original prototype, this would let you see, like, where a definition came in.
But…
I can see this being used in a few cases. One is, I can see this being used,
For policy reasons?
So, if I find a policy violation with an inherited field, but there was a thing that suppressed the policy for my parents.
and I accidentally don't include that, maybe we could just implicitly say, cool, we're gonna ignore policy violations on things that are inherited, and we're only gonna report them against the top-level thing. Possibly.
Liudmila Molkova 00:24:18 Okay, so forge schemas too.
Josh Suereth 00:24:21 For what?
Liudmila Molkova 00:24:22 Still, forge schema.
Josh Suereth 00:24:25 forge schema.
Oh, because we need… yeah, we would have to have it in forward schema, yep.
Liudmila Molkova 00:24:32 But not… Resolved.
You don't need it for a result, especially if you're a declarate.
Josh Suereth 00:24:39 can't make forge schema unless you have it in resolved. This information's completely lost, you cannot reconstruct it, that's the problem.
Liudmila Molkova 00:24:47 I understand, but it means… it doesn't mean that we need to spit it out for resolved schema. It can be in the Rust code, but it doesn't have to be in JSON schema.
Josh Suereth 00:24:58 No, it does, because if we publish the schema, again, this information can't… if this information cannot be reinterpreted, like, if we cannot infer it.
We have to spit it out as part of the thing.
Liudmila Molkova 00:25:13 But this is going to blow out everything. Like, why do we try so hard to…
Reduce the volume of resolved schema.
Josh Suereth 00:25:25 Resolve Schema today has all of this crap in it.
Liudmila Molkova 00:25:29 Nobody uses Viva Unresolved schema, it doesn't matter. You cannot even make Viva produce it, so not a problem.
Josh Suereth 00:25:39 Anyway, I think there's a discussion of, is this information useful, and I don't think you think it's true, and I think it's true.
So what I can do is I can… we can take an iterative approach here, and we can keep a minimum amount of information. So, what you see today is bloated. Agreed.
And I think we need to find a way to, like, minimize what it is. That I think is fine. But when I plan and think about the things that we're gonna do with, like, inheritance, of multiple dependencies, when I think of, like, things we want to do around policies and stuff.
I think that this will be crucial. If you look at how we used it for V1, it was absolutely crucial.
semantic convention, just even the links that we have wouldn't work without lineage. Like, we use lineage for those, you know?
Liudmila Molkova 00:26:30 Without provenance.
Josh Suereth 00:26:33 What?
Liudmila Molkova 00:26:34 Without provenance.
Not lineage, right?
Josh Suereth 00:26:39 I think we use both, actually.
Liudmila Molkova 00:26:41 Okay.
Josh Suereth 00:26:43 Go ahead, Lauren.
Laurent Querel 00:26:44 Yeah… So, I do agree with,
The fact that this information will be lost, and when you import
A dependency, so a registry in a reserved representation.
Regarding the… so, could be… this information could be interesting, but what I'm… I'd like to, maybe, to explore is…
Regarding the policy idea that you mentioned,
Is it something that needs to be applied to imported registry, or only for your local registry that you are resolving it? And I think that's only the second one.
And if you agree with that, then…
You don't really need this information
to resolve a registry that is imported. But, yes.
Josh Suereth 00:27:42 Fair.
So, so maybe, I think the most important piece of information I want is this, and I want to actually sort out what provenance is, because provenance, I think, is problematic today.
So what I'd like to do is have provenance basically be schema URL.
and, a file name where we found that schema URL that we use locally, but when we serialize Providence and publish it, we actually publish our provenance with just the schema URL. So locally, Providence has a file name that we can use for error messages, but when we publish, we only publish schema URL provenance.
Does anyone have concerns with that?
Okay.
So, what… what I might do then is, I might actually just create a whole new, PR. Like, I think this one is good for exploring the space of
what would V1 look like in V2?
But for the purpose of what I think we actually need, immediately, that is missing, is V2 provenance with lineage. So we can make a signal lineage struct, we can put provenance in it.
And then we can use that everywhere, with schema URL.
And we can have it locally keep the file, and if we want to expand all these other things of tracking attribute lineage and all that stuff.
We can decide when… when and how to do that later.
Does that sound reasonable for… for now?
Okay.
I do think, Laurent, the, like I was saying, I think there's a way we can actually hyper-optimize these to be really, really, really minimal size-wise.
And really only track absolutely necessary things.
So, I think what we want to do… I still think there's a lot of value in this that we can unlock, but I think what we want to do is find the targeted use cases that we know we need right now, and add them in. And I think we can do it in a non-breaking way, it just means that we'll have a bunch of registries that don't have lineage.
out there in the world that we'll have to deal with, and I think that's okay.
The thing that I think is non-negotiable, though, is this provenance of knowing what schema URL a signal came from, or attribute group, or whatever. I think that is… that is absolutely needed.
Laurent Querel 00:30:05 And that also can be easily optimized.
And I think we should do it, day 1 for V2.
Because we could imagine that we have this list of registries or dependencies.
Where you have this information, you have, and so on, and then you just have a reference to that, for every single lineage.
Josh Suereth 00:30:28 Like we do for attributes and all those things.
Yeah, where's the, is it in other changes?
Where did you put my test data, you dumb-dum? Here we go, okay. So, in expected schema right now, we have an attribute catalog, we have the file format,
I think the manifest is separate, is that right?
Ludmilla.
Liudmila Molkova 00:30:52 manifest? It's separate.
Josh Suereth 00:30:55 Because what… Good.
Liudmila Molkova 00:30:59 What do you mean by manifest is separate?
Josh Suereth 00:31:01 The manifest of the registry that tells you what the dependencies are.
Is that… did we put that into the schema?
I think we.
Liudmila Molkova 00:31:09 Now…
Josh Suereth 00:31:09 No?
Liudmila Molkova 00:31:10 We didn't. It's only in the manifest.
Josh Suereth 00:31:13 Okay, I think I might want it in the schema.
Liudmila Molkova 00:31:17 Yeah, in the resolved schema, just with schema URLs, as we just discussed.
Josh Suereth 00:31:21 Yep, and with schema URLs. And then this becomes, instead of, like, path and registry ID, this provenance becomes basically, just the schema URL. Straight up. And then we can ignore these for now, all these attribute things, and that's all that we track for now.
in lineage, and I think that makes a lot more sense, because right now, this is like… this is meant to be that ID that is schema URL. Well, we're replacing that, getting rid of it, and this is useful only locally for error messages, and so we can keep it locally for error messages. So, alright, cool.
Laurent Querel 00:31:55 You can, so it's very close to what I was saying, but…
Josh Suereth 00:32:00 Oh, oh.
Laurent Querel 00:32:01 was…
Josh Suereth 00:32:01 I was saying that the provenance in this location could be a reference and not necessarily.
Laurent Querel 00:32:07 a schema URL. So if you have this registry of dependencies, you have everything very clear.
But you just have a one integer,
Yeah. As a value for the covenants.
Josh Suereth 00:32:21 Yeah, so it would look like this.
Yes. That's also… I meant to say that out loud, I don't think I did. Yes, that's… that's why I was asking first about can we put the dependencies in schema URL, in Resolve schema. So then we just reference the dependency chain with, like, the index that it is in that.
Laurent Querel 00:32:37 Yes.
Josh Suereth 00:32:37 So we'd sort them.
And then we can reference them by index, and then we get a much… Yes. …very small…
Yeah, okay, because that, that will actually be real, real tiny then. Cool.
Liudmila Molkova 00:32:49 And we also put it in Attribute Catalog.
Josh Suereth 00:32:54 That's the other part, yeah, I think for attribute catalog, for attributes that we import.
we should probably keep Providence there. Right now, Lauren, that was the other thing I, right now.
All the stuff we're tracking on groups. We're tracking the source of attributes, kind of, via this on a group.
But now that we have raw attributes, it probably makes sense to put lineage
Right into the catalog in some fashion.
Okay.
Let me quick sketch this out.
Okay, so… quick sketch.
We have, signal lineage.
uses, Providence… has data file, but does not serialize it to… so I have schema.
has, you know, the L, but uses a… Dictionary.
Look up.
Excellent. Thanks to you, man.
Right, first we have to add dependencies…
Right, it has human… I'm sorry, list.
Excuse me, your L.
in residing schema.
And then we're going to add an attribute linear inch, right?
Attribute.
And catalog, and then,
similar shape.
Signal. Shoot. Do. Signal.
lineage, just providence. Alright, does that sound reasonable?
I'm also thinking about, for the attribute catalog, you can tell me if you hate this, forcing you to go through a lookup. So basically, the attribute catalog is a big array of attributes. We have a, attribute, we also have an array called the lineage.
Array, which is a array of the provenance
So, it's just an array of numbers that points to the provenance. I'm thinking about doing that.
Laurent Querel 00:35:25 Yeah.
Josh Suereth 00:35:26 So if you need… if you need your attribute lineage, you have to go back to the catalog and ask for it.
But it means we basically have two arrays. I mean, I guess it's not that much different.
We can put them together.
Okay, cool.
Alright, next up. Jeremy's not here.
Unfortunately, oh, sorry, was there anything anyone wanted to say about Lineage and V2 before we move on?
Cool.
So this proposal… We have 3 approvals.
Liudmila Molkova 00:36:13 I haven't…
Josh Suereth 00:36:15 Yeah, what?
Laurent Querel 00:36:17 Sorry, excuse me, back to the previous question.
I was re-reading the registry resolution document I wrote a long time ago.
In the, the, the dependency list.
First point of your quick sketch.
Josh Suereth 00:36:36 Do we have the version…
Laurent Querel 00:36:38 I think version is important, for, conflict resolution.
Josh Suereth 00:36:48 Yeah, so schema URL is both the name and the version.
Laurent Querel 00:36:51 Oh, yeah, yeah, yeah, my bad, sure.
Indeed.
Josh Suereth 00:36:55 Okay.
Cool. Alright, let's go, let's go to this one. So this is, Jeremy made a proposal around fixing config in Weaver.
I really, really like this, and I wasn't sure what's hanging here. There was a bunch of good discussions going.
Liudmila Molkova 00:37:14 I'm questioning, two things. One, I don't remember what, but the second one, why do we need to merge multiple configs together? I… I don't get it.
Why are we even considering it?
Josh Suereth 00:37:29 This year.
Liudmila Molkova 00:37:31 Yeah.
especially if you have something like registry in the config. Walking up and merging configs for different registries is not…
Good.
Laurent Querel 00:37:45 I think a good example, Lumia, is,
the, the, like, like we discussed last time, monorepo, and, and the case where you, you have,
Needs to support multiple languages, for example, for a client library.
It will not make sense, in my opinion, to repeat yourself again and again.
for each client SDK, because it's a different language, and repeat the acronyms each time.
So the… And we already, and we know that, we already have people using this approach, today.
For example, the… I remember a guy, with his hair long in the Elixir.
they used the initial hierarchy approach I put in place to basically,
Specify what needs to be reused across different languages.
In that case, it looks here and analyze.
So the same problem, will happen again and again for, for monorepo.
For different purposes.
Josh Suereth 00:38:52 Lauren, could we take the approach cargo takes here, and have, like, a workspace?
Section, and then in the subprojects, you would say, like, you know, setting.workspace equal true, and that says to inherit from the parent.
So it's explicit.
Laurent Querel 00:39:08 Yes, why not? But that doesn't change the… yes, it's a slight variation around what,
I think Jeremy proposed there, but we still need to override, so… but to answer the question, the initial question from Milmila.
What you are exposing is a variation that could be a little bit more… Safe.
I think that's the purpose of the… of this approach.
But still, we need to have an override mechanism to simplify the life of people in this kind of use cases.
Josh Suereth 00:39:48 Yeah.
Liudmila Molkova 00:39:51 The… the… the… the idea of… having multiple…
registries in one mana repo is… Just chill.
It's super edge case.
And we are…
also, not that we are adding something that they cannot do. We're helping them not to write a few lines of
Config code.
Laurent Querel 00:40:18 I think it's not HKS, I mean, it's… it's the case.
Because if we consider that the registry, not the intermediary registry, but the registry that you will have, assigned to a microservice.
You don't want to expose for this microservice
the merge of all registries for all microservices. You… you… it's important to understand exactly, for example, for life check.
And you… and you want to create an instrumentation coverage approach integrated into your CICD.
You don't want to get the signal of any other… microservice.
you need to get only the signal from this microservice in order to implement properly that I've checked integrated into CICD.
So that's why it's… it will be a collection of projects we're not…
A single one that is the merge of everything.
Liudmila Molkova 00:41:21 You're saying that, okay, there are subfolders in this modern repo with microservices, and each has individual registry. How would you put the configs in specific locations? Like, how would you know where to put configs? And you would, okay, you would have them spread across the repo, and one you would have in the root, or in the root of some, at least some folder.
It's so many implicit things that will be easy to break. We will have problems with merging stuff from these configs, and sometimes they will contradict each other.
why are we need… do we… do we actually need the complexity? You can find the case for it, but it's complex as hell, implicit, and hard to document, and nobody, like, knew… Jeremy, Josh, and me, we didn't know that Weaver does it today.
Josh Suereth 00:42:11 I knew, I knew.
Liudmila Molkova 00:42:12 Okay, you knew.
Laurent Querel 00:42:14 We know, and we have users using it. I mean, it's not a new thing at all.
Josh Suereth 00:42:18 Yeah.
Laurent Querel 00:42:19 We, we, we, we had discussion on that on the, on the channel multiple times.
Yeah, I think it's…
Josh Suereth 00:42:27 It's true that Semantic Conventions doesn't use it, and I think if you're a simple user, you wouldn't use it at all. But I agree with Laurent, like, all our advanced users are using that feature. And working at a company with a giant frickin' monolithic repository, I think it, it'd be nice if we have that feature.
Liudmila Molkova 00:42:46 use it for Azure SDKs. We would put configs in a special folder, not… we would not keep them in the root.
Josh Suereth 00:42:55 Sure. We would have a special folder, but we would have subfolders. Like, so the idea would be every team might have a folder that they have ownership and write access to for their specific signals, but they cannot modify, like, the baseline properties that we want them to have across the whole repository for the company.
Right? So, like, I hear what you're saying.
I, I still think, how about I'll say this?
We could start without it, and we can add it in, but if somebody's willing to contribute the code to make it work, because they find it useful.
I don't think we necessarily say no, we just guide them on how to not have it be a horrible mess. Like, if you're worried about this being a horrible mess, great, let's shrink that down.
Like, from my perspective, I would want something like this for our company. I know Laurent wants it for his company, so you have people who see a use case and want it. So let's just make sure it's not hard to maintain.
Laurent Querel 00:43:53 And I'd really like to see a description of the mess that you are describing, Lemire.
Because I'm not convinced that there is a mess at all. We have so many examples
Not related to either… That works this way.
So why, why… so, just like the, what we, we mentioned before, cargo.
Is working this way.
I mean, it's not… it's not a new thing to have, configuration file.
That are hierarchical, and resolved in a hierarchical manner.
Liudmila Molkova 00:44:36 It's not the new thing, but it's used in the… ubiquitous tools.
future ecosystems. We are not that, at least yet. My concern, the mess, both configs… my concern is people would put crazy stuff in the configs, and it will have
conflicting stuff. Maybe if we say that policies are declared in the manifest and never declared in this config.
this, my concerns would be eliminated, because then it's just a config of how River runs, not what it…
validates.
Laurent Querel 00:45:14 So, maybe there is a misinterpretation on my side.
We are talking about the new Weaver TML file, right?
Liudmila Molkova 00:45:24 Yes.
Laurent Querel 00:45:26 Okay. I don't remember seeing the policy in this one.
What I remember is…
Liudmila Molkova 00:45:35 We've been discussing having registry in it, and this is the other discussion that is still… I feel, is important.
That having registry inside this config is… Sounds… wrong to me.
I can, explain why.
But.
Laurent Querel 00:45:56 maybe I didn't, follow the last discussion on that, because for me it was more,
Seems like, Dictionary of, of terms,
And parameters, this kind of thing that we were looking at, override with this mechanism.
I don't remember anything regarding policies and other things like that, but .
Josh Suereth 00:46:30 Well, it's… it's implicit here, Lauren. Like, right here, this templates one.
This is a package, and so yeah, this is the, like, template for what you're gonna render, so you don't have to.
Laurent Querel 00:46:40 I think that has been, added recently.
Josh Suereth 00:46:44 Yeah.
Liudmila Molkova 00:46:45 Policy section.
Laurent Querel 00:46:47 Okay.
Josh Suereth 00:46:49 Yeah, so…
Laurent Querel 00:46:50 There are some extensions now that didn't exist, I think, during the first video.
Yeah, I can understand why, but…
So, for me, the right decision will not be to remove the override mechanism, but maybe rethinking what we put into this file.
The simple example of multi-language is, I think, a so common one that I have some hard time to understand why we will not be able to use that, even without monorepo.
You have a project, not Mono Repo, just a single project emitting multiple client SDK in different languages.
Do you really think that you have to repeat yourself again and again for each of those, sections, like the template, like the…
The white space control, like, the… the acronym, and so on.
Liudmila Molkova 00:47:46 I, I'm not worried if it's just the… the…
I don't know how to even describe it, some minor configuration that controls weaver behavior. But I have a proposal that policies, the list of policies you follow, and maybe even the list of
I think we can start with the policies. Like, the location of the files and the policies, or in the manifest. Like, the manifest is the location. You pass the manifest, and here you go. And manifest can contain the list of policies you're supposed to run against this repo.
You can ignore them, maybe, or override them, but that's part of the definition of the registry.
And then, if we don't make it part of the config, merging becomes… it starts to make sense.
Josh Suereth 00:48:44 I think I see what you're saying, Laurel. So you're, like, there's a piece of this which is, you want to divide it and put it into the manifest, and I like that direction. Maybe we need to take that idea that… and… and mer… like…
But literally.
I think Jeremy wanted everything that you're suggesting to be in this new TOML file.
Liudmila Molkova 00:49:03 Right.
Josh Suereth 00:49:04 But I agree that maybe it makes sense to have a good piece of it in the manifest, because that's actually your project definition. Like, that's… that's our equivalent of cargo tomol for a thing, right? And this is more like the,
the workspace tunnel.
Where it's like a set of shared things that you can reuse, so you could reference them. Yeah.
I think the TLBR, from my perspective, I wanted to see if we still had contention in this proposal, and we absolutely do. I didn't… I wasn't gonna click the merge button, honestly, because I was like, huh…
this has 3 approvals, but then I looked at the comments, I'm like, maybe it doesn't have 3 approvals. Maybe it has… We love the idea, but we disagree on how to get there, and so I think…
Liudmila Molkova 00:49:53 We'll keep treating it that way.
Laurent Querel 00:49:55 Yeah, and also the… I think the state of this, initial PR changed a lot, over time.
Because there are some elements there that I don't remember to see, during the first reading.
Liudmila Molkova 00:50:12 Yeah, and approval on the RFC is…
Doesn't mean approval on implementation details, yeah. Love the idea, but yeah.
Josh Suereth 00:50:22 Yeah, and I… honestly, I think that's…
the thing I want to get to, maybe what we should do.
is, can we agree to start having, weaver.yaml
target the policies, as a direction forward, and maybe we can… like, I think this is already true, but we can just document it. The Weaver.yaml hierarchical lookup, we will never do.
for policy packages, today. Like, for now.
Liudmila Molkova 00:50:55 For a registry.
Josh Suereth 00:50:56 Or, or register, sure. And we can,
But maybe we can limit the initial thing that we implement, and use this directionally and aspirationally, and we can flesh out better proposals that, like.
account for some of the concerns we hear here. Because I think we all agree, we want, like, there should be a config file for a Weaver package that is independent
Of everything. It's just how the package works. And then there's this configuration for your project that might need to influence it with, like, here's a set of acronyms and things, and the Weaver package should be able to get that data in some fashion. But we want to divide Weaver YAML and that mechanism from each other.
Is that fair? Okay, cool. So if we agree to that, maybe we update the proposal to just say that for now, get that through, and then we can do a Phase 2.
Awesome.
We have 8 minutes left, and I had one last thing to show, quick.
Which is, now, here's what's funny, okay? Basically, I wanted to, we've had a few PRs where Dependabot or Renovate fails because a Rust API changes when we do a version bump.
So, I was like, you know what, let's see if AI can do all the stupid function renames for us.
So it's a lot easier to deal with these.
So, I was… been waiting for a failure for weeks. And we had one.
And I said, hey, here's a set of instructions that I wanted to give you, and go fix the braking change. Now, and it did, but here's what's hilarious, okay? So…
here's the description for what it's supposed to do. You can read through this, and I think this all works. It's supposed to create a PR against main, it'll say it fixes the original PR number, and it will go through and, like, do renames and things for us to make sure that things work.
And then it's supposed to… I might need to add to the workflow to, like, validate that cargo format and cargo test.
Batch. So anyway, I wanted to get… oh yeah, that's already here. Verify that it works.
So… This, this worked.
The funny part is, the breakage for RAND that I had waited so long for was not a renamed breakage, it was a transient failure. So just making a new PR was… I could have just asked Dependabot to rebase, and it would have been fine.
So it was… it didn't have to do any work at all.
neil yashinsky 00:53:31 The test worked, right? I mean, you still got to validate the approach you're trying to validate, even if it was, like, a false positive, I guess, is that right?
Josh Suereth 00:53:39 Yeah, but I don't know how well it's gonna handle the actual function renames, but I want.
neil yashinsky 00:53:43 Right, right, right, right. It was, not the most effective test you thought it could be, but it was at least… it didn't break a bunch of things. Exactly, exactly. I'll take it, it's a win.
Josh Suereth 00:53:54 Yeah, so the cool thing is, I think it… I'd like to get this AgentMD file in. I have them both together in the same PR. I can pull it out if you want. I think I'd like to get this in so when we see Dependabot changes, we can… all of us can take a crack at just saying, hey, go fix this change, and then let it come back, and that should help
alleviate some of that. How do we feel?
Laurent Querel 00:54:16 Already cooling.
Okay, I will, I will, steal it,
We'll take this file, into another… into another project.
Josh Suereth 00:54:27 Yeah, feel free. And for context, I found the best way to write these is if you have a session with an agent where you're getting it to do a task, at the end of the session, say, hey, can you create an HMD file for me that explains what we just did?
And, then you, then you just tweak whatever the heck it makes from there. Yeah.
Liudmila Molkova 00:54:48 And then the research shows that it takes 3% of future recessions being productive.
Agent-generated Hedge SMD is proven to be not productive.
Josh Suereth 00:55:02 Yeah, I mean, it depends on what you're talking about, but I think… I do think there is something to agent skills. I do wish frickin' GitHub had, like, skills, or souls, or whatever the hell the equivalent is for GitHub Copilot, but right now it's literally separate agents, so whatever.
neil yashinsky 00:55:19 I don't think they've really figured out…
That skills both need to be a set of execution, or, you know, execution instructions, but there's also an aspect of versioning themselves.
That, like, it kind of… I don't want to say it breaks the model, but I don't… it just doesn't… I've seen very clean support for such a thing, and I think that's where, like, if they did, it would be amazing, because this is the perfect scenario where you'd want, like, if you will, versioned skills. Because I think your assessment of getting that Agent MD is correct. And I'd just like to add, like, if you can get a second session…
You know, where you've taken that MD, and you've used it a little bit, and a second session, and then say, oh, now, update it based on what we've learned. I think you, you know, like… it's obvious, of course, but just one other…
Josh Suereth 00:56:04 Yeah.
neil yashinsky 00:56:04 thing I like to do.
Josh Suereth 00:56:06 That is exactly how I do all of my agent skills locally, is, anytime it runs into problems and I have to tweak it, I say, tell me how you'd update your skill right now, and then, like.
neil yashinsky 00:56:17 I literally made a skill update skill yesterday for just that purpose. I don't know if that's overkill or not. I feel like the snake is starting to eat its tail, but maybe not. I don't know.
Laurent Querel 00:56:28 Something I did yesterday, also, in this, in the same,
area, a long session to implement something.
And at the end of the session, I ask, okay, can you create a prompt
That will, describe things that I want to check on future PR.
The truck party wound.
neil yashinsky 00:56:52 Yeah, that's a good…
Josh Suereth 00:56:53 Actually, one of my coworkers who's, he's a Prometheus maintainer, Bartek, he was just sharing with me, he has a really cool, like, prompt for getting, a good review of a PR.
That tells you, like, the things to look at.
You know, this touches security, go review the security in this file, this touches blah blah blah. It's not a review itself, it's like a how you should look at the… I really like that prompt.
Laurent Querel 00:57:23 I'm using that every day, running multiple sessions in parallel in
The avalanche of PR that I have to review every day, I'm doing that.
Josh Suereth 00:57:35 Yeah, well, so GitHub Copilot has instructions that we can put that in. Would we want to try that in this repo?
Liudmila Molkova 00:57:45 We tried it in semantic conventions, and at that time, it didn't use instructions for review.
But if it can now, I think it can now. And it had no effect, I think.
So now I think…
Josh Suereth 00:57:58 Yeah.
Liudmila Molkova 00:58:00 But it's been, like, 6 months ago, or maybe more.
Josh Suereth 00:58:04 Well, is that because of our stuff throughout the context window?
Liudmila Molkova 00:58:08 I think it just didn't understand that it can use instructions for quad review, and this is where they are the most useful.
Josh Suereth 00:58:14 Yeah.
If anyone's interested, maybe, Lauren, if you have something you're happy with, feel free to, like, send a GitHub co-pilot
Review instructions, and let's try it out, see if it.
Laurent Querel 00:58:26 Yes, me too.
Josh Suereth 00:58:29 Cool.
All right, I exhausted, all of our time with agenda items. Apologies. If there's anything else that we missed,
Yeah, apologies we didn't get to anyone else's stuff, but I think… I hope, Ludmila, I captured your concerns and my concerns, so I think it's good discussions.
Yeah, dude.
Liudmila Molkova 00:58:48 Thank you.
Josh Suereth 00:58:49 Okay, one last thing. The OTEP you have, I think I approved it.
Liudmila Molkova 00:58:57 You approved it, but I really want to get Trust's approval, and I didn't have a chance to do something realistic that would apply to, let's say, Java.
Yet. So I think this is pending, and I'll try to get to it as soon as I can, but my next few weeks are just crazy, sorry.
Josh Suereth 00:59:18 That's fine. I just wanted to check on status. So, like, the next thing for that OTEP is we want to get an actual demo with Java.
Liudmila Molkova 00:59:26 Yeah.
Josh Suereth 00:59:27 Okay, because the federated CENCOM one that I have, I want to delay putting that into review from draft until yours is through.
So if there's anything I can do to help there, let me know, but I figure we have enough on Weaver that I'll be swamped anyway.
Liudmila Molkova 00:59:43 Yeah, so let's… let's focus on Weaver. I'll do this as soon as I can, and yeah.
Josh Suereth 00:59:49 Cool. Awesome.
Laurent Querel 00:59:50 Is there anyone here that is going to the Absarity Summit in May?
neil yashinsky 00:59:58 I don't think so. Where is it?
Laurent Querel 01:00:00 the observability to submit, in May, I think it's.
Liudmila Molkova 01:00:04 Minneapolis.
Laurent Querel 01:00:05 Yes.
neil yashinsky 01:00:06 Minneapolis?
Laurent Querel 01:00:07 Yes.
neil yashinsky 01:00:08 Oh, interesting.
Do you know who's putting it on?
Laurent Querel 01:00:11 I think I will be there. It's not yet sure, but.
Liudmila Molkova 01:00:16 Did anyone come into KubeCon?
Laurent Querel 01:00:19 And keep fun, yes, probably. Yeah, it's in November, right?
Liudmila Molkova 01:00:23 Yeah, I mean… In… in two weeks.
Josh Suereth 01:00:26 The 1 and 2.
Laurent Querel 01:00:26 Oh, no, this one I will not be there, sorry. No, no, I was talking about the North America coupon, not the Europe.
Liudmila Molkova 01:00:34 I'll be, I'll be at the KipCon.
Josh Suereth 01:00:36 In Amsterdam. Nice.
neil yashinsky 01:00:40 Good for you. And there's something in May, too. Is there a CubeCon event in… or a Cube something event in Toronto area, or, Canada in May, I just saw? Anybody know?
Josh Suereth 01:00:50 That might be…
neil yashinsky 01:00:52 conference or something?
Josh Suereth 01:00:54 Huh, interesting. No, I don't know. In Toronto, that's like a 4-hour drive for me, so maybe…
neil yashinsky 01:01:01 Yeah, we kind of meet in the middle, maybe, even, Josh. Where are you based?
Josh Suereth 01:01:05 I'm in Pittsburgh.
neil yashinsky 01:01:06 Oh, okay, yeah, I'm on the other side of Lake Erie in Michigan.
Josh Suereth 01:01:10 Oh, nice! Okay, yeah. If only we could drive through Lake Erie.
neil yashinsky 01:01:14 We need one of those, amphibious cars.
Josh Suereth 01:01:19 Yeah, yeah.
neil yashinsky 01:01:20 It's a 3-hour tour, I'm sure.
Josh Suereth 01:01:21 Yeah, well, it's like… it's like a 5-hour drive to go around, or.
neil yashinsky 01:01:25 Right.
Josh Suereth 01:01:25 an hour through, you know? So, anyway. Alright, thanks everybody. We'll see y'all next week.
neil yashinsky 01:01:31 Same, thanks. Have a good one. Bye.
