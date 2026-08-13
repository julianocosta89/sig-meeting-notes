SIG: Semantic Convention Tooling
Date: 2026-08-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jeremy Blythe** 00:43 Hello.
**Josh Suereth (Google LLC)** 00:49 Hey, I was worried I was on the wrong Zoom.
because you made notes, and I didn't see you here. And I was like, oh…
**Jeremy Blythe** 00:58 No, I joined, and then no one was here, and then… but then, I think Arianna is trying to join, but she's in the wrong one, so there's still a mix-up with these links.
**Josh Suereth (Google LLC)** 01:07 Yeah… okay.
**Jeremy Blythe** 01:13 Post this. Paste this for her.
**Arianna Vespri** 01:16 No, I'm here.
**Jeremy Blythe** 01:18 Okay.
**Arianna Vespri** 01:18 I don't know why in the calendar there is another one, or maybe I don't have, like, an updated calendar. It also says Semantic Convention Tooling.
**Josh Suereth (Google LLC)** 01:29 Yeah, there's, like, two calendar links, so if you had a copy of the calendar, and not.
**Arianna Vespri** 01:34 Yeah.
**Josh Suereth (Google LLC)** 01:35 Then it… it's broken, yeah.
**Arianna Vespri** 01:38 Okay, I mean, I used the one in the notes, so it's okay.
No.
**Josh Suereth (Google LLC)** 01:46 Gotcha.
**Jeremy Blythe** 01:50 That's my go-to. I always click the link in the doc, so…
**Josh Suereth (Google LLC)** 01:57 Well, Jeremy, do you want to take it away? I think we have to talk about your PR. I was… I'm only… like, 30% through it, because I was trying to go through, like, the details in my head.
And, yeah, our resolution algorithm is complicated.
**Jeremy Blythe** 02:12 I'm just worried about…
**Josh Suereth (Google LLC)** 02:13 bodies.
**Jeremy Blythe** 02:14 I'm not sure we need to go through all the detail of it, and it's probably better that you… Go through it.
I just… I just want us to… I'm a bit concerned about the scope of it.
Because it was… Originally, it was like, oh, I've got this problem with entity associations that they're not… they're not really being resolved, right? So they were just free strings. You could put anything in there, you wouldn't get an error.
It also meant that we couldn't… we were then getting import problems because… because they're not resolved, certainly in what I do at work, we were then having to import Into the upstream, which meant that downstream.
they then went to import again, and then we're getting a fault, because we're, like, double importing something, because, like, all of that's not… so I… my intention was… with the PR was to kind of fix that at the surface level, but it seems to… I think that… as we've got into it, it's grown in scope, and I'm just a little bit… As you say, it's complicated.
And if I just keep growing and growing the single PR, we're gonna have, like, thousands of things all thrown into one. I don't know, I can carry on and do that, it's just gonna be a giant PR if I… Like, the thing… the thing Lauren pointed out, which was to do with logic error, that was cop… that was a block that's copied from how, like, existing to-dos on all the other signals.
**Josh Suereth (Google LLC)** 03:48 Yeah, well the…
**Jeremy Blythe** 03:49 Copy that up.
**Josh Suereth (Google LLC)** 03:49 The logic… the logic error where it doesn't print something, if you looked at where that existed, there was an if check To make sure it wasn't an option, and then there was a match later, or something, where, like, you were guaranteed to never hit that use case.
Theoretically.
And so, that's… that's why that was there, because I literally tried to execute it to make it fail, and I couldn't. But… we could have refactored the code, and now you can hit it. I don't know, you know, like, but at one point in time, that was impossible to hit. So if you copy-paste it blindly without the if check, that's a problem.
**Jeremy Blythe** 04:29 Yeah, there's… what I'm coming up against now is that there are failure cases That are being uncovered because of things like that.
**Josh Suereth (Google LLC)** 04:39 Yeah.
**Jeremy Blythe** 04:40 To do with the compatibility with resource.
Yeah. And so I think, like, even the thing you just mentioned.
I just looked at that, and actually, there is a… there is a bug in there, and it's to do with resource again.
But I was going to defer, like.
dealing with resource and throwing resource away into another PR, but now I'm like, whoa… Maybe… maybe all that needs to be pulled in, I don't know.
**Josh Suereth (Google LLC)** 05:15 I think we should try to walk before we run with this PR. Are you… you're enforcing entity associations exist in this, right?
Because what if… what if we start with the first thing where, for entity associations, we just, make sure the references are legit and issue a warning otherwise, as, like, step one?
**Jeremy Blythe** 05:35 Yeah, that's fine.
**Josh Suereth (Google LLC)** 05:37 You already have that as a separate PR?
**Jeremy Blythe** 05:40 No, that's in this one.
**Josh Suereth (Google LLC)** 05:41 No, what I'm saying is, let's make that a separate PR.
**Jeremy Blythe** 05:44 Oh, I see, like, dissect this one a bit.
**Josh Suereth (Google LLC)** 05:46 And then, yeah, so we can, like, focus on each, because you said this one's getting really big and unwieldy, right? So…
**Jeremy Blythe** 05:53 Well, it's been growing.
**Josh Suereth (Google LLC)** 05:56 Okay.
I need to finish reviewing some of it. I do like some of the refactoring you're doing, but I'm wondering if maybe we should do some of those as separate PRs?
Just to, like, you know.
Take baby steps as we walk through this.
**Jeremy Blythe** 06:15 Yeah, I think I agree. I… because we… you mentioned this before, when we were looking at another issue. I feel like we're just kind of picking away at this.
And maybe there's a bigger refactoring.
And I feel like… I feel a bit like I'm coming in from the side, having not, like.
Sort of putting all the… All of the blood, sweat, and tears that you did to get it to this point.
**Josh Suereth (Google LLC)** 06:41 Well.
**Jeremy Blythe** 06:42 Seriously.
**Josh Suereth (Google LLC)** 06:43 Yeah.
**Jeremy Blythe** 06:43 starts again from the side with, like, oh, but this doesn't work, and that doesn't work, and that doesn't work, and kind of picking away at it.
**Josh Suereth (Google LLC)** 06:48 I mean, the reality is, at some point, if we could get rid of V1, We could really simplify everything.
**Jeremy Blythe** 06:56 Yeah.
**Josh Suereth (Google LLC)** 06:56 because we can get rid of so much… we lose so much going into V1 and back, like, because we have to do all this weird inference of, like, oh, are you this, are you this, are you this, are you this, that we don't have to do if we could keep it as V2. But the other thing is, and this is… this goes into our discussions, like, a couple months ago, of… we're in an interim place where imports are not really imports, right? They are… like, nested in the upstream schema. So what you're doing, another way to approach it would be, if I want to validate entities exist, I would look into all the downstream dependencies and see if they're there.
And if they're in one of my dependencies, I could optionally upgrade them and import them, but I don't need to. I can just look at them directly, I have them there.
I've already resolved the dependency.
So, the fix that I have for, the Weaver Resolve schema that adds dependencies, right? You could actually just go look through your Resolve dependencies.
for the entity in a dependency if you don't find it in core. But we had this issue where we're trying to treat everything as a flat as a flat repository, and as a set of dependencies. So, like, all the things you expect from having a language, where you would say, okay, this references this thing that's over here, we don't have, but the other thing that I think is the main mistake that you caught Maybe the resolve schema dependency, entity ref should not be the string anymore. It should literally say, I am entity named X from this dependency. It should have provenance with it.
So you can look at it and say, if it doesn't include a provenance, I can find it locally. If it does, I have to go look through my dependencies to find it.
Right? If the entity ref said, I depend on this entity from this dependency schema.
**Jeremy Blythe** 08:48 In the definition.
**Josh Suereth (Google LLC)** 08:49 In the… no, in the Weaver Resolve schema.
So, if Weaver Resolve Schema has that, Right.
**Jeremy Blythe** 09:00 Didn't I do that? I would change that to the… oh, I see.
**Josh Suereth (Google LLC)** 09:06 Like, like, I should probably, I should probably present, If you look at what we did… here, let me just share… Here's me looking at your pool requests, but… Ugh… Maybe code's gonna be easier here.
Do you appreciate looking at Russ Craigs or Yamble? What's gonna be easier to understand?
Right, so when we look here at V2, we have provenance, which basically is either, I came from a dependency.
And if it's none, I didn't come from a dependency, right?
**Jeremy Blythe** 09:52 Yep, yep.
**Josh Suereth (Google LLC)** 09:53 And anytime we reference something.
it will tell us what… whether we came from a dependency. So, like, for attribute.
We have a provenance, so that I know if I don't see the attribute locally, I know exactly what dependency to go find it in.
Because I'm like, it's actually a reference. What we did for entity ref, though, is we were stupidly lazy. We didn't really model it strictly.
So, in entity, I think what I would do is, when we have… oh, no, it's actually not entity, it's, like, in signal. Let's, let's take, like, metric.
Where we have entity refs. Entity associations. We have an entity association.
Wherever this is defined. So what I think we should do is, in here, Right?
This is using Weaver Sencomp.
Today. Straight up.
We should change and make a resolved schema entity association that includes this enum, And an optional provenance.
to tell you, like, where you expect it. But the optional provenance only has to be part of this. So ref would become string and optional provenance in Resolve schema.
**Jeremy Blythe** 11:11 Yeah.
**Josh Suereth (Google LLC)** 11:12 And then I think you have everything you need to do, like, because when we resolve, we can remember where we got the entity ref from. We can do all the resolution you're doing.
And then, when you go to look up entity associations in, like, live check, you will know if you… if the optional provenance is none, okay, cool, I should find it locally. If it's not none, I have to go look in one of my dependencies.
And I know which dependency to look at.
But… but I think the thing you're running into is… This is the problem. This here. Like, like, we, we took a huge shortcut, right here, and Resolve Schemas should probably keep the provenance.
**Jeremy Blythe** 11:59 Okay.
So one of the other… okay, I see that. One of the other things… that we were discussing in the PR and in Slack was… refinements on entities.
**Josh Suereth (Google LLC)** 12:18 Oh, and did we add entity refinements? I don't remember.
**Jeremy Blythe** 12:21 I… I… they are there in this PR.
**Josh Suereth (Google LLC)** 12:27 Okay.
**Jeremy Blythe** 12:28 But… Then comes the question of, Then comes the question of… What do we do about materializing those?
So if you… if you draw a parallel with attribute.
We… when we materialize, we, like, all of the… all of the parts of the attribute are, sort of, are then represented.
Again.
In the forge output, right?
If you do that for entity, that could be huge.
**Josh Suereth (Google LLC)** 13:02 Yeah.
Because you… yeah.
**Jeremy Blythe** 13:04 Yeah, because now you've got a whole entity that has a whole, like, list of attributes that has a whole, like, thing, and then before you know it, like.
by… By completely resolving this all out, like we're… We're duplicating…
**Josh Suereth (Google LLC)** 13:21 Well, we can't…
**Jeremy Blythe** 13:23 I don't know, that's probably…
**Josh Suereth (Google LLC)** 13:24 just… Can't we just do what we did for the other Forge stuff? Hold on, where's Forge?
Great.
Forge.
Source… 2… Yeah, I thought for, like, metric, right?
We have both metric and metric refinement.
as separate things, and then in the actual forge schema.
that's not what it is.
Is it under registry? I think it's under registry.
Yeah, in the actual… we have a spot for the registry, and a spot for refinements, and you just put entities here.
Right? In fact, we do have entity refinement here.
So what do you mean by it explodes, I guess?
**Jeremy Blythe** 14:18 I guess I'd need to look at YAML again of the output, but we… Do we not?
So confused. Do we not… When we make the forge output, we copy in all of the elements of the attribute into that output.
YAML, or JSON, or whatever.
**Josh Suereth (Google LLC)** 14:42 Yeah, but we already do that for all of these.
And it does get very large.
Yeah.
**Jeremy Blythe** 14:49 Yeah, so for… and… So, for an entity association.
Do we then restate the entire entity?
in the.
**Josh Suereth (Google LLC)** 14:59 Oh.
**Jeremy Blythe** 14:59 Entity associations for every metric.
**Josh Suereth (Google LLC)** 15:03 Yeah…
**Jeremy Blythe** 15:04 That whole entity again, with all of the things of the entity again.
**Josh Suereth (Google LLC)** 15:08 No, that… yeah, that's why we were keeping them as strings, and that… like, I assumed, even in Forge, you would do a lookup for the entity in some fashion.
**Liudmila Molkova** 15:17 Oh, never mind.
**Jeremy Blythe** 15:22 I think that was a point that… I don't know if…
**Josh Suereth (Google LLC)** 15:25 No, it was.
**Jeremy Blythe** 15:26 tacos.
**Josh Suereth (Google LLC)** 15:27 3rd.
**Liudmila Molkova** 15:27 Yeah, I'm talking… can you hear me?
**Josh Suereth (Google LLC)** 15:31 You're really quiet for me, it might be a me thing.
**Liudmila Molkova** 15:35 Is it better now?
**Jeremy Blythe** 15:36 Yes.
**Josh Suereth (Google LLC)** 15:37 Lot better.
**Arianna Vespri** 15:38 That's…
**Liudmila Molkova** 15:39 Okay. So, why wouldn't we? How would somebody rendering entity, if they want to do something about entity associations in Markdown, let's say, or if they want to, I don't know, write a query that a template, a query that does something with NGG associations, how would they look it up? It will be a lot of crazy joins, and… Why?
**Josh Suereth (Google LLC)** 16:07 if…
**Liudmila Molkova** 16:09 Materializing association would be a problem of any sort.
In 4H.
**Josh Suereth (Google LLC)** 16:15 I think, to Jeremy's point, it becomes a huge amount of duplicated code. Like, I think we would actually see noticeable slowdown in rendering.
significant slowdown. So, what I would rather do is actually find a way to optimize that lookup and make a bunch of ginger functions that do it for you.
So, you could have a Jinja function that says, if I have an entity ref, go find the entity ref in the current context.
**Liudmila Molkova** 16:45 Wouldn't life check mean the same?
**Josh Suereth (Google LLC)** 16:48 Yep.
**Jeremy Blythe** 16:50 LifeJack already does that.
It's just using the.
**Liudmila Molkova** 16:53 So… Like, like…
**Josh Suereth (Google LLC)** 16:56 We are trying to keep things as much raw JSON as possible in Jinja, because that's kind of the model, is we produce raw JSON, throw it to JSON tools, and then we have lots of flexibility. But the reality is, when we start talking about, like, an AST, it gets complicated and nested.
And when you have things that are references, and we try to flatten them all out, I think… and I personally think entities is a step too far.
We can implement it and see what happens, but, it… I… it seems like this is gonna be pretty explosive.
**Liudmila Molkova** 17:29 Okay, so as long as we could… We don't ask users to do joints in GQ.
And as long as custom policies in Regal can get the entity without the lookup, they cannot even do the lookup.
Really, without super hockey ways.
**Josh Suereth (Google LLC)** 17:51 You might have to write a helper in… Rego's a good concern if you're saying that RegO can't do the lookup.
**Liudmila Molkova** 17:58 Yeah.
So, like, for regal purposes, we would need to materialize it.
**Josh Suereth (Google LLC)** 18:06 But why can't we go do lookups? We have a bunch of lookups we do already with sets.
**Liudmila Molkova** 18:15 Because I'm not talking about the policies, I'm talking about the life check policies, when all you know about the registry is what… Life check match and return due in the definition.
**Josh Suereth (Google LLC)** 18:31 Right, but live check can do the lookup for you and pass it to you as part of the definition. So, like, LiveCheck can do the expansion and live check, and then raw rego policies, when we have access to the whole definition, I think we can do the lookup.
So I, I think.
**Liudmila Molkova** 18:47 Okay.
**Josh Suereth (Google LLC)** 18:47 We're okay. But I agree with your concern, like, we shouldn't make users figure out how to do this every time. We should provide a bunch of utility libraries for it.
**Liudmila Molkova** 18:57 Okay, sounds good.
Sorry, a small off topic, and it's not for now to solve, but in the confirmance repo, we actually… Do a fake… Pass a fake registry… not a fake registry, some projection of the registry to life check policies, and it's quite helpful to overcome… It's a lucky enough spend type. So maybe the life check should get the full registry. Why not?
Anyway, sorry.
**Jeremy Blythe** 19:38 I can't help thinking what he does.
But let me check on them.
**Josh Suereth (Google LLC)** 19:54 So, in terms of making decisions, I think my proposal here is… we have scope here, right? So, one is, issue warning… Error if entity ref.
Refers to an entity that cannot be found.
Part 2. I think we should do this, but you can tell me what you think. Uber resolved.
schema.
Entity rep.
Should keep Providence.
Part 3… We should, it's expansion helper's… finding entity in various places, so… Live check. What do I do.
Look up.
Entities, and make sure that they're… Available for Rego policies. We have a Jinja template helper to look up entity by RAF, in… Alright, schema slash dependencies… And we want a, Rigo helper.
You look up, it's due by rat and current schema.
Equities.
Is that… I don't think this actually fully solves the issue, though, right? Like… Because you're under… If all the things we just talked about, did we actually solve your underlying issue?
Oh, actually, I think it would, if we, I think it would. Okay, here's why I think it would.
Once we have the, like, Jinja helper template and live check looking up across dependencies, because we have provenance.
then I think you will be able to find dependencies from upstream… you'll be able to find entities from upstream dependencies when you need them.
**Jeremy Blythe** 22:20 Because… how will they… hmm… Right.
Because it… Because I won't…
**Josh Suereth (Google LLC)** 22:35 Yeah.
**Jeremy Blythe** 22:35 I won't need to import.
Because it will find it in the dependency.
Yes.
**Josh Suereth (Google LLC)** 22:45 scheduled.
**Jeremy Blythe** 22:46 Let's see, where does it go into the refinements?
**Josh Suereth (Google LLC)** 22:51 The entity will be available in the registry.
with its ID, and it will be available in refinements also with just the raw ID, because every signal has a refinement, which is exactly itself, yeah.
**Jeremy Blythe** 23:07 Yes, so it would be… Duh.
Okay.
**Josh Suereth (Google LLC)** 23:15 But I think we should have a principle in V2.
Going forward, every single reference that we have, ever.
in resolve schema. Needs to keep provenance, so we know if it's referring the local thing or a remote thing.
Because we're gonna keep running into this issue of, like, oh, do I embed all the crap into one repo, or do I reference it remotely? And we… like, I was trying to rip it out so it stays remote, but you have access to it locally, and you can look it all up together.
Yeah.
So, I think this is in line with that direction.
**Jeremy Blythe** 23:52 Yes.
Okay.
Alright. The other thing I fixed along the way that maybe I should break out as another PR is… imports.
Imports would silently fail if you asked it to import something with a typo.
So if you put Service X instead of service… It would,
**Josh Suereth (Google LLC)** 24:20 Yeah.
**Jeremy Blythe** 24:21 No, it won't. You just won't get what you wanted, but you won't get a warning. So I added a thing to fix that.
Please, please, I saw…
**Josh Suereth (Google LLC)** 24:30 I saw that code, and I really appreciate what you did there, I think it cleans it up a good bit, but that one should definitely be a separate PR.
**Jeremy Blythe** 24:37 I think.
**Josh Suereth (Google LLC)** 24:38 Yes.
**Jeremy Blythe** 24:39 Okay, I think what I… I think what I'll do then is I'll probably pop this one back into draft.
**Josh Suereth (Google LLC)** 24:45 Okay.
**Jeremy Blythe** 24:46 And then… pull… pull pieces out of it and do smaller POs. It just… It was one of those things where I started, like, tugging the threads.
And then it was just…
**Josh Suereth (Google LLC)** 25:00 Yeah.
**Jeremy Blythe** 25:00 Traveling.
**Josh Suereth (Google LLC)** 25:01 Well, I think… I think you… you… you caught the issue where NCREF was not well designed.
And so, now we're making it better. So that's… this is exactly kind of what we need, I think. This is another thing we want to do before… like, I think we should consider this stability blocking. Like, this here… I think until we have a… we have a resolve schema, I think we do this no matter what, regardless of whether we expand. Because Part 3, I'm ex… I'm proposing we have expansion helpers.
If we start down that path, and we're like, this sucks, and we want to expand in line, like Ludmila suggested, great. Like, let's… we can flip, and it's fine. But I… we need to figure out what's good enough, and I think we can still this is the thing we're publishing, so I want to get this change made so we can stabilize, right? Yeah. On that. Okay.
Because this would be a breaking change.
Cool.
Thanks for working on that, man.
**Jeremy Blythe** 26:05 Yeah.
Yeah.
Hey, Joran! Sorry, just before we leave.
your… The other one that you were doing, ugh, I just approved it was to do another thing to do, yeah. Are we going to get that in? Because that will unblock another thing that I've… another…
**Josh Suereth (Google LLC)** 26:27 Can I… can I merge it now?
it looks like the only thing I ran into was there's a code coverage issue.
Where, solving the code coverage issue, do you know what we have to do?
I need to add… remember how we have the idea of this schema URL is this resolution?
URL.
Yeah. And we have the overrides.
**Jeremy Blythe** 26:54 Yeah.
**Josh Suereth (Google LLC)** 26:55 I want to add that as a feature so I can use that in tests.
Because if I can start using that in tests around Weaver Resolver, I can execute all the edge cases more easily. So, what I want to do is submit it with the minimum it has now, and then add that feature next as a separate PR, because every time I tried to expand test cases, I ran into it really looks like crap. Like, I have to dramatically change the test suite, or I just add that feature and then we're good.
Basically, I added that feature to make the tests, and I didn't want to do it in the same PR.
**Jeremy Blythe** 27:33 Yep.
Makes sense to me.
**Josh Suereth (Google LLC)** 27:37 Okay, are you okay if I merge that now? I might click the button.
**Jeremy Blythe** 27:41 Let's do it.
Okay. Then I can… Then I can progress on another thing.
**Josh Suereth (Google LLC)** 27:47 Okay.
Cause that, that'll, that'll give you the other thing you need, then, for,
**Jeremy Blythe** 27:53 I'm not using.
**Josh Suereth (Google LLC)** 27:53 ref, yeah.
**Jeremy Blythe** 27:54 Yep.
**Josh Suereth (Google LLC)** 27:55 Okay, I will work on the… exposing the override rules next question.
Do you have a place in Weaver Tamil you think it fits?
like, should it be Weaver Tomo only, or should it be Weaver Tomo and command line?
**Jeremy Blythe** 28:16 That's interesting.
I think the reason… one of the reasons they remain We've autonomous that the command line is getting really… Crazy. So I… I think we need to be… more conservative about what we put in the command line. So if it's not something that's, like.
like, really regular usage stuff, I would put it in the tunnel.
**Josh Suereth (Google LLC)** 28:51 Yeah.
I think I only won at the tunnel. Okay, so I'll look into that and come back with a proposal. So I'll try to get that done for our meeting next week.
Let me add that here.
Fix number 2… That's real.
It's horrible.
to students. Okay.
Cool, because that… this should let us make some really sophisticated test cases, then, that are more legit Weaver. Like, we can actually run it through Weaver itself, kind of like the, nightly thing that, Liudmila added.
**Jeremy Blythe** 29:38 Okay.
**Josh Suereth (Google LLC)** 29:40 Awesome. With that, Arianna, you want to talk about,
**Arianna Vespri** 29:45 Yeah, I just wanted to give you, like, a quick heads up about the fact that I started… I started, finally, to, to tackle that, so the… adding the links to the… to the span definition, and in my… in my idea, I… I think I would need a couple of PRs to do this. So the first one, like.
like, adding the more obvious things, like, of course, links in the span definition, and the definitional model, the schemas, etc, etc. But then, considering all the ongoing work that you are doing on the refinements.
probably I would… I don't know, like, begin with one PR, and then on a second PR, maybe tackle the span refinements, or something like that. And One thing that I'm not super sure about Is, and this is something that is mentioned in the… is part of the issue, is about, having a link type already To begin with, and I wonder whether I could just, like, not having that, in, you know, in the first, version.
Of, of this, of this addition.
And yeah, because… Like, maybe the, the, like, something like a type link could, could come later?
like, like, I don't know, like, an attribute on the link, or something like that, and So, as a second iteration or a next iteration. But as I said, I just started today, so I will… I'm planning on opening a PR or a draft, within the end of the week or beginning next week, so I just wanted to give you a heads up that you know, that thing has been assigned to me for a couple of months already, I haven't forgotten about that, I started today. So that's the only thing.
**Josh Suereth (Google LLC)** 31:46 One thing I'll say for links is the notion of a type and things, I wouldn't start with that now, because as we found out, and as we know with, like, having span type, stick to what's actually in the proto that isn't acceptable, right? Like, span ID… Trace ID, you don't have to care about.
trace state, don't have to care about, right? That's not interesting. So the only thing interesting here is attributes that you can have conventions around, and maybe flags, but I don't remember… I think flags is actually the… yeah, this is trace context flags. So also, not interesting for you, right? So when it comes to, like, modeling semantics on top of link.
Right now, you can really limit yourself to just attributes, because that's better than nothing, and that's all that exists in OTLP.
**Arianna Vespri** 32:32 Yes.
**Josh Suereth (Google LLC)** 32:33 Yeah, so if we needed to enforce types and stuff later, we would have to have a way of encoding type into OTLP, and I'm excited to see how we deal with tracing before we push for links, right? Like, I just don't think you need to… I wouldn't… I think you're totally fine not even worrying about it right now.
**Arianna Vespri** 32:51 Exactly, exactly. I was mentioning it just because it's, like, listed in the issue, but, like, trying to… you know, think about the ramification and everything, it was like, yeah, no, yeah, exactly what you said, so…
**Josh Suereth (Google LLC)** 33:05 Yeah, we, we can, we can figure this out later. That's… that's totally fine. Yeah.
**Arianna Vespri** 33:12 Yeah, I mean, in any case, I'm gonna, I mean, as soon as I open a draft or a PR, I mean, I'm gonna, you know, in the description of the PR, I'm gonna, say all this, so I'm gonna explain My decisions, or, you know, why things are maybe not, seemingly addressed.
And why?
**Josh Suereth (Google LLC)** 33:37 Now, one thing I'll say, based on the discussion we just had.
Don't make the mistake I made on entity ref. When you refer to span.
In the definition syntax, it can be a string, but in Resolve's schema, we need to actually remember if it came from a dependency or not.
Yeah. So we'll pay closer attention to that, because I think this will be the third use case of ref. Like, we have ref for attribute, we have ref for entity, and now we'll have ref for span.
**Arianna Vespri** 34:08 Yes.
**Josh Suereth (Google LLC)** 34:09 Yeah, it probably makes sense to put… make some kind of design doc or principles doc around modeling refs in the thing that I can write to help out there, but yeah.
Yeah, multiple PRs totally make sense, you can take it incremental,
**Arianna Vespri** 34:25 Yes.
**Josh Suereth (Google LLC)** 34:26 Yeah.
**Arianna Vespri** 34:28 Thank you very much.
**Liudmila Molkova** 34:30 One thing, I think we should not edit for V1. It should be V2 only.
**Arianna Vespri** 34:35 Yes.
Yes, I think that in any case it should be compatible, because if something is not there, I think it just gets ignored, right?
For, for previous… versions, or…
**Liudmila Molkova** 34:52 Well, it's a different file format, so we will probably, at least in some cases.
I think now we will fail hard, but in the future, we will ignore unknown properties in… in a typical case, and sometimes we'll still fail. It's more like, for V1, it's okay to fail. It's different schema, different everything.
**Arianna Vespri** 35:15 Okay, so just for V2. Okay.
**Liudmila Molkova** 35:18 Yeah.
By the way, Josh, it made me think we use REF for refinement.
Should we have a provenance?
There as well, as a top-level property, or we do already.
**Josh Suereth (Google LLC)** 35:36 I think we have it… And that's a good call-out, because that's exactly the kind of mistake we might have made, that we will regret later. I'm pretty sure we have provenance on Wrath, refinement. Let me… let me check.
I'm not sharing the right tab, am I?
So, if we look in… crates…
**Liudmila Molkova** 36:04 But guys, I'm coming up front because I want them to tell me what they want in my game, but I don't know how I'm going to get in here. This place is completely closed!
**Josh Suereth (Google LLC)** 36:14 Oh, Louie, that's V1, V2.
**Liudmila Molkova** 36:17 But I can't get in here because of the car. See?
And bots, coding agents, make this mistake all the time. They are also confused.
**Josh Suereth (Google LLC)** 36:29 Yeah, I, I, I think, I don't think we have it.
**Liudmila Molkova** 36:33 Meanwhile.
**Josh Suereth (Google LLC)** 36:36 So, like, we have it for references, but not for refinements. But I didn't.
**Liudmila Molkova** 36:41 The shoe.
**Josh Suereth (Google LLC)** 36:42 Refinements actually do copy-paste everything over.
Whereas references do not.
**Liudmila Molkova** 36:49 It's like the soccer field, and I'm going to a friend of the street up in here, and now my game is printed.
**Josh Suereth (Google LLC)** 36:53 Because, like, an attribute ref literally is an index to a ref.
**Liudmila Molkova** 36:59 Oh, right.
**Josh Suereth (Google LLC)** 37:03 Yeah, and we do… I think in AttributeRef, if we look at that, that has the thing. I agree with you, we should probably have provenance at this level as well, for, like, the provenance of the thing we depended on, that we refined.
**Liudmila Molkova** 37:20 So.
**Josh Suereth (Google LLC)** 37:20 Like, we… can you open a bug about that? I'm probably gonna forget.
**Liudmila Molkova** 37:24 Yeah.
**Josh Suereth (Google LLC)** 37:28 Awesome.
Alright, did… with that… I want to do real quick… I think that's… that's it for the agenda. Real quick, I wanted to take a look at, to consider for next release.
And, I think Jeremy's on all the really urgent stuff. Ludmila, I think you had a fix as well. Is there anything else that we need to jump on for next release here?
Remove deprecation from stability. Disallow requirement level field from the identity section and entities. Strict mode for Jinda 2, don't care.
cannot load registry directory beginning with dot.
That's one… I want Lauren to take a look at this PR, I'll ping him offline. He blocked the previous one, I don't know if this one is better, so I'm gonna let him figure that out. Multi-dependency support, I think we can… I'm going to archive this, because I think we have multi-dependency support, we just need to actually fix all the bugs with it.
Okay, move SSL dependency decisions into features… That's still to consider. Live check, namespace, registered coverage, and fail on coverage below. Alright, is there anything that we feel like we need to get a handle on fixing?
**Jeremy Blythe** 38:51 There were a few… New issues… There is the issue… there's still the issue with the… Yeah, live check stopping.
But I was looking at a… Bigger refactor for that.
That's the third branch that I've got open.
Okay.
So I don't… it may not be able to go in the next release, I think I need a bit… longer. I think to really properly do it right, I need to have… and I started looking at it.
Things that run in a CLI mode.
And things that run in a server mode.
We can properly divide those things.
**Liudmila Molkova** 39:41 He doesn't seem to be smart, and actually, he just seems like a normal.
**Jeremy Blythe** 39:44 When you want to run live check in a way where you're really interacting with the API, and saying, hey, read this registry, hey, get me a report, hey, do this, hey, do that.
**Liudmila Molkova** 39:52 Okay, and this time.
**Jeremy Blythe** 39:53 I need to go through the server, Mark.
It'd be really neat.
**Liudmila Molkova** 39:57 Also, really weird, because there's a key here who has way too many lights, but this other house is normal.
**Jeremy Blythe** 40:02 But I think it's gonna take longer than the next page.
**Liudmila Molkova** 40:03 So that means all the odds are weird. But now, I want to talk to this player to see what he wants to know.
**Josh Suereth (Google LLC)** 40:11 Do you know which one that is? I can move it over.
**Jeremy Blythe** 40:15 It's the one that says bug. Bug. Registry life check output. HTTP stop.
**Josh Suereth (Google LLC)** 40:21 Alright, I'm gonna… I'm gonna add it to 2Consider for next release.
Yeah.
This is the one we put some workarounds, but it's still broken, right?
**Jeremy Blythe** 40:31 Yeah, but I honestly, Again, it's one of these things you start pulling on it, and no matter what you do.
we're, like, synchronizing these threads together, when really you don't… if we used… you… you can have the API calls you make and the receiving of OpenTelemetry just to all be tasks in Axum that then are part of the same thread, and everything is, like, properly… you know, all of this sort of thread synchronization stuff goes away, and I think it just needs to be done, like.
That, otherwise… Something else is gonna come up with something else and something else.
That's my feeling.
**Josh Suereth (Google LLC)** 41:12 Okay.
That sounds reasonable to me.
Cool. We have all these other live check reported bugs from Ludmila. Any of these we should add?
**Liudmila Molkova** 41:26 Now, they are as obvious things, not, like, real problems that we have to fix.
**Josh Suereth (Google LLC)** 41:32 Okay.
**Liudmila Molkova** 41:33 The thing you added, the downstream check, downstream check is failing. I have this unbabysited draft PR that should fix it, I already added it in the next release.
**Josh Suereth (Google LLC)** 41:45 I, I was actually… yeah, I was, I was looking at this one. The, Do you know what it did to fix it?
**Liudmila Molkova** 41:53 No, I didn't have a chance to look.
**Josh Suereth (Google LLC)** 42:00 Like, it… it… I can't actually figure out what it did here.
**Liudmila Molkova** 42:05 I… it added the raw, remember how we removed the name from the dependency recently?
**Josh Suereth (Google LLC)** 42:13 Yeah.
**Liudmila Molkova** 42:14 And it added the helper structure row dependency back.
And, it did some deserializing, but this is where I stopped looking. It… I… what I would check, if I had time, that it did it for V1 only.
And given our repo structure, it's very hard to tell from just the PR.
**Josh Suereth (Google LLC)** 42:45 Interesting.
Okay…
**Liudmila Molkova** 42:52 Probably didn't, because we share this across V1 and with you, and that's exactly the failure mode that we have.
Because we share things.
**Josh Suereth (Google LLC)** 43:07 Yeah, oh, this is… so this is… this is, the schema… the schema manifest, I gotcha.
And if we had split schema manifest to be different between V1 and V2, we would have been fine?
**Liudmila Molkova** 43:20 Yeah, we would not make this mistake, but then there will be way more duplication.
So, I think it just adds the raw structure, and it should tolerate name on the old, and should not on the new.
But how it implemented the time, I cannot tell.
**Josh Suereth (Google LLC)** 43:39 Yeah, it's kind of interesting. It… this looks like it was just a refactor.
But they also… this has me a little nervous, right?
Yeah, pessimism is a better message, right?
What? Why did it change the assert?
**Liudmila Molkova** 44:00 Maybe just move things around, it's hard to see.
**Josh Suereth (Google LLC)** 44:03 It could be. Okay. Alright, we can review it later. Thanks, everybody. I think that's it, then, for planning. So the… The one from Copilot we should review, ludmila, you have another one that I need to finish reviewing, and then Jeremy will work on yours, and I will, do my part with the, schema URL stuff.
**Jeremy Blythe** 44:33 Okay.
**Josh Suereth (Google LLC)** 44:35 Cool.
Awesome.
Thanks, everybody. I guess we'll see y'all next week.
**Arianna Vespri** 44:40 No, I won't be there next week, but thank you so much, and I will talk to you async with the PRs and everything. Thank you so much.
**Josh Suereth (Google LLC)** 44:48 Yeah, look forward to seeing you, bye-bye.
**Arianna Vespri** 44:50 Bye, bye.
**Jeremy Blythe** 44:51 Right.
