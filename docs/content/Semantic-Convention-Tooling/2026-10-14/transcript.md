SIG: Semantic Convention Tooling
Date: 2026-10-14
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:19 Hello! Hi, Josh.
**Josh Suereth (Google LLC)** 00:22 Hey.
Oh, okay, I'm working now.
Ugh.
It's dark there.
**Liudmila Molkova** 00:30 It is! I mean, it's October.
**Josh Suereth (Google LLC)** 00:34 Mmm.
I thought you guys had infinite sunshine all the time.
**Liudmila Molkova** 00:38 Oh, seriously.
Yeah.
Okay.
Okay.
**Josh Suereth (Google LLC)** 00:47 Oh, yeah, I'm a bit slow. I needed, to take care of something from my previous meeting here, so I'm gonna be a bit distracted, for the first 5 minutes. What.
We wanted to cut a release, right? I think that's probably our number one discussion.
**Liudmila Molkova** 01:03 Yes, is there a discussion, though? I can cut a release.
**Josh Suereth (Google LLC)** 01:12 I just sent the Gen. AI merge thing today after you approved the fix to Gen. AI. So we do need to do another nightly check, because I think nightly is still broken for the back ends.
**Liudmila Molkova** 01:27 Okay, so we need to merge your PR?
**Josh Suereth (Google LLC)** 01:30 No, I clicked enable auto merge, so I haven't seen if it merged yet.
**Liudmila Molkova** 01:36 Okay.
**Josh Suereth (Google LLC)** 01:37 But we need to merge the Gen AI fix, and then we can cut a release.
**Liudmila Molkova** 01:43 And I can run nightly, and make sure… manually, and make sure it works.
**Josh Suereth (Google LLC)** 01:48 Yeah.
**Liudmila Molkova** 01:50 Cool.
And then I think we should talk about the stability.
**Josh Suereth (Google LLC)** 01:59 Yes.
Yep.
**Liudmila Molkova** 02:07 So, I've… Asked our… Awesome bot to collect all the issues and PRs that could potentially be.
Something we should address before stability?
Oh, wow.
**Josh Suereth (Google LLC)** 02:28 Okay.
**Liudmila Molkova** 02:29 And not all of them. I don't think we should address all of them, but we should decide.
**Josh Suereth (Google LLC)** 02:40 Well, let's go through them one at a time. So what's the definitely in scope ones?
**Liudmila Molkova** 02:45 So this one, this one we know, it's a relaxing decompatibility, allowing unknown properties.
Yep. Turns out we have a bug, that our schema contradicts our validation.
For Timo Yarrow.
**Josh Suereth (Google LLC)** 03:05 Yep. Because. Because of the whole, like, schema derivation crap. Right. And the new type. Yeah.
**Liudmila Molkova** 03:13 Yeah, so this is what it says it should be, and this is what it actually is, so I think we should fix it.
It's trivial.
I don't know why it's… oh, it's in drought, because I didn't take a look at the copilot comments.
Hmm.
This, is also a trivial one. Or maybe it's.
I'll check if it's still relevant, but if you take an identity from V1, And you refine it in V2.
And V1 identity didn't have… doesn't have identity attributes.
Then we allow it.
**Josh Suereth (Google LLC)** 03:52 Oh my god.
Because you're allowed to do it in V1, we don't hard crash. Yep.
Okay.
**Liudmila Molkova** 04:02 Yeah.
**Josh Suereth (Google LLC)** 04:02 Is that… Yeah, we should just issue an error. I guess you have a PR for that already?
**Liudmila Molkova** 04:09 Yeah, it's just been a while, I'm not sure if it's still… How much?
Wait.
**Josh Suereth (Google LLC)** 04:20 I think it's that, yeah, 1759.
**Liudmila Molkova** 04:24 Oh, I mean, there are no conflicts, but I'll take a look how relevant it is.
It's been a while.
Okay, this… I.
**Josh Suereth (Google LLC)** 04:38 Oh, this is where we did crazy ass parsing of reason.
At one point, right?
**Liudmila Molkova** 04:44 Right.
Yeah, so we probably should fix it.
We have a bunch of things related to deprecation, because it used to be a string, and we kept allowing it, and then it gets difficult. And I think it's trivial to fix, so it should be… Nice clean up.
This is also in the… probably in scope, because it's so easy to fix. We currently do it with policies. But I think we fixed it for entity associations.
And we should probably fix it for… Renamed things.
**Josh Suereth (Google LLC)** 05:31 Yeah.
Yep.
This is where we're starting to move more and more things into Weaver check instead of policies. Yeah. Yeah.
**Liudmila Molkova** 05:40 Yeah.
**Josh Suereth (Google LLC)** 05:41 Okay.
**Liudmila Molkova** 05:43 Okay, so this is, I think,
**Josh Suereth (Google LLC)** 05:48 here.
**Liudmila Molkova** 05:49 So this one… It is… we should make a decision for sure, but we currently allow to refine refinements, and maybe it's a good idea.
But…
**Josh Suereth (Google LLC)** 06:03 you I feel like it's a good idea, but I could be wrong.
**Liudmila Molkova** 06:09 So maybe we disallow it and we can allow it later when we.
**Josh Suereth (Google LLC)** 06:15 Okay.
**Liudmila Molkova** 06:16 I think… There is an unread message from this morning from mainframes people who are questioning this, if they should do this.
Because… and they are allowed to know.
**Josh Suereth (Google LLC)** 06:31 So you want to disallow it so it's not even an option. Gotcha. Okay.
I'm fine either way, but yeah, I think that should be included as a decision we make in, for things, so… Let's just do it and include it for V2 stability, because allowing it later is not breaking.
But preventing it later is breaking.
**Liudmila Molkova** 07:16 Okay.
So, let's move this friend… Previous section… Okay, So… I… Actually, I think it should be out of scope.
Because we don't even have a design.
So instead of the prose, we would write something formal.
I'm thinking we can do this later.
**Josh Suereth (Google LLC)** 08:05 Yes.
This is like having official conditions, right?
**Liudmila Molkova** 08:17 Yeah.
The the only official condition I was that consistently comes up, like, let's say, if succeeded, it failed.
**Josh Suereth (Google LLC)** 08:27 Yeah.
**Liudmila Molkova** 08:28 For.
most of them are not even formalizable, like, if available, what does it mean? It just means it's optional, nullable, or whatever.
**Josh Suereth (Google LLC)** 08:39 Right, right. It's like, you should include this absolutely when you can, but you might be impossible in your instrumentation, yeah.
I… I agree that this is not blocking V2 stability because I don't think This would need a really solid prototype, including instrumentation, proving that it works.
And I don't see how to do that.
**Liudmila Molkova** 09:03 Yeah, yeah, and, like, there is not even… like, it would take years before it… Hope, like, we find the design that works across the board. Okay, so let's take it away from… Maybe in school… you know… Pop it out.
Okay.
Template examples.
There are strings now?
We can change them. It would be fun.
**Josh Suereth (Google LLC)** 09:54 Yeah.
**Liudmila Molkova** 10:00 I think we can live without it.
**Josh Suereth (Google LLC)** 10:04 I'm fine with that as well, yeah.
**Liudmila Molkova** 10:07 We put examples, like, we have a… We have some tables that we write in in semantic conventions and notes, and that's examples, it's not normative. We won't use it in code generation.
**Josh Suereth (Google LLC)** 10:21 Yep.
It is useful documentation, but I also think that we need to do a non-breaking change to examples at some point if we're going to do this, and there are ways that we can get around it, but I don't think we have enough I don't think this is strong enough on its own to do now, and I think that a comprehensive design will take a while, but we can do it in a non-breaking way. We'll just, like… Deciding not to break users is easy. It does make it ugly, but that's fine. You know what I mean? Yes.
**Liudmila Molkova** 10:54 Yeah, exactly.
**Josh Suereth (Google LLC)** 10:57 Okay.
We have here…
**Liudmila Molkova** 11:01 So in this front perspective.
Okay, so I think… well, it'll take a while. I think what it means is that, when we have… Hmm.
Innos.
**Josh Suereth (Google LLC)** 11:25 Oh, is this where we have some sort of compatibility?
Bullshit. And so… The schema doesn't mark it as required even though for v two, it should be required?
**Liudmila Molkova** 11:36 I think so.
Unfortunately, the comment…
**Josh Suereth (Google LLC)** 11:50 Oh, this is where this might be fixed now, though, when I did the v one v two stuff.
**Liudmila Molkova** 11:56 Okay, yeah, let's see.
**Josh Suereth (Google LLC)** 11:58 So we should reevaluate it.
Yes.
**Liudmila Molkova** 12:01 But I think if it's not fixed.
**Josh Suereth (Google LLC)** 12:03 It's not in scope. Yeah.
**Liudmila Molkova** 12:06 Yeah.
Okay, and finally… Yeah, I think we should do this one. We used to have unspecified as a special marker for the… Deprecation, where… We gave it… gave a string node.
And we no longer need it. If we need it for backward compatibility, we want.
And I think we should drop it in V2, it's trivial, it's a nice cleanup before…
**Josh Suereth (Google LLC)** 12:54 Yeah, I'm in, that sounds good.
**Liudmila Molkova** 12:58 Okay.
So, then these friends are probably in scope, let's see what's probably… out…
**Josh Suereth (Google LLC)** 13:12 Oh, the extending a new member list with ref and refinement.
I remember this one.
**Liudmila Molkova** 13:19 Now, this one… Oh, right.
I think it is out.
Because… The number of times we need it is… Small.
And… It's just, we are so far from designing it that.
**Josh Suereth (Google LLC)** 13:41 I also think we can add it in a non-breaking way. I don't think it's a… Yeah. Like, we can do this in a way that doesn't break people, so we'll figure it out.
**Liudmila Molkova** 13:50 Right.
Right.
The types. I think it's out. It's not necessary right now.
**Josh Suereth (Google LLC)** 14:11 Yeah.
**Liudmila Molkova** 14:12 And… It's… Yeah, non-breaking in the future.
**Josh Suereth (Google LLC)** 14:18 Right. It is something I absolutely want to do, but, like, we're still… it's been how many… it's been 2 years, right, since we had the idea?
I think we're at the point now… No, just one. It's only been one year, okay.
**Liudmila Molkova** 14:37 Yes, so, on this one.
I think we use them still as an escape hatch, right?
**Josh Suereth (Google LLC)** 14:45 Okay.
**Liudmila Molkova** 14:45 But I don't see us how we can remove them.
**Josh Suereth (Google LLC)** 14:52 Now one one thing, there's a discussion I'm having with the network folks, by the way.
About allowing entities to be on, other signals.
outside of resource.
**Liudmila Molkova** 15:07 Mmm.
From the data model.
**Josh Suereth (Google LLC)** 15:12 Like, I could have a metric where, in the attributes of the metric, I have an entity reference in there.
**Liudmila Molkova** 15:21 Oh, and it appears as entity or it, oh, okay.
**Josh Suereth (Google LLC)** 15:26 It would appear as an entity, yeah.
**Liudmila Molkova** 15:30 And it's not entity association.
So it's the same as entity association, no?
**Josh Suereth (Google LLC)** 15:37 No.
Entity association, and that's where we, like, that's where things get awkward, okay? Entity association is the source.
entity.
But this would be… and it might go into the types thing, this is where I have a destination, or a thing that I'm looking at. So, entity as the resource that you're talking about, that's what entity association is.
But let's say I'm doing an edge metric. Let's say I'm writing a log that is about, oh, I see IPA is talking to IPB.
And I want to actually say entity A is talking to entity B and track, like, the amount of bytes flowing between them.
You know?
Because I'm the network team, and that's what I do.
**Liudmila Molkova** 16:19 I see, so then you're putting it on the data point attributes.
**Josh Suereth (Google LLC)** 16:25 Yeah, so there's two different.
**Liudmila Molkova** 16:26 Go ahead.
**Josh Suereth (Google LLC)** 16:28 There's two different ways to model it, right? You could model a resource that is A talking to B.
You could also say, I'm modeling I'm going to track from resource A how many bytes are going to resource B. And so my resource is entity A, and the metric attributes has entity B in it.
Both work.
And I think the that's that's the thing we're discussing is how do we model that? Because for networking, it's kinda critical. Almost all the kind of edge things and that sort of stuff.
We see this in GCP, right? Have you looked at our VPC flow logs that we… Allow you to get.
They're logs that are like, you know, service A talks to service B, and here's what it's doing. It has all kinds of crazy attributes in, but they're effectively… every log is like, resource A is talking to resource B.
And that's what they are?
**Liudmila Molkova** 17:26 Yeah, yeah.
**Josh Suereth (Google LLC)** 17:27 That's, like, so critical in networking land. So I think we we don't model it well yet.
**Liudmila Molkova** 17:34 Yeah. Okay, cool.
**Josh Suereth (Google LLC)** 17:36 By the way, GCP doesn't model it well either. If you look like you, I'll put, I'll give you the GCP public docs. But yeah, if you look at what we do, we have a resource which says like, oh, you're this network interface. And then.
all of the attributes have, like, these qualifications that are, like, source and destination in them, or, you know, from and to, and that kind of crap. Yeah.
**Liudmila Molkova** 18:00 fun.
And you would like like trying to connect it to the attribute groups.
**Josh Suereth (Google LLC)** 18:11 Yeah. Oh, so so basically, what folks are doing now is they're making attribute groups, which are entities, and they're putting them on signals.
**Liudmila Molkova** 18:19 Hmm, I see.
**Josh Suereth (Google LLC)** 18:21 So I'm not saying all attribute groups are entities. I think it's only a subset.
So… but I do think we… we have confirmed that we need attribute groups as escape hatch, that it works really well.
And that they need to be available on all signals, and with LiveCheck.
This, like, where… what should LiveCheck do when encountering a signal with extra attributes and attribute groups? I think that is now answered.
with Jeremy's.
**Liudmila Molkova** 18:48 Right.
**Josh Suereth (Google LLC)** 18:49 Filter matching stuff, so I think we have that.
Will we allow attribute groups on metric signals? I think the answer to that is yes.
We are. Oh, but dynamically adding them to a metric signal, I think we don't do. We allow you to reference them, right? With ref group.
**Liudmila Molkova** 19:10 We are allowed to reference them as ref groups on anything, because they are attribute groups.
And it's the authoring magic.
Oh, so one thing… Maybe we should harden the policies around them, because we don't want Anybody to add attributes to?
stable groups.
And I probably already have the policy, I'll check.
And then it will keep the metrics safe.
**Josh Suereth (Google LLC)** 19:47 Mmm.
Okay.
**Liudmila Molkova** 20:03 On entities… are they descriptive? Oh, it's actually…
**Josh Suereth (Google LLC)** 20:08 This… so this… this gets into what I was just saying, of I would say that attribute groups are kind of a workaround for not having entities on signals.
And this is going to be TBD work. I think we attribute groups in Escape Hatch for lack of entity support in various locations, but they are both independent and Might be used in places where entities exist today.
Or where entities would exist in the future, you know what I mean?
I can write this down, by the way, like you don't have to write all this. I can go through and update some of that. But in terms of the the top two bullet points there.
I think the… those two are checked, like, we know what the answers are.
Should emit place attributes on all spans events it generates? That, I don't think we have an answer to.
So when we synthesize data, are we putting attributes on it or not? I don't know.
**Liudmila Molkova** 21:11 It generates… In meat.
Well, I mean… It's just the regular attributes from the Spanner event perspective.
We have requirement level.
**Josh Suereth (Google LLC)** 21:26 This is like, so do you remember the, you were just working on this, AWS log.
**Liudmila Molkova** 21:31 Bye-bye.
**Josh Suereth (Google LLC)** 21:33 Is a public attribute group.
So the question we have here is like, okay, if AWS Log, Attribute sort of thing.
It's a public attribute group, but it's not explicitly put on any log event.
**Liudmila Molkova** 21:49 Right.
**Josh Suereth (Google LLC)** 21:51 So when should Emit be putting those attributes onto log? Because there's not going to be a ref group.
So, we could say not on all, only when referenced, and that's fine. It does mean, though, that, like.
Some of the things we might allow is.
Okay.
would… like, that live check would allow, would not be able to be admitted. And I'm fine with that, personally.
as what we do for V2.
**Liudmila Molkova** 22:19 The life check would also need a special metro for this, right? To check it. It would ignore them.
**Josh Suereth (Google LLC)** 22:26 LiveCheck would need a matcher to check for it, yes.
**Liudmila Molkova** 22:29 Yeah.
**Josh Suereth (Google LLC)** 22:30 So like, do we need the equivalent in emit or not?
I don't think we do for… for stabilizing V2. I think we could figure that out later.
**Liudmila Molkova** 22:39 Even if we need to, it can, it's a new feature, it can be added later.
**Josh Suereth (Google LLC)** 22:44 Okay.
Sounds good.
How would out-of-the-box codegen interact with these attributes? Will we have type say? I think that's still TBD because we don't really have out-of-the-box codegen right now outside of attribute keys.
So…
**Liudmila Molkova** 23:03 Yeah.
But I I mean.
Yes.
Currently, in the current shape, it would just consider them as a regular.
Attributes when it comes to signals, if they are referenced.
Yep. And do nothing, and we can do something later by saying, okay, this group of things is an AP address in Java.
**Josh Suereth (Google LLC)** 23:31 Yep.
I think that that makes sense. And the last one is about documentation. So this would be the registries. Do we think we need a public attribute group registry or not?
**Liudmila Molkova** 23:57 Maybe.
But it can be done, right? It's not something that blocks stability.
**Josh Suereth (Google LLC)** 24:03 I don't think it blocks stability. No. This bug is an overall tracking bug for public attributes, so I think we have sub-bugs. So, at this point, given where all the answers to these stand, I would remove it as a V2 blocker.
But just leave it as a tracking thing of stuff we have to sort out for attribute groups.
Like, we're… We're making more progress on that than I would have thought, so that's good.
I didn't think I was act… like, we were actively doing anything after opening it, but we're actually solving things here, so that's good.
**Liudmila Molkova** 24:34 Yeah.
Cool.
So this is not a V2 blocker anywhere… Let's just remove this.
Okay.
**Josh Suereth (Google LLC)** 24:49 So instead of probably in scope, we should just say in scope.
**Liudmila Molkova** 24:53 Right.
I'll just remove it.
**Josh Suereth (Google LLC)** 24:58 Okay.
**Liudmila Molkova** 24:59 Okay, so this was definition.
And everything else. Now we are to the Resolve 10 materialized.
**Josh Suereth (Google LLC)** 25:09 Yes.
**Liudmila Molkova** 25:12 Okay, so this is the forward compatibility similar to this friend.
Hmm The… okay, so this one is… is a nice one. It should be easy.
And, It's not critical, but it would be nice. So imagine you have an annotation in the definition.
Later on… You want to, let's say, in a different registry, To expand the annotation.
It was more stuff.
**Josh Suereth (Google LLC)** 25:50 It should… that should already work.
**Liudmila Molkova** 25:53 It currently replaces the annotations, doesn't merge them.
**Josh Suereth (Google LLC)** 25:57 It's it should be doing a merge. Did I did I f that up? I wrote a merge algorithm at one point.
**Liudmila Molkova** 26:03 Oh.
**Josh Suereth (Google LLC)** 26:03 That would be emerging.
**Liudmila Molkova** 26:04 Okay.
**Josh Suereth (Google LLC)** 26:06 But it does key-by-key merge.
So it could be that the merge is not good enough.
Or it could be I broke it when I did the V1 V2 crap.
**Liudmila Molkova** 26:17 I think it was before you split. It was a while ago.
**Josh Suereth (Google LLC)** 26:22 Yeah, but it… check if it's fixed already, or check if it's, like, if there's awkwardness, but that… from my standpoint, that was the intention of annotations, was that you would merge when you have a ref.
Always.
If, like, you have two values, it should not be a full replacement.
But it does naive key-based merging. So if you define a key.
I… it might blow away the whole sub-object.
**Liudmila Molkova** 26:50 Okay, or maybe J does the intersection, not union.
**Josh Suereth (Google LLC)** 26:55 Yeah, it could be intersection, so we might have to look at the algorithm, but it's… the intention is it's supposed to do that. So I would keep this in scope, and let's evaluate whether it's… Doing what we want.
**Liudmila Molkova** 27:07 Yeah.
**Josh Suereth (Google LLC)** 27:08 Yeah, cool.
**Liudmila Molkova** 27:09 Okay, and then the last one… I.
I think it is unnecessary.
**Josh Suereth (Google LLC)** 27:25 What was this one?
**Liudmila Molkova** 27:26 So… Let's say we're deprecating an attribute, and it's an enum. Do we go and deprecate each individual property? And I think it's not what… We normally do in, let's say, programming languages. We don't deprecate each property of the deprecated enum.
**Josh Suereth (Google LLC)** 27:47 Yeah.
**Liudmila Molkova** 27:48 And I think the point, James makes is that If we had types, Then we would deprecate it.
Type.
And then if we use the type on an enum.
Sorry, if we use the type on an attribute with different name.
So it's very convoluted, and we don't have types.
**Josh Suereth (Google LLC)** 28:18 Yeah, this doesn't seem like a blocker for V2.
At all. And I think we can figure out what we want to do with this later.
**Liudmila Molkova** 28:28 Yeah.
**Josh Suereth (Google LLC)** 28:29 Or… Some of those, I think we can actually… there's, like, some long open bugs or, pull requests on Weaver that we can probably close to.
**Liudmila Molkova** 28:38 Let's try.
**Josh Suereth (Google LLC)** 28:42 Yeah, there's one here from 2025. Like, the namespaces, the instrumentation packages, those proposals, they're marked stale, they're not closed.
Aggregation of metrics can be defined, that's another one that I… we… we said, like, please use, annotations, you know?
**Liudmila Molkova** 29:01 Yeah.
Yeah, these are also some things that we… that are just new features.
It wouldn't change behavior, or at least in any reasonable way that we care about.
**Josh Suereth (Google LLC)** 29:15 But also when those proposals were made, we were still on V1 syntax.
So.
**Liudmila Molkova** 29:20 Yeah. Oh, I'll show you something in a sec, but let's finish on this one. So it brings us to one, two, three, four, five, six, seven, eight.
10.
Issues.
**Josh Suereth (Google LLC)** 29:33 Sweet.
**Liudmila Molkova** 29:33 Like half of them is trivial.
**Josh Suereth (Google LLC)** 29:35 Yeah, alright, let's do it. Let's do it.
**Liudmila Molkova** 29:39 Cool.
**Josh Suereth (Google LLC)** 29:41 This has been a journey, right? When did we… when did we start V2? Was… it was a year ago, right?
**Liudmila Molkova** 29:47 More, no?
**Josh Suereth (Google LLC)** 29:50 I don't remember.
**Liudmila Molkova** 29:52 So… We have a bunch of this.
**Josh Suereth (Google LLC)** 29:57 June 3rd, November 3rd, 2025, that's one year.
**Liudmila Molkova** 30:02 And it's been, like, the moment the issue was created, right? It's been a while.
**Josh Suereth (Google LLC)** 30:09 Yeah, before the… Maybe, yeah.
**Liudmila Molkova** 30:12 Yeah.
We have something unchecked. Stats verified, Mintz. Are you okay or not?
**Josh Suereth (Google LLC)** 30:17 So I don't think it like who's using stats?
Right now. And if we need to add it, we add it later. It's not a problem.
But registry stats works, it produces things, it just doesn't give you stats about how many refinements are in your registry. Cool, if someone cares, they can add it. Like, it's not… You know, like, the whole stats feature is literally, you want to add a stat, you go implement it. I have no concern approving those POs.
Yeah.
**Liudmila Molkova** 30:48 I actually think the confirmance repo is the future of stats.
And, the… the… whatever the format we decide is the best one.
**Josh Suereth (Google LLC)** 31:00 Yeah, and stats is literally just the dumbest, simplest possible, go read the result schema and add stuff up and put it in a, you know.
What might be reasonable for someone making decisions?
But performance is better. Yeah.
**Liudmila Molkova** 31:18 Did we do this, by the way?
the… Data model for values sent to Rigo policies. I think we did.
**Josh Suereth (Google LLC)** 31:27 We did, yeah. Oh, I did, yeah, and then it didn't mark it as complete. This is.
documenting what goes into the various things. I think I actually did that.
I really sent it to Rico.
**Liudmila Molkova** 31:41 Let's do this. I'll put this…
**Josh Suereth (Google LLC)** 31:43 we…
**Liudmila Molkova** 31:43 And…
**Josh Suereth (Google LLC)** 31:44 Yeah, we can add it in there as something to consider and basically ask the question, but that's just about docs.
Did you see I added the virtual directory reference docs?
**Liudmila Molkova** 31:57 Oh, yeah, nice.
**Josh Suereth (Google LLC)** 32:00 Yeah, I was impressed that we had gone this long in the Weaver projects with people doing crazy ass virtual directory things, and the docs were never written.
They were reading the Rust code to figure it out.
**Liudmila Molkova** 32:15 Before AI, I've read the… Examples, the tests that we had to find out specific syntax for GitHub.
**Josh Suereth (Google LLC)** 32:26 Yep.
**Liudmila Molkova** 32:30 I think we're done with the manifest, right?
**Josh Suereth (Google LLC)** 32:34 Yeah.
**Liudmila Molkova** 32:36 And we just discussed that this for the.
**Josh Suereth (Google LLC)** 32:40 say.
**Liudmila Molkova** 32:40 coffee, too. We are…
**Josh Suereth (Google LLC)** 32:41 We can close that, yeah.
**Liudmila Molkova** 32:45 And this is the future, and… Can I close this?
Since we have this other tracker now.
**Josh Suereth (Google LLC)** 32:54 Go ahead and close it. I think that's awesome.
Big milestone.
**Liudmila Molkova** 33:02 Yeah, and also this one.
**Josh Suereth (Google LLC)** 33:05 Yeah, you can close this and have it be superseded. That's fine.
That was my earlier attempt to get us to cut a release.
**Liudmila Molkova** 33:16 Project management with AI is so good. I mean.
**Josh Suereth (Google LLC)** 33:21 Yeah.
**Liudmila Molkova** 33:23 Yeah.
**Josh Suereth (Google LLC)** 33:24 Have you used the triage skill that I have to try to make project roadmaps in OTEL, the one that's on the proto repo?
**Liudmila Molkova** 33:30 No, not yet.
**Josh Suereth (Google LLC)** 33:31 It's pretty fun. It does… like, it actually… so mostly it's documenting where OTEL keeps its, like, projects and things that it does. But it goes through every single bug, stores them all in a giant JSON.
of Doom in your local directory, and then tries to extract themes and give you ideas for, like, oh, here's a theme you could explore for, like, the next set of things you fix. Which, for the proto repo, is important, because.
**Liudmila Molkova** 33:58 Hmm.
**Josh Suereth (Google LLC)** 33:59 You know, people have been opening bugs for 5 years, and no one was fixing them.
**Liudmila Molkova** 34:03 Yeah.
**Josh Suereth (Google LLC)** 34:04 The problem is, the latest thing that I was working on for it, I don't have enough time to finish, and it's, because it's actually tricky and hard, which is about reliability, of the… Client server in the protocol?
I… it's… it's amazing… How far we've gotten with some of the bugs that you see in there.
That's all I'll say.
**Liudmila Molkova** 34:31 Oh, the the okay, that's probably the partial.
Successes.
**Josh Suereth (Google LLC)** 34:35 Partial success is a big thing. Yeah. The actual retry spec, because people do the right thing, it doesn't matter what our spec says. But the way the spec is written is really awkward.
**Liudmila Molkova** 34:50 I have a theory that 90% of the bugs live in the retrial logic.
**Josh Suereth (Google LLC)** 34:59 I mean, and honestly.
That's probably a good place to be. It's like for Weaver, 90% of our bugs should be about error messages when we're successful.
Like, once we've hit product-market fit and all the features are down, it should be people saying, oh, I ran into this and I don't understand what the it's telling me, and we're like, okay, let's go improve error messages.
If we get there, we're winning.
**Liudmila Molkova** 35:24 Yeah, hopefully not dependency conflicts.
**Josh Suereth (Google LLC)** 35:27 Well, it'll be errors about dependency conflicts. That'll be one of the things.
**Liudmila Molkova** 35:31 Yeah.
I wanted to show you something, about the namespaces, and this is the future. Maybe it's the V2… point 99.
**Josh Suereth (Google LLC)** 35:44 the 2.99.
**Liudmila Molkova** 35:49 Okay, so this is Gen AI Semantic Conventions, fully generated.
And… and there is a monstrous weaver YAML that does it all.
If I can find it.
And it has a notion of operation.
And it definitely needs polishing.
But this is the operations, and this is effectively a spend type, which should be.
**Josh Suereth (Google LLC)** 36:21 hearing.
**Liudmila Molkova** 36:21 used consistently.
And then, like, this is now we have in the schema, we can get rid of it over time.
But then there are interesting things. What metrics do you report for this operation?
DRAMatrix, you just report every time?
**Josh Suereth (Google LLC)** 36:36 Right, because you're pulling in the duration of the operation. That's beautiful, yeah.
**Liudmila Molkova** 36:40 Right, but then there are metrics that are related to this operation that you should just generate. You, like, the auto-generated code doesn't know went to… Report these metrics, but it knows how.
And then what it does for each operation, it creates a type, a class, and it has helpers on this class and all the stuff. Like if anything needs to be cached or there is some common knowledge about it, it lives there.
And some form of this seems to be generalizable.
So this is, I think, the namespaces thing, also the events.
And essentially, this Viva YAML, I found it's the source of everything that should be in the schema.
Literally downtown.
**Josh Suereth (Google LLC)** 37:40 And… Which we might want to move to have operations that link together all the template… all the metrics and spans, and yeah.
**Liudmila Molkova** 37:47 Yeah.
**Josh Suereth (Google LLC)** 37:48 Wow. Okay.
So this gets into instrumentation 2.0.
**Liudmila Molkova** 37:54 Instrumentation 2.0, yeah.
**Josh Suereth (Google LLC)** 37:56 I told you about this, and I know this is publicly recorded, but I'll say it again. I do think that there is going to be a… we do need to have a wave 2 of how we do instrumentation in OTEL, and this is what it needs to look like.
Like, our APIs are targeted at operations.
You know what I mean? Instead of, like, here's how you write a span, here's how you write a metric, here's how you write a log. What if… what if we actually optimize to how you actually frickin' write the instrumentation? As our API.
Mhmm. Hey. I'm starting an operation. I wanna record a metric about this during the operation. You know? And everything is contextual.
And then we find a way to synthesize the OTOP on the other side. So we can highly tune and optimize our SDKs, make it real easy to write, make it easy for agents to slap all that junk in. We have conformance tests to make sure the OTOP is right so no one notices any difference.
And we can, like, hyper-optimize. You can use eBPF instead of code if you need. Doesn't matter, who cares? You know, but, like, the notion that I can take and get.
here's the set of attributes related to this operation, here's the ones that need to go on the metric. Cool, I'll extract them from context and put the data in, you know, instead of… Right now, everything is manual, and all of the hard work is on the instrumenter.
**Liudmila Molkova** 39:22 Yes.
But you know what? What I see, somebody on our team is doing it for the first time.
And they don't realize how complex it is.
Yeah.
Yeah, there are so many of these tiny details, and they try to hand-roll it.
And people like in Python community, they are doing this for HTTP, like the OTOs for HTTP, and they hand roll it. They don't realize how many small, tiny details there are and how hard to find the issues there.
Yeah.
But anyway, so let's see what we can do here.
Okay, so this is… okay, I need your approval on this, because this is why we need the release, actually.
It's… it's trivial. It, extracts some common…
**Josh Suereth (Google LLC)** 40:18 Yeah, I was halfway through reviewing this. I didn't get through it before the meeting. Sorry. I'll review this. Yeah.
Okay, so we need this for the release, and we need to issue a, a check on… all of the builds to make sure that we don't fail them, which I think we can probably do now, if you want to kick it off.
I can… actually, let me do that. I can do it here.
**Liudmila Molkova** 40:41 Okay.
**Josh Suereth (Google LLC)** 40:42 I'll, where are we? Downstream check is still failing. Let's run it against main, see what happens.
Let me also check the previous downstream check because it should only be Gen AI that's failing at this point.
Where are failures?
Come on, scroll. Yeah, so only Gen AI is broken. And I sent you the CL, so we'll… and that's for generated docs. So that should be good.
That's the LPR. Semantic Conventions Gen AI, let's see if my thing merged.
Yeah, it did. It's in…
**Liudmila Molkova** 41:31 Okay.
**Josh Suereth (Google LLC)** 41:31 So I'm running… I scheduled the… yeah, I scheduled a downstream check, so it's going to test right now.
But yeah, the only… the only thing left from last night's check was Gen AI, because I didn't get it merged in time.
But, yeah, we'll check again. I think we're good.
**Liudmila Molkova** 41:50 Awesome.
**Josh Suereth (Google LLC)** 41:55 Oh, I'm gonna merge the Rust TLS bump, too, that's a security-related patch we should add. The other thing that I found out from my own Rust projects.
The CERD… Yaml parser that we are using.
I don't remember if we moved to Zephyr yet, or whatever it's called, but… If we're still using CERT YAML, which I'll check. is now officially all of the Rust libraries are abandoned at this point.
I don't know.
**Liudmila Molkova** 42:31 the.
**Josh Suereth (Google LLC)** 42:32 Yeah, so CERT YAML itself, the guy who initially made it, it was like a wrapped C++ thing, and that he said, I don't have time to maintain this anymore, and then there was a community fork that we moved to.
And, I believe that .
the fork is now abandoned as well, but there is a different project that's not called Serdiamel, it has some fancy name, like Zephyr, or Raphir, or… it has, like, a YR in it for no reason, besides being cool.
That one is not abandoned, and I think we need to move to it. Yeah, it looks like we're still using CERT YAML.
We were using CERT YAML NG, then… but CERT YAML NG is the one that is now… I'm getting security advisories for it from my, cargo audit check.
So I think we need to move off of that. I think that that should not be breaking.
But it will change.
**Liudmila Molkova** 43:35 Yeah.
**Josh Suereth (Google LLC)** 43:36 Yeah, it will change some things. I don't know if this needs to be part of the V2 stabilization. I just think it's something we have to do.
I'm just calling that out. I found that out yesterday, that the Sir Yaml thing, that's where I saw it. Where's our dependency bot thing? I'm looking for… Dependency dashboard, does it call it out here?
Warning, renovate config warnings, warning, package lookup failures, warning, updating branch, update failure. Okay, cool.
I see. It looks like the next time we go to update the dependency is when we'll get the abandoned notice.
I don't know if you know how that works with cargo and all that, but the… oh, we already… here it is, we are using Sapphire. Okay, so we're using Sapphire, we're using Sapphire 2.0, so it's just, we need to get rid of a few of the… references to, Serd YAML. But it looks like we already pulled in Sapphire. We're probably using that everywhere we can. I found that there were a few places where Serd YAML was sneaking in my own personal project, so we'll have to take a look at that. Yeah, like, right there.
I think we define it for, like, our, XTAS cargo?
But not Weaver itself, something stupid like this.
But if you look at Sapphire, it's like S-A-P-H-Y-R. If you just search for YR, because why would you put YR in it?
Name, unless you're trying to…
**Liudmila Molkova** 45:15 Oh.
**Josh Suereth (Google LLC)** 45:17 Yeah, we are using Sapphire. That is the new YAML parser.
So, Yay.
Which also makes me think.
Weaver's a pretty good name, but across open telemetry, do we need cooler things, like… Sapphire as names? Should we just put Ys randomly and stuff? Like, Gen AI, should it be Gen with, like, a Y in the middle?
**Liudmila Molkova** 45:45 Let's not call it Gen AI.
Yeah. Wow.
Unless it's the thing that comes out of the bottle.
**Josh Suereth (Google LLC)** 45:58 All right.
Serde YAML, S-E-R-D-E.
**Liudmila Molkova** 46:09 Oh, yeah, yeah, that's what I…
**Josh Suereth (Google LLC)** 46:11 Serialization, deserialization, yeah.
Set a fire. Everywhere. We should just say everywhere, because, like, we're half… we half did it.
So yeah, in the description of that, I just say there's some… there's still some references to it. Well, I can fix that later.
**Liudmila Molkova** 46:33 Okay,
**Josh Suereth (Google LLC)** 46:36 Cool.
**Liudmila Molkova** 46:37 I want to say I didn't see this PR from Jeremy. I think we should try to include it if it's good.
**Josh Suereth (Google LLC)** 46:44 Agreed.
I think that one's probably a pretty simple fix. This one, I didn't understand when I got rid of all the CERD skips. I remember reading this. Did I comment or approve? I don't… maybe I did, maybe I didn't.
Okay.
Yeah, but basically, it just removes a whole bunch of,
**Liudmila Molkova** 47:12 Oh, because he removed the serialized.
**Josh Suereth (Google LLC)** 47:17 Oh, he's not serializing the whole live checker, he's serializing the actual values. That makes sense. Okay.
He implemented his own serialize that actually does specific things.
Which is better. Okay, cool.
**Liudmila Molkova** 47:39 Okay, so let's put it into the release.
No… Do you want to fix SARDA before we're releasing, or after?
**Josh Suereth (Google LLC)** 47:59 No. No. You can you can release today without it. Yeah. I think it's.
It's risk, but it's not like, It's not getting worse. The one that I just merged is the one that we probably wanted, which was the TLS updates.
So that one's already merged. Keeping on track of all that. Actually, do you mind going back to the Weaver?
GitHub and clicking on the security thing, security and quality.
Oh, fun.
Jeremy had been looking at this. Let's click on the Vulnerabilities tab and just take a quick look at anything critical.
Promise to assemble… Oh, this is in PNMP. If it's in PNMP, that's Weaver UI, we actually don't care. Weaver UI is not part of our… we should make a security threat model about how Weaver UI is not, you know.
important, but that… That's one I think we can ignore.
well, not ignore, but it's not actually critical for Weaver. It's only critical for Weaver UI, and we need to write a security threat model about how UI should never be exposed outside of your local machine. Oh, go back to… was there anything else in security and quality that was… that we should look at?
**Liudmila Molkova** 49:14 Well, there was something, but it wasn't critical. There was…
**Josh Suereth (Google LLC)** 49:21 I wanted to check…
**Liudmila Molkova** 49:22 So Jess.
**Josh Suereth (Google LLC)** 49:24 JS, that's also JS, that's JS, JS, JS, it's all JS. Okay, so nothing… nothing on the Rust side, which is good.
And the Rust TLS handshake, I just updated.
I just updated REST TLS to the latest version, so I think we should be good there.
Cool.
**Liudmila Molkova** 49:45 Cool, yeah.
Awesome. So we have a plan. We talked about everything.
**Josh Suereth (Google LLC)** 49:52 Yeah.
**Liudmila Molkova** 49:52 We can take 5 minutes back.
**Josh Suereth (Google LLC)** 49:55 Awesome. Have a great morning.
**Liudmila Molkova** 49:57 Thank you, you too.
See ya.
