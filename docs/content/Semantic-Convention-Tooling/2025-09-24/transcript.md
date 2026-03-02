SIG: Semantic Convention Tooling
Date: 2025-09-24
Duration: 58 minutes
Zoom Recording URL: https://zoom.us/rec/share/5DQIF9TeftarRO-kAkbrjbxj3EExCoje4T4LNsLBSsnU7hCR9srnnuTsGM_bWqQt.zReq0nLPPiep7PVF
============================================================

## Zoom Recording Transcript

**Laurent Quérel** 00:13 Hi, Josh.
**Josh Suereth** 00:14 Hey, how's it going?
**Laurent Quérel** 00:19 Do you know what I mean?
**Josh Suereth** 00:20 Yeah, can you hear me?
**Laurent Quérel** 00:23 Okay, I contribute…
**Josh Suereth** 00:25 I can hear you, and it says I'm talking in the mute thing.
**Laurent Quérel** 00:28 Okay, okay, okay. Done. Thank you.
**Josh Suereth** 00:33 Alright, I'm just pulling up our notes here, and then we'll get going.
Alright.
Alright.
Man.
It's been, been quite a…
Quite a month for me so far.
**Laurent Quérel** 01:13 for September.
Super, super busy. Yeah. Two, two, entire weeks, spent in Seattle.
**Josh Suereth** 01:25 2.5, one week of vacation with my oldest daughter.
**Laurent Quérel** 01:30 And, and just after this week in Seattle, I'm going in Hawaii to see my other daughter, so…
**Josh Suereth** 01:36 It's.
**Laurent Quérel** 01:37 It's super busy between family and,
And, constraint, here at the fire.
**Josh Suereth** 01:46 Yeah.
Alright.
I, I… for me, I'm going to New York next week, so I, we're taking the family to see a musical, and then I have work in the week, but I will not be in the meetings next week, so…
**Laurent Quérel** 02:05 Anyway… Yeah. I think I will be,
Yeah, Wednesday… I'm coming back Tuesday. Yeah, I think I will be there.
**Josh Suereth** 02:17 Okay.
Let's do a little bit of triage. We don't… I have one thing to talk about, but we can get into it and see if other people join. Real quick, I think we talked about this before, and I still haven't done it yet. I want to kill this board.
And move everything into the Weaver board.
**Laurent Quérel** 02:37 Yep.
**Josh Suereth** 02:38 One of the things that we… I want to do…
Is… and we can do that now, or we can do that later.
I want to go through this improved YAML schema thing, and figure out which ones we're actually going to keep, and figure out which ones we,
we destroy.
**Laurent Quérel** 02:56 So for example.
**Josh Suereth** 02:58 Formalizing registry definition.
I think we talked about how we want to have, instead of just having random groups, we want to have a formal registry. I believe V2 does this.
the way we're defining it. There's gonna be literally an attribute registry of just all the attributes, and a metric registry of all the metrics.
So, that, you know, that's an example of, like, I think…
I don't know if I include this in the V2 one or get rid of it, but there's a lot of these. I think we can close almost all of these.
Pretty easily.
Yeah. Okay. Anyway.
And then the rest of this, like, template generation fixes,
I don't know if we move this into Weaver, or we create a new place to track these, but this is,
I don't… I don't know if we want to keep talking about that here.
Versus other things we want to do.
**Laurent Quérel** 03:56 Yeah, I definitively agree that having a single place will be much more…
It will be easier, definitively, so… I'm pretty cool for that.
**Josh Suereth** 04:05 Yep, so I… I… things that we don't know what to do, I'm gonna move over into Weaver.
Those YAML things, I might move into V2 schema here.
Interesting.
Yeah, this one, okay.
In fact, I might start doing that a little bit here, I'll just move a few things.
Okay.
So, let's see, we have to consider for next release. We still have ease of use things we need to work on. I still think there's ease of use problems, but I think the V2…
schema will actually solve a lot of ease-of-use problems, and then we need to kind of get on more of these after that. For example, discoverability of things…
Yeah. Anyway, let's look at to consider for next release. Lauren, you weren't here last week.
We did make a release, but this Make Intermediate registry directory optional.
Is this,
Is this something that you had a chance to work on, or is this something that's still, like, pending?
**Laurent Quérel** 05:23 I can work on that, if everyone is okay with the approach described there.
I can definitively work on that.
And I think that that will definitively simplify the…
The way of, using this system.
**Josh Suereth** 05:46 Yeah, we had a bug recently where somebody,
Had their templates and their model in the same directory, and then got confused when both got pulled in as templates.
That's another example of some… something we might need to clarify.
Like, how the glob matching works or something.
So This approach makes sense to me, honestly.
**Laurent Quérel** 06:11 Okay, so, yeah.
I will try to work on that next week.
**Josh Suereth** 06:20 True.
Alright.
then, I don't think… I don't think, Alexandra's here.
This we might pull into V2 work. Alright, Weaver should resolve full URL.
This is a to consider.
Did you have a proposal for how to do this, Ludmelon?
Oh, she left for coffee.
Yeah, define a base URL for each link check if it's relative, if so, pretend. I think the key here is, do we have a base URL that we can use in Weaver to expand these into full URLs?
Because I don't think we can assume the registry URL that we have as a registry definition is the same URL as what the links are relative to.
**Liudmila Molkova** 07:37 We… we can ask for it as a param. I think we take the param… Or something?
With resolving markdown, we can take another one, or it's the same one.
**Josh Suereth** 07:52 Well, that's… we do for resolving Markdown, but that's in,
That's in a different code path.
Oh, I see, but that's… that's a… you're talking about the loose param that we accept. That's a semantic invention thing.
**Liudmila Molkova** 08:12 Hmm… I see. I see.
**Josh Suereth** 08:14 This is… do you want Weaver to do this on your behalf? That would have to be a Weaver thing, not just a… like, right now, yeah, semantic conventions has a loose param you provide. That will do it. And we could… we could do that, but then you don't need Weaver to do any work. That's just a semantic convention template problem.
**Liudmila Molkova** 08:37 But… It would be better if it was something that Weaver did, or if we had some… Right.
**Josh Suereth** 08:43 Yeah. Some convention that…
**Liudmila Molkova** 08:45 For example, when we write these URLs, I don't know, we leave a placeholder.
**Josh Suereth** 08:51 I… I… I'm thinking, it would make sense in Weaver. A straw man would be, let me…
Let me pull this up. So, when we define…
Where is this? This is in… not source, it's in crates.
Weaver SimConv… Would we define the registry?
this is not the right thing, is it?
**Laurent Quérel** 09:26 You are looking for that for the Weaver file, or the…
**Josh Suereth** 09:29 the… I'm looking for… what's the definition where we say, here's, like, a registry, here's its name, is it the.
**Laurent Quérel** 09:35 Oh, that's the… okay, it's not in… in this crate, I think it's in, checking config.
**Josh Suereth** 09:44 You sure it's not the manifest one?
**Laurent Quérel** 09:47 Oh, yes, Bernice, yeah, sorry.
**Josh Suereth** 09:49 Okay, so I think it's in Manifest.
**Laurent Quérel** 09:51 Yeah.
**Josh Suereth** 09:51 So in Manifest, we have a description, we have the version URL, we have a schema-based URL for where the registry schema files will be located when you publish it.
what if we added here a documentation-based URL, and then we could use that for…
**Laurent Quérel** 10:07 Yeah, that makes sense for me.
**Josh Suereth** 10:11 So, let me add a comment.
Alright, here.
Strawman.
Add a doc-based URL.
Field to, manifest… When Weaver resolves…
YAML, and it detects a relative…
URL path that can use the doc Face.
URL for that registry.
via manifest to expand into a full URL. Okay.
**Laurent Quérel** 10:55 Perfect.
**Josh Suereth** 10:56 Alright.
Does anybody have time to work on that for a next release? Does anybody want to take that?
**Laurent Quérel** 11:06 I'm not sure to be able to do that, in addition to the other one.
**Josh Suereth** 11:10 Okay.
**Laurent Quérel** 11:11 there is a priority between the two, I can…
Walk on one or the other orbits, not two of them.
I actually think… At least not next week.
**Josh Suereth** 11:25 I can list Help Wanted or Good First Issue, too. I don't know if this is a good first issue, but it's like…
I don't think it's hard.
**Laurent Quérel** 11:33 Yeah.
**Josh Suereth** 11:33 It's just time, yeah.
Okay, we'll leave it, we'll leave it as is for now.
Oh, Jeremy and Ludmila, we're just going through, to consider for next release right now.
And trying to see what we could have. Weaver registry diff, template extension weirdness. This one we just still need to investigate, and I haven't had a chance to dive into the YAML to know where these are coming from.
Worldwide.
there's some… some kind of shenanigans between CERT and CERDYAML. It also could be that with our upgrades to CERDYAML, this is fixed, so I just wanna… I wanna try it out again.
Hmm.
**Liudmila Molkova** 12:10 I… I can try to rip her again, but I probably won't have a chance to take a look.
**Josh Suereth** 12:16 Yeah, yeah, yeah, no worries.
I do think this is related to Sergiano, personally.
But I…
we can try to repro. My hope is that if I delay long enough, Sardiano just fixes it.
**Liudmila Molkova** 12:32 It makes sense, it actually affects different semantic conventions only, so it's not… the blast radius is very small.
**Josh Suereth** 12:40 Yeah.
It's fun. Let's see… enable strict mode for Jinja 2. Did we already do this? Or is this… this is a new one?
**Liudmila Molkova** 12:52 No, we just talked about it, but we didn't do it.
**Josh Suereth** 12:55 Okay.
Junior 2 code to reflect context groups, and now able to see this context under docs. Okay.
The way I can introduce a gycope in the YAML. Oh, interesting, yeah. That's another request.
**Liudmila Molkova** 13:10 Right.
**Josh Suereth** 13:12 Yeah.
I'll just say… Funny.
For this.
Something… Nope, not exiting.
Alright.
Well, crap, we do have instrumentation scope, don't we?
We just don't use it.
**Liudmila Molkova** 13:37 Do we allow somebody to create, to define it?
**Josh Suereth** 13:40 I think… Hold on, we'll go back here.
I'm pretty sure group type… How's the instrumentation scope?
**Laurent Quérel** 13:49 I remember a group type, regarding scope.
At some point.
**Josh Suereth** 13:55 Yep.
I mean, I don't think it's used.
And we don't have any semantic conventions in OpenTelemetry around it.
Nor do we have, like, understood how we want to do CodeGen with it, so I think it's… it's…
And given the OTEP I just opened, there's some problems with it.
Yeah.
It's there.
I'll respond to this, this later, actually. Of basically, it's not called instrumentation scope, scope is instrumentation scope, but…
I think we should sort out what they want to do with instrumentation scope and understand it better.
**Liudmila Molkova** 14:41 Do you know what? We don't advertise it in the JSON schema, and we don't advertise it in the docs, so it's as good as we don't have it.
**Josh Suereth** 14:50 Yeah, yeah, yeah, fair.
I think we tested, though. At least last I checked. Anyway…
the… the key here is strict mode. I think this is actually a pretty simple…
Is this still working? Come on. Okay.
I think this is a pretty simple addition, right? Adding strict mode?
**Liudmila Molkova** 15:15 Behind feature flag.
Yes. Because… yeah.
**Josh Suereth** 15:21 Yeah, we'd, like, having a flag to registry generate, or any… anything that uses the template engine, having a template parameter that would use strict mode.
Cause I do… I do think strict mode would break everything.
**Liudmila Molkova** 15:35 It does, yeah.
Yeah, it should be pretty straightforward.
**Josh Suereth** 15:43 Okay.
We'll leave that as an open. I'm gonna change this to enhancement, it's not necessarily bug, right?
**Liudmila Molkova** 15:52 Yeah, it's not the bug.
**Josh Suereth** 15:56 Alright, cool.
If anyone wants to sign up for that, feel free, I don't think we have time. Live check reporting improvements. This one, I think…
we've… you've been discussing, and we kind of talked about before, I'm gonna leave that for the open discussion.
Alright, let's check real quick. I believe there's a… Open PR.
That should be in the next release category.
From Jeremy. So let me go fix that.
Or did it already get merged? It's already merged, never mind.
**Jeremy Blythe** 16:37 Also be my smallest PR ever.
**Josh Suereth** 16:41 Yeah, I'm just real slow. Okay, live check reporting improvements, though.
We can talk about those. Let's come back to the agenda.
Alright, attribute groups, Ludmilla.
**Liudmila Molkova** 16:55 Yeah, so for attribute groups,
There were a couple of discussions, left. One of them is,
named, sorry for my Java terminology, versus synonymous types.
for public and private group, sorry, public and internal groups. So if you scroll down a little bit…
Yeah, here, so the problem,
is that Rust really doesn't like named types… Here.
**Josh Suereth** 17:42 What do you mean?
this here?
**Liudmila Molkova** 17:46 Yeah, right. So, the moment you do this, it starts complaining about unused qualification.
It considers this qualification unused, because these types are not used anywhere except, the attribute group.
And it takes… It requires global disablement of unused qualification to let it pass.
**Laurent Quérel** 18:18 So I look also to this, issue.
And I also observed the fact that, we, we…
Without the unused qualification, we get this warning.
My analysis is slightly different.
Of the reason why we observe that. I think it's a bad interaction between
the, this, helium… initially, we had an enum with a variant that is… that was, a struct.
**Josh Suereth** 18:52 No, so real quick, this is straight up a bug. This is not… this is a bug in the JSON schema derivation macro.
**Laurent Quérel** 19:00 Yeah.
**Josh Suereth** 19:01 We've already reported this. It is not… it's nothing you did, Lymella, it's totally fine. If you remove derived JSON schema, then everything passes.
**Liudmila Molkova** 19:11 I know, but they cannot remove it.
**Josh Suereth** 19:14 I know, what I did, and yeah.
I think I listed this in the bug, is you can actually manually generate
You have the derived macro run, you look at the output of the derived macro, you remove deriving it, you copy-paste the output of the derived macro and fix the unused qualifications that the macro generates, and then everything's gravy. And I did this already for the versioning thing.
And I have, docs for how to do it. It's really stupid annoying. Real quick, let's see…
If… Let's, who… is it, author? Let's see if my bug was actually responded to. Yeah.
So, here, this is…
This is the bug. I'm having difficulty reproducing what version of Rust are you using? Oh, God. Two weeks ago.
I didn't notice, my bad.
How can he not reproduc- okay, what version of Rust are we using?
**Laurent Quérel** 20:25 I was using the last one, but,
I think that happened with previous version, anyway.
**Josh Suereth** 20:32 Yeah, I think it happened with both. Let me take a look at Weaver right now.
Is this in Cargo YAML? Where do we define our Rust version?
**Laurent Quérel** 20:41 We… let's see, I think we have.
**Josh Suereth** 21:03 I think our Dockerfile defines one, right? Right now it's… well, it was 1.88.0, was the one that I saw this on, so I'll say that.
**Laurent Quérel** 21:13 Oh, yes, REST toolchain terminal, I think we have… oh, no, it's not defined there.
I'm surprised not to see the…
Oh, in the, in the config, the terminal… Let's see… No?
**Josh Suereth** 21:34 I've just looked at what my local West was, yeah.
**Liudmila Molkova** 21:38 I have 189.
**Josh Suereth** 21:41 You have 189.
**Liudmila Molkova** 21:43 Oh, it's the mushroom Perfect.
**Josh Suereth** 21:46 Yeah.
**Laurent Quérel** 21:50 Yeah, the reservation, the minimal reservation used for this project is 121.
It's defined into the main cargo terminal shine.
**Josh Suereth** 22:01 It's its minimum standard Rust version, right?
Is, what, 121, you said?
**Laurent Quérel** 22:07 1, 81.
**Josh Suereth** 22:09 I'm 81.
Okay, cool. Yeah, if you want to see how to fix this little millet, please don't hate me.
**Liudmila Molkova** 22:36 How can you show me?
**Josh Suereth** 22:38 Yeah, I'll show you. It's,
So, in Weaver SemConv, in V2, not in V2, it's near V2, where was that? SemConv?
Oh, come on.
Come on, GitHub, just open it. Alright. We have right here, note.
**Liudmila Molkova** 23:01 Mmm…
**Josh Suereth** 23:04 So, what you do is you run Cargo Expand.
with the annotation defined. And that will work, that will not fail from linter checks.
**Liudmila Molkova** 23:13 Okay.
**Josh Suereth** 23:14 And then you copy-paste the big, ugly…
monstrosity that it auto-generated for you, which is all, you know, silly code to do the thing. And inside of here, you will find unnecessary qualifications.
**Liudmila Molkova** 23:29 Okay.
**Josh Suereth** 23:30 And so then one… then, you know, you remove the derived schemas, you leave this automatic derivation of it here, and you fix the code here with the linter check, and then everything's gravy. Until we can fix their macro.
**Liudmila Molkova** 23:45 Okay, sounds fun.
**Josh Suereth** 23:46 I might… that you might motivate me to literally go issue them a patch to fix it, because it's, I don't know if you're familiar… if you want it… if you want the term.
Rust macros are non-hygienic.
Is the term.
And since there's no hygiene for macros, this is a common problem with unhygienic macros. Hygiene is about whether or not the symbols and terms that you use are kind of independent, or they bleed into the underlying code.
So, there is no hygiene, therefore, linting gets exciting. And this is a common problem.
Anyway, good times.
Yeah, look at this, look at this wonderful code we don't have to write by hand, though. Isn't that fun?
**Liudmila Molkova** 24:35 It's awesome.
**Josh Suereth** 24:38 We can't leave an ever side.
If only what?
**Liudmila Molkova** 24:42 If only we've never seen it.
**Josh Suereth** 24:45 Yeah, yeah, yeah. If you don't see it, it doesn't exist.
Cool. So that's, that's what you ran into. That is…
unfortunate. I didn't think that you would run into it for this, but I guess any kind of thing like that is having problems, huh? Alright.
Cool.
Do you need anything else for attribute groups, though? I think that's the last breaking change, right? Or no, the other discussion?
**Liudmila Molkova** 25:12 The… I forgot what was the other discussion, let's see. So the discussion with Lorent is the same one?
There was a second comment now.
**Josh Suereth** 25:23 You made a comment about whether we have a specific type… oh, is that… is that about these specific types? Gotcha. I thought you were talking about whether or not we should have a name for attribute group and a name for private attribute group separately in the model. You just meant in Rust.
**Liudmila Molkova** 25:39 Yeah, I mean, I think there was another discussion.
**Josh Suereth** 25:46 I'm looking for it, yeah.
We don't want to interrupt lineage here, descriptive usage.
**Liudmila Molkova** 25:55 Oh, right, the lineage.
**Josh Suereth** 25:57 Yeah.
**Liudmila Molkova** 25:58 Maybe we should talk about lineage a little bit.
So, we don't have a lineage problem.
Because… Where… Still generate registry groups as public.
Yep, for now.
**Josh Suereth** 26:15 We, we will when my PR hits.
**Liudmila Molkova** 26:20 Right, so the moment with the resolved schema, and we have actually…
**Josh Suereth** 26:25 You do have a lineage problem, because you're erasing the group.
the internal groups.
You're actually removing them before you release the groups.
**Liudmila Molkova** 26:38 Yes, but I don't do anything that previous version didn't do. We also erased them previously.
**Josh Suereth** 26:46 So… didn't, I don't think?
We didn't have an internal before.
**Liudmila Molkova** 26:55 we erased all intermediate groups. So, if you look into the resolved schema, you would see on the registry groups there.
**Josh Suereth** 27:05 I don't… Think that's the case?
You mean Weaver did this, or Symante Conventions did?
**Liudmila Molkova** 27:15 we already did the semantic conventions, if you just run Weaver, Resolve, you would…
Not see any intermediate groups there, because this code Updates groups to the…
the source group on attributes to the registry. And it never produces source groups for Non-attributes.
**Josh Suereth** 27:41 So… That… you might be talking about the semconf helper JQ functions do that.
**Liudmila Molkova** 27:51 They do… don't do anything worse.
lineage, but I'm also not running those, I'm just running the result.
**Josh Suereth** 27:58 You know, what I'm saying is, in… all of the groups are included in Resolve Registry until you hit JQ, and JQ is what removes just the registry groups.
But in Weaver, those other groups are still available and accessible. I think, again, we're talking nuances, and this is new stuff. I'm looking for the thing I wanted that led me to have concerns.
Is it the Weaver Resolver?
And then not data, I think it's this one here.
Yeah, you have, underserved… where's the clear that you did?
We include, we resolve inheritance, we add the unresolved groups, and then… I think it was…
And result group to index… Yeah, the, the, the…
**Liudmila Molkova** 28:59 Sorry?
**Josh Suereth** 29:00 There was somewhere where you were moving the private groups completely.
**Liudmila Molkova** 29:05 Yes, there is a line somewhere, but this code where the discussion is, this code actually always
Resolves the final source group.
It never… result… it never results in lineage having intermediary group.
**Josh Suereth** 29:23 Oh, okay, so you're saying that the… you've already cleared the intermediate ones, and I just didn't notice that? That's my bad.
**Liudmila Molkova** 29:31 It's always been there. It's already… it already works like this.
**Josh Suereth** 29:37 Okay.
So, if you extend a group, the extended group has disappeared. Like, that ID doesn't exist. What I was trying to understand is, this parent group ID, will this ever be a private attribute group?
**Liudmila Molkova** 29:52 No, this code is fairly complicated, and I hope we can improve it. I think it can be simplified, even though it's present there.
It will later be… Erased by something else.
**Josh Suereth** 30:10 Oh, you mean attribute lineage will eventually release it, erase it?
**Liudmila Molkova** 30:13 Yes.
**Josh Suereth** 30:15 Okay.
**Liudmila Molkova** 30:15 I mean, this piece of…
**Josh Suereth** 30:17 That's… I agree with that. That's what I was just calling out. I…
This wasn't meant to be a blocking comment, this was just meant to be, we need to talk about how we want to do lineage going forward, and I think we're purposefully breaking it temporarily.
as we move towards V2.
So, I just want us to, like.
Right now, Attribute Lineage has this assumption that it's group, group, group, group, group, group, group, all the way down, right?
in V2, since it's not fully group-based, and group isn't, like, the thing, we actually have to have some reference as the lineage that is not just group, so we probably need an attribute lineage V2.
And what I want us to avoid, like, the reason I wanted this discussion.
was, I think we have to revamp lineage, and so…
preserving naive group-based lineage in the V1 resolver, and then re-interpreting lineage on the other side, I think is going to be…
Something we need to do.
And we have to have a bunch of discussions about that, yeah. That was what my point was. It wasn't meant to be…
I did want to make sure that you had lineage where we can
You know, fix it after the fact, and get rid of things, and make sure we understood what happened.
but, yeah, I agree with you, like, we don't need…
We don't need it to be 100% accurate.
Right now, and I think we need to be willing to allow some breakages to lineage when you engage with V2.
Especially since V2 is an opt-in.
**Liudmila Molkova** 31:55 Right, alright.
**Laurent Quérel** 31:56 I think we just need to be careful about the… Removing the entire lineage infrastructure.
Even as an intermediary step, could break some template generation.
**Liudmila Molkova** 32:09 We are not removing anything.
**Laurent Quérel** 32:11 Okay.
**Josh Suereth** 32:12 Yeah, lineage will remain.
**Laurent Quérel** 32:14 I was thinking that Josh was saying, okay, maybe temporarily we can remove it.
But.
**Josh Suereth** 32:18 No, no, no, what I mean is, temporarily, there might be inaccuracies in it.
For V2.
**Laurent Quérel** 32:24 Until we have fixed it for V2 on the other side.
Look at that.
**Josh Suereth** 32:29 I can… I can show you guys what I'm working on with V2 resolution in, like, an example, where, we'll have to rethink some lineage things, and what I'm thinking for V2
V2 Part 2, which is, like, taking existing groups and extracting out the V2 schema from it.
But, yeah, okay. I think, Ludmela, once… once you manually generate that macro, I think that's good to go.
**Liudmila Molkova** 32:57 Okay.
**Josh Suereth** 32:58 Yeah, and apologies, you just hit, probably, level 12 in Rust.
Knowledge and expertise now.
I don't know. I don't know what the level scale is, but I just… something high.
**Liudmila Molkova** 33:11 Okay, yeah, that's fun.
**Josh Suereth** 33:14 Cool.
Let's see, what else do we have on the agenda?
Live check report, let's have that discussion.
**Liudmila Molkova** 33:24 Yeah, this is a quick update from the last week, so we had some back and forth with Jeremy on this. So I've updated,
the PR… to do the following. Josh, would you mind, Opening…
a device file, let me see if I can find it.
**Josh Suereth** 33:53 AdviceRS?
**Liudmila Molkova** 34:00 No, violation arrest next to it.
**Josh Suereth** 34:04 This one here.
**Liudmila Molkova** 34:07 Yeah, so, can you show the advice trucked?
**Josh Suereth** 34:14 There's an advice truck in here, you mean?
**Liudmila Molkova** 34:16 line 91. Yeah.
Okay. Here it is. So, I'm proposing the, the structure,
defined in this comment, the convention for the advice.
R… So…
The point is, advice should be… it should be possible to use it as a self-contained thing. You should be able to have structured representation of it if you want to use it in JQ filter, for example.
The message, though, would contain the unstructured portion, the human-readable message.
So… For example, it will contain the full information, this attribute for Boris, deprecated, blah blah blah.
Then you can put structured portion in the value.
It supports structured data, it would have, let's say, attribute name there.
Or some additional information.
the advice has signal type and signal name, so because you… it's… it's difficult to understand, let's say if you're just looking at the advice,
It's hard to understand if you had some attribute problem, which signal it applied to. So, essentially, it's important to know this is the identification of what this signal… this advice is about.
So this is what I'm proposing. It changes how the report looks slightly.
But… It allows us to consume advices without the full report.
So, Jeremy, I'm not sure how comfortable you are with this still.
**Jeremy Blythe** 36:22 Sounds like you're…
I haven't looked at the code yet, but I've looked at the… your example output, and so I agree that the example output
Is definitely more readable.
I'm still not sure why we need value, if we… If we're in… We're embedding the…
Like, the useful pieces of information into the message.
I'm not sure what value there is in value anymore.
**Liudmila Molkova** 36:57 We don't need to add value, but it… I was thinking it, it was useful to add attribute name there for the JQ filters.
But it's… it's… Some future possibilities.
**Jeremy Blythe** 37:11 Custom report.
**Liudmila Molkova** 37:11 chicken.
**Jeremy Blythe** 37:12 My only concern with this is that we're changing, like…
We're making the… we're repeating lots of bits of the structure
Are we only doing that to make the JQ easier? Like, is it just that JQ's, like, not the right tool or something? I…
**Liudmila Molkova** 37:31 Imagine, like this Martin scenario where you report it as a telemetry item. Would you want a group by attribute name? Maybe?
**Josh Suereth** 37:45 I think the thing here that I see is value… this is actually…
Can I fully construct a message?
From everything else in this string.
**Liudmila Molkova** 37:56 Nope. The answer should be yes.
**Josh Suereth** 37:59 Nope.
If the answer's no, I kind of want to understand that, because, like, from what I…
What I understand you're doing here, Ludmila, is this, combined with the other things in this advice.
Are so that you can do custom rendering.
Of, like, what's going on and what should happen, and that sort of thing. So, my question would be, if this… I think it's fine to pass this along as a default human-readable message to the templating engine.
Right? Of, like, make sure the template engine has access to that if they want to use, like, a default message. But if they want to re-render, or do anything magical, or put things in tables, right?
Theoretically, all the information of advice type, value, advice level, signal type, and signal name should be able to synthesize the exact same human readable message, as if a template was used.
And if that's not the case, why is that?
**Liudmila Molkova** 39:00 I mean, we can do… we can do the log message, we can have the…
Template of the message here, and we can let people, put… fill the template as they see fit, but it's a lot of work, and…
This is not my goal.
**Josh Suereth** 39:18 No, no, no, no, that's fine. What I mean is, for a given advice, right, like, is deprecating.
Can I have, like, a single template that can read the value, the signal type, and signal name, and generate a human-readable message that makes sense? Or am I doing, like, weird… other custom logic in Advice?
This goes into, if I'm defining RegO policies, right, and I want to have an error message from Rigo policies.
am I actually putting the string advice in the Rigo policy for how things will render, or am I just saying, here's a bunch of data?
Go, and here… and over here is a template that can render that data into a human-readable message.
**Liudmila Molkova** 40:03 So, I would love for it to be that there is a,
There is a bunch of data, and it's possible to render it however you want, but it's… it's… it's a complicated problem.
And I'm not trying to solve it, I'm trying to, I think this is good enough that we have, human-readable message that you can,
give, and maybe eventually we can… we can do better than this. I also don't want to force everybody who uses this to have a custom template per advice type, right? It should be the same template for everything, which makes things really complicated.
So, if,
The… if it's okay to have the full human-readable message, but the concern is, let's remove the value.
Let's, let's remove the value.
it's not something we would probably aggregate a lot on. The rest is more important.
**Josh Suereth** 41:11 I… I'm not… I'm… my… my preference would be to keep the value.
And I'm not saying that we have to make it so everyone requires a template. What I'm saying is, we provide this as the default for the default rendering, so you do the least amount of work possible.
But we should encourage this to have enough context that I could synthesize this with a custom template in all cases. That way, if somebody needs to customize, if somebody wants to do special reporting, they have access to the data they need, and we don't have to continually muck with our engine.
**Liudmila Molkova** 41:44 Okay, cool. So then, I'll update this PR to include every dynamic component I put into the message when I format them.
**Josh Suereth** 41:53 if we need it from the hard-coded things, yes. When it comes to, like, Rego-based policies, I assume that we can fill this out from Rego?
and then we're fine, right? So when Rego will say, add a human-readable message, which is the default rendering, you can throw a bunch of stuff in value, and then you can do special stuff if you need, and now we don't have to keep changing our engine.
Anytime someone wants customization.
**Jeremy Blythe** 42:19 So, to… to be fair, you're saying…
that the… that the JSON blob that's in value should contain… All of the…
Fields and their values, like, like we've got here, attribute name, foobar.
That you would need to construct the message.
So if there's a clash with a namespace, you would have something in the value that said namespace, and then the thing it's clashing with.
**Josh Suereth** 42:51 Yep. And if you had two fields, like you've got in your example, FUBO and Fu Baz.
**Jeremy Blythe** 42:56 You'd have those two things called out.
Because they are very… they're, like, variables that you're then injecting into that message.
Yeah, that was con…
I never did it, but I had in mind, like, that the message would be like a format string with curly brackets that would then pull from the value.
And put into the message, rather than…
coding that in separately. See what I mean? So that somehow, when it was producing the output.
It would… it would use… it would do a format and pull from the value into the text string.
I don't know that we necessarily need to do that, but…
**Liudmila Molkova** 43:34 We can still do this in the future, right, so it's useful to format the full message anyway, but the original
Unformatted string can also be part of the structure once we Know how to do this.
**Jeremy Blythe** 43:51 Yeah.
Because what I ended up doing was just, like.
I'm just, like, dumping out the value, and then putting a dash, and then dumping out a message that doesn't have anything embedded in it, and…
You know, it was cheap.
So the outcome of what you're doing is better, but,
The other thing that… I guess my only other thing is…
In this example, you've got value that has attribute name.
**Liudmila Molkova** 44:18 Huh.
**Jeremy Blythe** 44:19 We should know… we should know that this advice relates to an attribute without having to re-enter the attribute into the value, like, because that's part of the…
That's part of the… If you look at the JSON output, the advice belongs to an attribute.
And that's what…
**Liudmila Molkova** 44:37 If… yeah.
**Jeremy Blythe** 44:39 That's what makes me feel this is a bit…
It's a bit like we're kind of repeating things.
**Liudmila Molkova** 44:45 But it's okay.
I feel strongly that advisors should be independent of the structure they are reported in, because it's very hard to know
Or, like, if you want to support Martin's scenario and report it as a telemetry, or if you want adjust the list of violations, you need to know what it belonged to.
**Jeremy Blythe** 45:16 Yeah, I guess we're making two different ways to find out which attribute it belongs to. Like, today it's possible, because you can just look up in the JSON and go, like, oh, this is for that attribute, now I've got my answer.
And what we're doing here is we're making it so that there's another way
So I don't have to look up to the parent and go, oh, my parent is this attribute and that's its name.
I can just go…
I've got this useful piece of information in this value tag.
I guess that's okay, it's just a thing, I don't know.
Do not repeat yourself, or something.
**Josh Suereth** 45:57 So, dry… this comes to, like, database normalization and denormalization?
I've given up on normalization when it comes to observability data for different reasons, but it's about, like.
where you have global views, denormalization and dry makes sense, but where you have localized views, denormalization makes sense. And I think what Lumila found, and what I think is true for rendering and templates, we have a lot of localized views of advice that we want to leverage.
**Jeremy Blythe** 46:27 Yeah. And so, denormalizing actually hurts localized views.
**Josh Suereth** 46:32 So, it's kind of a matter of, like, what's more important to us. If we want to say, you know what, you can only engage with us globally at a report level, all of our templates should only be at a report level. Everything we do should only be at a report level.
So that you have that global view. And then denormalizing and dry is fine. And that can actually minimize the output format that we have, and like, if we are worried about the amount of memory this stuff takes up, that's fine.
I don't think we're in that with LiveCheck right now. Maybe we get to that at some point, but it's not like profiling where we have to keep it as small as possible and jam everything into little tiny, you know.
sorry, it's still big, but a little payload. This is kind of more integration testing, this is, like, details are more important, localized contextual understanding is more important. So I feel like this is one of those areas where it's not dry.
On purpose, because we have… we want localized and, like, access to things without the full set of context.
Right?
**Jeremy Blythe** 47:30 Yep.
Let's said we should always know when we're in one or the other of those scenarios.
**Liudmila Molkova** 47:45 Cool. So then I'll follow up on the value, and see you all online.
**Jeremy Blythe** 47:54 So we'll keep all of this, we'll keep value, but we'll actually plug
More and more things into value.
to provide.
Is the rule that value… that we should only pull from value?
To make message.
Or do we just, like…
**Liudmila Molkova** 48:10 All the dinosa.
**Jeremy Blythe** 48:11 value in…
**Laurent Quérel** 48:14 I checked the card right now, and it looks like the… If I'm not mistaken.
Everything is already in value.
So we should be able to.
**Liudmila Molkova** 48:28 It's not.
**Laurent Quérel** 48:29 Oh, okay. I didn't find any example of it, but, okay.
**Liudmila Molkova** 48:34 So, I think every, think about it as a structured log. The message is the text, when you write it, you write only the, the…
thing with curly brackets, right? All dynamic components go into,
parameters. And value is essentially these parameters, but contextualized.
The message, contain, is, is the res… the result The resulting formatted string.
**Laurent Quérel** 49:06 Yeah, I know. But I look at all the formatted string, and what I discovered was…
all of them, I think, maybe I'm wrong.
are other things that you can find into the advice type?
So basically, it's a formatted string,
creating a human version of this advice type, or it's something coming from the value, but maybe there are some examples that I didn't see.
**Liudmila Molkova** 49:32 So what we do today, we don't, have formatted message. It's the string constant, usually.
I'm changing…
**Laurent Quérel** 49:42 Except in few places.
**Liudmila Molkova** 49:44 Okay, so I'm changing this, and now essentially every advice message becomes a full human-readable explanation.
**Laurent Quérel** 49:53 Okay, in this case.
**Liudmila Molkova** 49:54 event wrong.
**Laurent Quérel** 49:56 Okay.
Because I look at the existing code in the main branch, so I didn't see that. Okay.
**Josh Suereth** 50:02 Okay.
Alright, so I think we have a path forward,
I think that makes sense. We only have 7 minutes. I do want to talk a little bit about refinements, if that's alright?
**Liudmila Molkova** 50:13 Yeah, thank you.
**Josh Suereth** 50:15 Okay. Cool.
So, I'm working on… Oh my gosh, why are you… come on, keyboard. There we go.
I'm working on, Schema V2.
And I'm working on actually generating, a V2 catalog.
I'm gonna actually copy-paste some of the YAML from the V2 catalog.
This is an example, of the database client.
of what it looks like, and I want to run this by,
Lawrence, maybe that's better. Why does that look so bad?
How about that?
Cool. So, what… what we have right now with this is in the… in the resolved registry,
We get a list of all active spans.
So, there's a span, that is called DB that has type client, the name is empty, and it has a set of attributes where
Now, in the new schema, required is not something that is on, like, the attribute registry.
It's not something you define when you define an attribute, it's something you define when you define a signal.
And so, this I wanted to run by Laurent, of actually
attribute refs now are… and I need to change this name, that's just what refs picked, because I didn't give it a good name. But this is the ID in the attribute, or the index.
In the attribute array.
And then we have additional information specific to the signal. So if sampling required was actually true, you would also see sampling required true here in addition to requirement level, right?
So, attribute references are now a index to the attribute that you are referencing, and then a set of requirements. The other thing that this caused was it actually compresses our attribute registry significantly.
Because there's far less, you know, there's more item potence and more reuse now in attributes, because requirement level is something different.
Where description and stuff change, we will still have duplicates, but it's… it's, like, slightly different.
Okay, so that's one thing. Now, where things get interesting is, and I put this in chat.
We have, let's just… I'm just gonna make this up, because I don't remember specifics, but we have, like, db.client, we have db.mysql.client, okay?
These are both spans.
one of them extends from db.client.
And what DB MySQL Client does is it has the specifics about MySQL.
what I'm thinking of is kind of two things are true here. So, let's, hold on, let me get back to…
Bam, bam, okay.
So, principles.
spin… Definition is… Live check users…
And is the thing available in O2P.
Spin… refinements… What?
CodeGen users, and, can provide… Optimal generation.
Specifically, library. Okay, so these, these two things are basically…
When I define a span, like DBClient, this is the overall convention for database client spans that's shared across a bunch of implementations. This is what Live Check will enforce, this is the thing that shows up in OTLP. When we add a span.type to OTLP, it's gonna be dbclient. It's not going to be dbMySQL client, it's gonna be dbclient.
live check will enforce that it matches the database semantic conventions and everything's gravy. When I define a refinement, what I'm actually doing is saying, okay, for MySQL,
I don't need to say that this enum has every single possible database in it, I only need the MySQL-based things.
And if I were to, like, document MySQL specifically, it should not ever conflict with what the database client span is. It's just literally a refinement, a specialization, if you will, for MySQL.
However, when I do code generation, I'm gonna interact with refinements, because… That's…
what I am doing, you know, I'm implementing for a specific instance, I'm implementing for MySQL. So I want refinements generated.
when I do documentation, I might actually have a special thing for refinements of spend. So I could say, like, here's database client, here's what it looks like, and here are the set of refinements, here's what it looks like in MySQL, here's what it looks like in MySQL Server, you know, that kind of thing.
So, I actually think span refinement becomes a top-level thing. The last is that every span…
Definition has an implicit span refinement of itself, with no refinement.
This is… this is the contentious part. So, this is where…
if I say, in CodeGen, give me all span refinements.
I would generate a refinement for MySQL,
And I would generate a refinement for just the raw database spend.
Because… I actually need access to that thing somehow.
And if I want to filter what goes into CodeGen from refinements, I can filter out ones that have no refinement. I can filter out just the MySQL ones, that kind of stuff.
But these are the 3 principles I'm thinking about.
for defining schema V2. And I can show you what that means in practice. This is just actually what my code generates today, but I needed to work on it a little bit for this. Wanted to run that by folks. We're out of time, sadly. Initial thoughts in, like, one minute.
**Liudmila Molkova** 56:52 That makes sense.
**Laurent Quérel** 56:53 Yes, me too.
**Josh Suereth** 56:55 Go ahead, Lauren.
**Laurent Quérel** 56:56 So, regarding the first part, where you have an enumeration of attributes with their index and,
the additional, override, override?
Yeah, I understand the rationale. That was not initially the… my initial intent was to have a fully reserved, registry.
It's like an intermediary level, but I think it's.
**Josh Suereth** 57:21 Excellent.
**Laurent Quérel** 57:22 table for the reason that you mentioned. First, it's smaller.
And second, it's… the rule to apply to achieve… to get the fully reserved are very basic and simple, so that's okay.
**Josh Suereth** 57:35 The other… the other thing that makes me comfortable, if this helps, Laurent,
This required is only applicable in the context of the span.
So I actually have a full attribute registry now, that is a registry of attributes, and required only applies to the code gen for that span. It might be recommended in the metric.
So, like, having a registry where recommended required's in it just means I duplicate the attributes for no great reason, and I'm not interacting with that in the registry of attributes. I only interact with that in the context of a signal.
Yep. So, okay, cool. Alright, I will, continue to work on that prototype, and apologies, it's taking me frickin' forever, but, eventually, you'll have some code to look at.
Sale next week. Or actually, no, not next week.
