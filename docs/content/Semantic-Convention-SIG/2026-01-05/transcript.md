SIG: Semantic Convention SIG
Date: 2026-01-05
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 02:02 Hey, is my sound working?
**Trask Stalnaker** 02:05 Yeah.
Happy New Year.
**Josh Suereth** 02:09 Happy New Year. How we all doing?
**Trask Stalnaker** 02:13 Angry.
Not sure yet.
Been on the job all of, 15 minutes here.
**Josh Suereth** 02:25 Oh, nice.
I, I tried to start about 3 hours ago.
I'm still jet-lagged from the, holidays, but I,
My laptop decided that it didn't want to have a hard drive anymore.
So, this is my, spare.
So I'm glad the audio's working.
With that, do you…
Do you mind running the meeting, Trask, or do you want me to, present?
**Trask Stalnaker** 03:03 Yeah, I can run. Yeah, yeah.
**Josh Suereth** 03:06 Thank you.
I'm still… I'm still getting the hang of this, this, other laptop here. I gotta… I had to reset everything.
**Liudmila Molkova** 03:55 Hey, everyone.
**Trask Stalnaker** 03:58 Happy New Year!
**Liudmila Molkova** 04:00 Happy New Year!
**Trask Stalnaker** 04:08 Alright, let's… Get going. Triage…
Let's see, these look… interesting. Is this blocked? Do you know, Lydmila, for general discussion, or for Gen AI-specific?
**Liudmila Molkova** 04:44 I think it's blocked by Jenny Isig,
It's still… discussion is still in progress.
**Trask Stalnaker** 04:55 Okay.
For service criticality, let's see… So… Josh… approved… .
**Josh Suereth** 05:17 I think this just had a technical issue that Yao called out.
**Trask Stalnaker** 05:21 Okay.
**Josh Suereth** 05:22 That needed to be resolved, and I don't… like, the… the content was fine, but there was a merge conflict or something that needed to get fixed, and I don't know if it did get fixed.
**Trask Stalnaker** 05:33 Okay, I'm not seeing any…
**Josh Suereth** 05:37 Yeah.
**Trask Stalnaker** 05:38 Okay. I'll just,
And I was just checking, sir, this week… Okay, we don't have… okay, the service…
SUMCOM meeting is next week.
Cool.
Guidance for RPC protocol versus framework… .
**Liudmila Molkova** 06:25 So I… I… I think that this change Adds a lot of…
Tries to define terminology for protocol and framework.
And it's very subjective, and I just don't think it helps with semantic conventions.
**Trask Stalnaker** 06:49 Yeah… okay, cool, we can.
**Liudmila Molkova** 06:52 discussing RPC.
**Trask Stalnaker** 06:55 Meeting. Yeah. That, makes sense to me.
Let's see… needs more approvals… This would probably be… Easy one… If somebody's got time…
MCP, this is from Ludmilla, has… 1… Gem AI…
**Liudmila Molkova** 07:38 to Gen AI approvals.
**Trask Stalnaker** 07:41 Oh!
Yes, indeed. Okay.
So, though, can we hit merge? Oh, it's got a requested change.
**Liudmila Molkova** 07:52 I've addressed the comments from this…
**Trask Stalnaker** 07:55 Okay, use your end.
Dismiss.
**Liudmila Molkova** 07:58 Oh, thanks.
**Trask Stalnaker** 08:03 Cause I won't think you can hear it.
No. Nope. What's it waiting for?
**Liudmila Molkova** 08:10 needs approval from, General Semantic conventions.
**Trask Stalnaker** 08:17 Oh, probably one of the files touches some general area.
**Liudmila Molkova** 08:21 Now, for every PR, the approval from a SIG counts as one approval.
And we need 2 approvals to merge.
So… it only… You can only merge if SIG approved and somebody else approved.
**Trask Stalnaker** 08:42 I'll try, I'll test that.
theory. because I… Thought that it shouldn't matter,
As long as you get two cod owner… Approvals?
**Josh Suereth** 08:59 This has a code owner's change, an issue template change, so I think that's why it's.
**Trask Stalnaker** 09:03 Yeah.
Yeah, so I… Cause he's…
**Josh Suereth** 09:07 Oh, go ahead.
**Trask Stalnaker** 09:10 these files, always… and maybe this is our problem, that chain… like, all PR… all of our PRs have one of these files, and these files are only owned
Are not owned by… code. SEMConf… Regular stem combo provers.
Does that make sense, Ludmila? Normally.
like, this file has no… none of the code owners for this file have approved the PR yet.
**Liudmila Molkova** 09:46 I… it's been a couple of weeks without meetings, but I'm pretty sure that they investigated in the past, and the approval from SIG counts as one approval.
And we still need review from the general subconf.
Because they're also co-owners.
And this kind of makes sense. We require pretty much anything to get through two approvals.
To group approvals, not to person approvals.
**Trask Stalnaker** 10:18 Yeah, I don't think that's how GitHub, approvals…
code owners works, but I will, I mean, if that's how we want…
if that's how we want it to work, I think it's fine. I think it's more that these files…
Outside. We'll… we can test the theory. I can try it.
In any case, we need a approval here.
I can… Leave that tab open and do that.
**Liudmila Molkova** 10:57 Thank you, and I have a draft of the blog coming for this, I can share it with you if it helps. There are some screenshots, and maybe it helps people review.
**Trask Stalnaker** 11:08 Nice.
These are… We can take care of these. Why are we failing?
I know what we're going to do. Oh, link checks.
We're going to rebase.
Just in case that helps.
This one… We can merge… Missing entity association…
So this looks good to merge, since you just approved it.
Yes, we've got… Seek approval…
And… last one…
Oh, we've got lots of SIG approvals.
Profile Attribute.
Josh… Do you want to…
Look at this…
**Josh Suereth** 12:49 Yeah, I can take a look and do the final approval.
**Trask Stalnaker** 12:53 Cool.
Alright.
I think that's our triage box, and… We got through some stuff… General topics.
Ludmila…
**Liudmila Molkova** 13:18 Yeah, so I'd like to bring your attention to this PR.
I tried to document how to define spans. This is the best practices from what we've done in…
databases and HTTP databases… What we're doing in RPC, and hopefully we'll do in messaging someday?
We can take a quick look, maybe?
so, I think that the key part, I'm trying to cover is…
When do you define a span?
And it's when you care about the duration, and it's interesting, really. It's, I don't know, a network call, or a group of network calls that, you're tracing.
Or, we know about one exception from this, is where we need a new trace context, because we're going to propagate it.
In messaging scenarios, and we need a unique context to trace the rule.
The other parts I'm covering in, White Strokes is… How to name spans?
How to document, Spain status,
How to… which attributes to use, how to annotate sampling relevant attributes, how to provide, the…
The requirements level.
And that we need to define a spend for each, like, individual type that we want to cover, so that we don't mix different span definitions in one, or don't break one span definition into multiple.
yeah, that's pretty much it. I think, I would appreciate review from
you trust specifically, because you're my main partner in crime defining those, and definitely from everybody else.
**Trask Stalnaker** 15:38 Nice.
Yeah, I will look at that.
Yeah, thanks for codifying, helping, codifying…
All these things that we,
decide ad hocly in the SemConv, stability groups.
Schema V2.
You wanna share?
**Liudmila Molkova** 16:15 Yeah, by the way, I'm happy to give the stage to others if they have topics. Dave, if you want to go ahead now, let's do your topic first.
**Trask Stalnaker** 16:24 Yeah.
**Dave Cadwallader (OSO)** 16:26 Yeah, thank you. So, I don't think I've met all of you yet. Hi, I'm Dave Cudwalliter, work at Oracle. We're pretty new in our
journey here, getting involved publicly in OTEL, but super excited. So, yeah, we had discussed, a while back, some prerequisites towards, getting,
some vendor-specific attributes going for Oracle Cloud to be used for public consumers of our, of our cloud platform.
And, the first attribute that we wanted to introduce under this, like, vendor-specific namespace was called the Realm, which is,
Pretty unique to Oracle, I think, but it deals with data partitioning.
And, so, I got a comment in this PR at the end here with some helpful feedback, and I kind of wanted to understand whether this was maybe some
Future-proofing that was premature, or whether this is actually a good idea?
Whether we should,
Yeah, whether we should have, like, just a flat, like, string for the realm, or whether it should be, kind of its own,
attribute an entity so that we could, I guess, maybe conceptually, I'm kind of new to this terminology, but it's sort of like whether something is just a string, or whether it's an object that itself can contain multiple properties, so we could have
Realm ID versus, like, Realm display name, or things like that.
So I, I was, I was just curious, like, is this, is this something where,
you know, I'm sort of the first one to, introduce something like this at a time when we're realizing maybe other things should have had this too, like.
should we have had this all along for things like availability zones, that you could distinguish availability zone ID versus name, or is there something unique about, Realm that maybe commands this approach, whereas, like, other similar concepts have not needed it in the past?
**Josh Suereth** 18:37 Yeah, I can jump in here. I think, if I recall correctly, Realm is similar to an availability zone, but, like, different. Yeah.
**Dave Cadwallader (OSO)** 18:46 Exactly.
**Josh Suereth** 18:47 Like, we…
We… so, from the entity SIG, we've kind of discussed availability zone and whether or not Availability Zone is an entity. We… we have a…
we have some interesting complications across, like, cloud vendors and providers. So, for example, GCP, where I work.
You can have a manager of VMs, which lives in one availability zone, and manages VMs in a different availability zone, and so if you try to say, hey, I have an availability zone that's the same across everything, it, like, doesn't work, because if I want to know about my manager, it's somewhere else.
**Dave Cadwallader (OSO)** 19:20 Right. So there's a hierarchy and a relationship set.
**Josh Suereth** 19:24 the… right… right now, that… that, like, definition of that relationship set kind of isn't set in stone. But…
I think what your initial PR is probably fine for that, even when that's the case. So, for example, we are allowing an entity to be defined by a single attribute, which is its identity. So, for example, service name.
Right? We have, a services entity where, like, the name is its…
ID. Service namespace is an entity where it's… the namespace is the identity of the namespace.
So you're kind of in line there, where you can say, like, a realm is an entity, and it is this attribute, and this attribute is the entire identity of the thing.
And, like, you don't need to do more than that, right? So, I think the suggestion might be a little bit overkill right now, like, future-proofing. If you don't expect realms to be any more than, like, you know, Enum-type strings that identify them.
you should be fine, right? Like, the key thing in defining an entity is you need a stable identity that remains stable across multiple observers.
And then you can have relationships between that thing and other things, where I can say, this is part of this realm, this is part of that realm. So…
I would stick with what you had initially of just OracleCloud.realm as a single string, and then if you needed to find an entity, you make the entity identity be the same… you make an entity called Oracle Realm and the Oracle Cloud Realm, and you make the identifying attribute be the same thing, and you're totally fine.
Like, it should be that simple, yeah.
**Dave Cadwallader (OSO)** 21:03 Perfect, that makes sense. Yeah, definitely, like, everywhere…
Yeah, on our public documentation, internally, like, realms are always just referred to by their little short ID, OC1, OC2, OC5, so that's…
that's the only way that I ever see them referred. There's no, like, longer display name kind of thing that, you know, folks need to know about, so…
**Josh Suereth** 21:26 Yeah, so I… the… for context, the way… the way I'm currently thinking about Cloud Availability Zone, and again, we haven't really discussed this in detail, because we don't really have a cloud SIG, but I'm thinking of doing the same with Availability Zone for cloud.
So, Cloud Data Availability Zone would remain as is, and there might be an entity called a Cloud Availability Zone, which the identifying attribute would be that attribute.
Where things get interesting are if you have another entity that's part of that zone.
and you need to report, like, two of these things in the same resource, like a managing entity and not, that's where things get funky, and that's what we're still sorting out. That's where probably there'll be some other attribute to denote, like, this thing is managed by something else in a different realm.
And you won't use Oracle Cloud Realm for that.
attribute. Does that make sense?
Okay.
**Dave Cadwallader (OSO)** 22:23 Yeah, absolutely. Yep.
**Trask Stalnaker** 22:30 Alright.
**Liudmila Molkova** 22:32 Dave, a quick ask for you, you… I think you've added the…
Oracle Cloud as an area, right? But I don't see,
the record and the code owners. And this is what powers automation.
Okay. This would, I'm sending…
a link to the code owner's file, and you can kind of guess how to add Oracle Cloud owners to
this one. And then the reviewers will be automatically triggered for the group.
Done.
**Dave Cadwallader (OSO)** 23:15 Great, and in that code owners, I should reference the new group that we created, the approvers group.
**Liudmila Molkova** 23:24 Yeah, so you're… you tag that group plus the spec subconf provers, so every…
Pass here has two. And you see, we have one pass for the docs, and one pass for the model.
**Dave Cadwallader (OSO)** 23:39 Okay. Should I do that for cleanliness as its own separate PR first, or should I just make it part of this existing one?
**Trask Stalnaker** 23:48 Do it as its own, because then we can rubber stamp and merge that, and we can get the reviewers, the code owner reviewers, on your current PR.
**Dave Cadwallader (OSO)** 23:57 Perfect. Sounds good.
**Liudmila Molkova** 24:00 Thank you.
**Trask Stalnaker** 24:06 Alright, over to you, Lyudmila.
**Liudmila Molkova** 24:09 Okay, so… Give me one sec, I'll open it up.
So I just wanted to share what we've been discussing and the progress we've made on the schema V2 when it concerns the specification and just the general story.
I'm sorry, I'm super dark.
This is still in the discussion. I'm really thankful for everybody who Take a look.
And I'm, I'm socializing the proposal and wanted to get any, any, kind of the feedback you folks might have.
So the goal of this is, as I see it for semantic conventions, is to be able to decentralize conventions, and let everybody publish them, and also have a clear indication of the stability
in Schema URL.
So what we published today, is…
Schema file, which is a diff.
So if you… I'm not familiar, this is… the…
thing that people see if they hit schema URL today, and this is the only thing people know about semantic conventions.
Externally, unless they're ready to go into the repo and,
dig into the, source code that we have. This is just the renames.
This is… By assuming there is one registry?
But with decentralization, it doesn't work.
So instead of seeing this, what…
I'm proposing to publish is this manifest file.
If we'll have file format, it's a major break-in change. What we have today is 110.
From the important things, It will have stability.
It will have a link to resolved schema.
Still polishing the details around this one.
But essentially, this URL.
If you are interested in the content, you would download it, you would cache it, it returns a resolved
schema.
So what is a resolved schema? So when we write conventions, we use
what I invented the term ChatGPT, thank you, source schema. If you have any ideas about the… terminology.
Happy to change.
so we…
use references, right? This is actually the source schema V2. We spread this across different files, and so on.
Result schema is a different beast.
First, it's a single file. It contains everything.
So, it has its own file format. Thanks, Josh, it makes sense.
it… has… A list of all the attributes.
And then, it's kind of… you can think about it as a minified thing. It's optimized for the distribution.
It… instead of references, it uses the indexes of the attributes in this catalog.
And you…
how you're supposed to use it, as a consumer. You use Weaver, or something similar to Weaver.
To, get the details about individual, let's say, metrics.
So you load it in memory, it's also memory efficient, because it uses these references and indexes.
But it's trivial to actually get the materialized view.
Separately from this ATEP, we are also documenting this materialized view that's used in code generation.
Anyway, so we will publish the manifest, we will publish resolved schema.
But we'll have two different… URLs.
War.
Stable on the part.
And everything?
And now… Any questions so far?
Great. Now to the tricky part.
you don't see that we publish diffs.
We don't publish GIFs for schema transformations, because someone can get them on demand. Someone can generate them with Weaver.
And… We definitely need to get
like, comments from people who contributed to Schema Processor, from the collector folks.
And see if they can, if anybody is actually using it.
And… if…
They became behind this proposal, but essentially, given the diffs and schema transformations got limited adoption, were not tested, were broken for a while, and
were not actually shipped in any distro.
We'd like to propose a breaking change here.
**Trask Stalnaker** 30:01 Do you… do you think that the diffs are… Needed… Anymore, like.
Except for backwards compatibility, is there a use for the diffs now that the schemas have the renamed 2 embedded in them?
**Liudmila Molkova** 30:25 That's a great point. So, in theory.
You can just, by looking at version, let's say, 138, Without even a diff.
See all the attributes that ever were.
And… What they were renamed to.
So for this single use case that we saw implemented so far, I don't think they even need it. But for the broader use case, I think they still would be needed.
Yeah, Josh?
**Josh Suereth** 31:01 Yeah, I'm… I'm curious…
about a few decisions that were made since I talked. What made you move to the Resolve schema with references versus the, like, big, ugly schema that has everything fleshed out?
**Liudmila Molkova** 31:14 Oh, Laurent changed my mind, so… Okay.
He explained that it's also memory efficient, and that anyone who would load it would get the optimizations in terms of memory, and it's extremely efficient, and that,
The opposite is impossible. You cannot get from the materialized view back to the optimized one.
But you can easily get from this one to the materialized one.
**Josh Suereth** 31:43 Okay.
So the second thing would be, one of the things that the telemetry schema file does today is it… it does have the diffs, but it also includes all the versions that have been released in a big ordered list.
We had talked about, at some point, allowing, like, LS, if you will, on the, directory, where the schemas are, so you can get a list of all the…
Version numbers in some fashion, or some way of, like, understanding what released versions there are.
Is that something that you were planning to, like, account for or discuss, or something you don't think we need?
**Liudmila Molkova** 32:23 We should be able to achieve it with just the… if you look at the schema URL.
We should just return it here.
Right?
part of the WhatsApp?
**Josh Suereth** 32:35 how do I… like, do I need to be able to list out all possible versions as, like, a thing that I can do?
Or, like, you know, this version, and here's all the previous ones. Like, a version history.
**Liudmila Molkova** 32:48 I think it's nice to have, but I feel it's orthogonal to this proposal.
**Josh Suereth** 32:55 Right, so there was a reason it was in the previous one, and I think maybe we should look at the… Oh, okay. Yeah. I don't remember why Tigrin wanted it off the top of my head, but I remember there was a discussion about it, so I just…
That's just a, please, please respond to that, or, like, it's not talked about at all, and it might not be needed, but if it's not needed, we should describe why it's not needed, right? If the previous one said that it needed it.
**Liudmila Molkova** 33:24 Okay, thanks.
**Trask Stalnaker** 33:26 I would guess it was… Because previously, each one only had the things renamed in that version.
And so, you really did always have to, like, if you wanted to do schema translation, you would always have to read through all of them and aggregate them anyways into your processor.
Versus now with the full schema.
I think, probably, you only need the one, because we have the renamed two, but maybe…
I mean, if we're not dropping things, that's the only…
Case where you might need intermediate.
schemas.
**Josh Suereth** 34:22 Yeah, the not dropping things is… I still… I am still a bit nervous about this surviving through major version bumps, if we do braking changes between things.
But, like, to Lyudmila's point, you would pull in the two.
We would do some kind of diff, and we need diff to be able to tell you this is a breaking change.
So you can't do a transformation between A and B.
Anyway, I still think, like, I like the spirit of what you're going for, Lyudmili, here, of we don't really know how to do transformations, so let's keep things automated to what we can do. Let's keep it simple, and let's make sure that we're publishing definitions, because they're more valuable.
And we think people will engage with them. And then let's work our way backwards into DIFs.
With what we actually need.
So, I like that as an approach, but I, yeah, when we start having breaking changes, or, like, dev versus regular.
and I diff those two, I should… I should see problems. Anyway, sorry, Christoph, you had your hand up, I keep jumping in.
**Christophe Kamphaus** 35:26 Yep, no problem.
I have two questions. In the resolved schema, if an attribute is renamed more than once, let's say two, three times.
Would that still be visible if we have the intermediary, renames?
**Liudmila Molkova** 35:44 Yeah, actually, even if you just look into the…
semantic conventions of the… of the target version, right? So, whatever version you take.
where… Keep when we rename attributes.
Let's see… an example.
And then let's take a look at the RPC.
I'm sorry, I'm in the wrong place.
**Trask Stalnaker** 36:21 Yeah, the deprecated YAML.
We'll have the renamed to something.
And then, if it was renamed again, that one.
**Christophe Kamphaus** 36:32 Some people would turn off.
**Trask Stalnaker** 36:33 have another entry in the deprecated YAML renamed again.
**Liudmila Molkova** 36:39 Yes, and we actually require this one to exist and not be deprecated.
So, when would the EF.
**Trask Stalnaker** 36:47 We deprecate this one.
**Liudmila Molkova** 36:48 one. Someone who deprecates this one would have to update This to the new.
Thing.
**Trask Stalnaker** 36:57 So there's a.
**Liudmila Molkova** 36:57 Right. Most one.
**Trask Stalnaker** 36:58 jump.
**Christophe Kamphaus** 37:03 Okay.
In the resolved schema, my other question was, why do we have the attribute catalog, and as well, then the registry attributes?
What is the difference there?
**Liudmila Molkova** 37:19 This is a great question,
I think we will polish the details, I don't think this is the final version, but this one has everything.
So, let's say you have server address attribute. There is the original definition of this attribute.
And then there are multiple refinements of this attribute. When we say, oh, okay, for the CICD, the server address is something else, not the generic description that we have. Maybe we polished some examples or notes.
And this refinement will also appear in the attribute catalog.
Right, Josh?
**Josh Suereth** 38:01 Yeah, so to make that more specific, let's say server address in HTTP SEMconv, I change the description to say HTTP server address, I would end up with two server addresses and attribute catalog. One that says server address, and one that says HTTP server address.
And the raw attributes will point to the first one, and the HTTP one would point to the second one.
**Christophe Kamphaus** 38:27 Yep, makes sense.
**Liudmila Molkova** 38:28 And here, it's only the indexes of the original definitions. They don't include refinements.
**Trask Stalnaker** 38:37 Oh, okay.
**Liudmila Molkova** 38:46 Okay.
So this is, essentially what I wanted to share. This is a draft. We will keep polishing the details, and I would appreciate any high-level feedback at this point, or any other
thoughts you have?
**Trask Stalnaker** 39:07 I have a question about the, so right now, like.
You… but you were saying that the…
A goal is to distribute the registry, distribute these, decentralize them.
Where… But currently we still have the bottleneck of the schema URL, is in semantic conventions.
Is the idea that other people would have their own schema URL, Publish their own… pieces… And somehow link…
**Josh Suereth** 39:54 Yeah. Schema URL, if you read the definition today, is supposed to just be a URL.
And so anyone can publish a schema.
And so this keeps that, right? So, like, today, there can be any web address that has a schema, it's just the only one OpenTelemetry has set up is the semantic convention one. The only one we maintain is the semantic convention one.
So, what Lyudmila has here is, we can publish
We change how we publish, and we make it really fit the Weaver tooling, and then we update Weaver to make it easy to publish these things.
And then, in OpenTelemetry, we still have to set up capabilities, like, for the collector to publish a schema.
or for collector receivers to publish their own schema. Like, I don't know what granularity we're going to want.
But the mechanism should support any granularity, because it's just a URL. So, like, the prefix… like, schema URL, the definition, in the spec today.
The first part of it is kind of uniquely defining, and the last part of the slash is the version number.
So, we can define any kind of directory structure we want in OpenTelemetry I.O. to support any number of OpenTelemetry components.
We may want to think about, like, the big OpenTelemetry semantic convention schema URL changing, but that…
we could do that later. For now, you know, like, let's walk before we run, but we can kind of keep that one for Big SemCom, and then for little things, everyone can have their own URL underneath OpenTelemetry somewhere, and we need a capability for them to publish their schema.
to OpenTelemptree.io.
**Trask Stalnaker** 41:34 So let's take the collector-receiver. They would publish a schema
A lot of the attributes that they're using are…
shared attributes from the semantic convention repo.
Would their schema embed… be a completely resolved schema that includes the resolution from the…
**Josh Suereth** 42:05 Yes.
**Trask Stalnaker** 42:06 Comm repo.
**Josh Suereth** 42:07 Yeah, so two things will be true. One is, their new schema will declare a dependency
on SemConv, at a particular version.
So their new schema can say, I depend on, like, OpenTelemetry Simcov.
Right? And then we have a mechanism where you re-export the pieces you're using. So, they could have… their resolve schema might be smaller, because it will only include the things they're using, and their resolve schema would say, I have a dependency on the OTEL thing, so this is the version that I'm getting my stuff from. So you can actually read the dependency chain.
If you need to see it, but the resolve schema should be fully usable.
**Trask Stalnaker** 42:43 Okay. Extra. Yeah. Makes sense.
And that's all gonna be fine, because…
each, we only have, on our telemetry, we only have one schema URL.
Place there, so essentially, you're gonna have to decide which one
Yeah, this makes sense to me. Cool. Yeah. Thank you.
**Liudmila Molkova** 43:07 It brings me to the,
observation, so I wasn't sure that we need to document how the decentralization and importing could look like.
I think we probably should… I probably should add, content to that section.
**Trask Stalnaker** 43:24 Just because it's, like, the… one of the key highlights of the… The whole thing.
**Liudmila Molkova** 43:31 Right, yeah, okay, thanks. Makes sense.
Cool.
**Josh Suereth** 43:43 Cool. One thing, Lyudmila, you should… you should add in here as a task.
is, we… I need to fix Weaver so it can use its own resolved schema instead of re-resolving every time. I still… we still haven't implemented that.
**Liudmila Molkova** 43:58 That's what I was thinking, I wanted to talk about it on the Wednesday call, so essentially, instead of source schema, we should take result schema everywhere as the first priority.
**Josh Suereth** 44:10 Yeah, I have that as a to-do, and I started doing research for how to make it happen, but I didn't actually implement it yet.
**Liudmila Molkova** 44:19 Okay, I will edit it here.
Okay!
Then… Anything else on this?
Well done, thank you.
**Trask Stalnaker** 44:44 Alright, and that's the end of our agenda.
So, till next time!
**Liudmila Molkova** 44:51 Welcome to 2026!
**Trask Stalnaker** 44:53 Yes.
**Christophe Kamphaus** 44:54 Happy New Year. See you next time.
**Josh Suereth** 44:56 Yeah.
