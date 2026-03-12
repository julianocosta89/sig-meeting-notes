SIG: Semantic Convention Tooling
Date: 2025-08-13
Duration: 41 minutes
============================================================

## Zoom Recording Transcript

**Jeremy Blythe** 01:10 Hello.
**Josh Suereth** 01:14 Hey, how's it going?
**Jeremy Blythe** 01:17 Yeah, it's going….
**Josh Suereth** 01:27 Ugh, … Oh, … student validation.
**Jeremy Blythe** 01:35 I tried to figure out what was going on with that, … sharing the room.
Error message.
But I didn't really get very far. I just got very confused, actually.
**Josh Suereth** 01:52 Heh.
The, … the way schema validation works is fun. I don't know who else is coming, by the way, so I don't know if you want to get started. We could do a little bit of triage while we wait, what do you think?
Okay.
… So, for next release, I think we need to look through some of the bugs that came in.
Do they automatically come into this? I think they do, right?
**Jeremy Blythe** 02:25 I never know.
**Josh Suereth** 02:27 Deprecation of a new member is when attribute is deprecated.
**Jeremy Blythe** 02:31 Yeah, that's new.
**Josh Suereth** 02:33 We are also needing to explicitly upgrade all the new members, but if we don't, the members will still show their responsibility.
This is actually a pretty… this is a pretty decent feature request. I think we could do this in Weaver.
What do you think?
**Jeremy Blythe** 02:48 When we deprecate an attribute, we need to also explicitly deprecate But we… The members will show… With their original stability.
**Josh Suereth** 03:00 Yeah, so you'd have, like, a deprecated annuity where a member is considered stable.
So, I'm wondering if, when you deprecated a new, we should just make sure everything is marked as deprecated.
It's just, it's weird otherwise, you know?
**Jeremy Blythe** 03:19 Right.
Yeah, because you're deprecating the entire thing.
Yeah. Yeah, it just… it doesn't make sense, yeah.
**Josh Suereth** 03:28 So, I'm gonna say this is an enhancement… I might say this is a good first issue, what do you say?
**Jeremy Blythe** 03:34 Yeah, it's probably not too bad.
**Josh Suereth** 03:37 Yeah.
In terms of status, … Should we call this ease of use?
It's not really getting started.
….
**Jeremy Blythe** 03:55 It's ease of use, because you can achieve it, but you have to go and edit your files and put in more stuff, right?
**Josh Suereth** 04:00 Okay.
Yeah.
Okay, then we have, … Output of Weaver Registry Resolve drops empty fields. This was on purpose, right?
**Jeremy Blythe** 04:17 Yeah, I thought… Wasn't that… didn't Lib Miller do that, like….
**Josh Suereth** 04:21 Trying to read the resolver format as just looking for required fields which are not present. Oh, oh, oh, oh, oh, oh, interesting.
If you have a brief which is empty.
An empty string. It's a required field.
So, I think, really, what we need to do here is if we're going to require brief to be specified, it can't be an empty string. We actually don't verify it's not an empty string.
We require it, but we don't say that it has to be non-empty.
**Jeremy Blythe** 04:53 That's where you get, commit messages that are just the full stop.
**Josh Suereth** 04:57 Yup.
Yep, … I'll just comment that. I think we want to enforce… That, … Brief is a non-empty string.
in practice here. … Does this… Any other values besides?
Free.
So… 2, 3, evaluate some… Serialization piece… resolution.
Restrictions.
Specific.
Okay.
I'm gonna mark this as a bug, actually, because it seems… … if we… I think… I think it's absolutely bug if we serialize something and can't deserialize it because of our serialization rules.
So Okay.
I'm also gonna mark this as to consider for next release, because I think this might be something we want to, … We might want to get on relatively quickly.
Okay.
Alright.
What else do we have?
Replace conditionally required with requirement level and conditions. I'm pretty sure we discussed this one before.
And I don't think we made a decision, and I… yeah, we can get quorum before we look at that one again. Alright, last thing I wanted to do… Because I think that's all the new ones that were there.
Do we have any issues that are in here that are not in there? Let's take a quick gander.
No, they all made it. Okay, good.
….
**Jeremy Blythe** 07:04 Technically, I should have made an issue for that, thing I put in the Slack.
For the, error message.
**Josh Suereth** 07:11 Oh, yeah, actually, you should, you should. I was looking at that today, so I wanted to… actually, in relation to this, I was looking at it.
**Jeremy Blythe** 07:18 Okay. So….
**Josh Suereth** 07:22 … this is a fun one.
We're gonna briefly talk about this. Guess what I found? This has been failing, right?
Do you know why it's failing?
**Jeremy Blythe** 07:34 Notice causing failures in doc tracks.
**Josh Suereth** 07:38 I looked into it.
**Jeremy Blythe** 07:40 So….
**Josh Suereth** 07:41 Readme.markdown is used by both GitHub and RustDoc.
The README.MD file in the base directory of a crate is used in that crate's documentation.
When you do RustDoc generate. RustDoc does not understand Pound a note, or pound warning, or anything like that, right?
I found an RFC from, I think, 2 months ago.
For Rust.
To say, hey, let's support these.
**Jeremy Blythe** 08:13 Right.
**Josh Suereth** 08:15 And there was apparently a discussion 2 years ago that said, we're not going to do this.
No, 5 years ago.
**Jeremy Blythe** 08:24 Okay.
**Josh Suereth** 08:25 that said, that when they opened the thing to, hey, say, fix it, and two years ago, they decided not to fix it, and they just added, like, the syntax extension that kind of doesn't really work well in GitHub, in my opinion, but works fine for RustDock.
And so I'm… I'm a little grumpy about this one.
Because it just… it just doesn't make sense. But I… anyway, I thumbs up this issue, I think we should thumbs it up and kind of talk through it. Apparently GFM already, … yeah, everyone's saying, oh yeah, we already have a way to do this.
….
**Jeremy Blythe** 08:59 This funny feeling that one of the first requests I ever did for Weaver.
I… Deleted the note.
**Josh Suereth** 09:10 Yeah.
**Jeremy Blythe** 09:11 And then… Laurent was like, no, don't delete the note, you can put this thing in.
To have the rust.
the Rustock, like, ignore it or something, there was I wish I could….
**Josh Suereth** 09:23 We'd look into how to do that, then?
If you can find that, that'd be good, and add that to the PR.
Because I'm more annoyed that Rust decided not to support this, given that it got merged into, like, all the Markdown parsers and things.
**Jeremy Blythe** 09:40 Hmm.
**Josh Suereth** 09:43 Anyway… So that, that's blocking, the dock update CL from Labila. … The other thing that I noticed, … oh, Tamil?
This dependency bump is broken, the ZIP dependency bump is broken, saffr dependency bump is broken, and PROSS dependency bump is broken.
**Jeremy Blythe** 10:06 So I'll tell you what, tell you what, I went to the bottom of the list, and I was looking at the Sappho… I was looking at that one, right? So I opened a new branch.
I'm gonna sort out these bumps, found the error.
It has to do with… the… It now more accurately finds the beginning and the ending of the blocks.
the YAML block.
Which is great, it's an improvement, but then it just means that one of our tests is failing, because previously it would say the block starts and ends on the same line. Don't know why. Anyway….
**Josh Suereth** 10:37 No.
**Jeremy Blythe** 10:38 So, the test can be improved, and then I'm like, okay, so I need to just check the output, and that's when I discovered that I wasn't getting the error messages anymore, because the whole point of that section was in order to be able to draw the nice, output with the… with the underline, saying, like, somewhere in this block, you've got a problem with your….
**Josh Suereth** 10:59 So….
**Jeremy Blythe** 10:59 And then I went, oh my god, why has that disappeared?
**Josh Suereth** 11:03 I see.
**Jeremy Blythe** 11:05 Oh, did we just break this? Because, like, every error message is just….
**Josh Suereth** 11:09 is everything.
**Jeremy Blythe** 11:10 to be version 1 or version 2, and it's neither.
**Josh Suereth** 11:13 I… yeah, I… that… that… that I'll work on fixing quickly, then. Please open a bug for that. Prost is also somewhat concerning. Prost, I think, is the, … RPC stuff, which, it's only for our dependencies.
**Jeremy Blythe** 11:28 Yeah.
**Josh Suereth** 11:29 If I remember right….
**Jeremy Blythe** 11:31 that as well. I think what we're doing… we're actually importing to… we're importing too, where we should actually… we should… I forget what you call it, like, we should reuse the….
**Josh Suereth** 11:43 Prost that's coming in from the library that's using Prost, right? So we're actually importing two Prosts into our key, into our tree.
**Jeremy Blythe** 11:51 Where if we just do a reuse from wherever else it is, I got partway through that.
As well.
**Josh Suereth** 11:57 Yeah, I see, because of how we're pulling in OTLP, gotcha.
**Jeremy Blythe** 12:01 Gotcha.
So if we do a reuse somewhere….
**Josh Suereth** 12:05 It's… it's… we have a diamond dependency, that's fun.
**Jeremy Blythe** 12:08 There you go.
**Josh Suereth** 12:10 Zip, I forget what this one was, I think it was super trivial. I was… I was going from top to bottom on these, by the way.
or I was trying to prioritize the ones that I thought were most impacting to users, but I just look at the feature, like, what's… what's the feature? Do we need it? Not super urgent, but yeah, it'd be nice to fix it. So this one, I think, was… yeah, it's the audit.
So, they are now, … Yeah.
Why?
**Jeremy Blythe** 12:43 Yeah, I saw that and I went, oh, I'm gonna ignore that, maybe Josh will do it.
**Josh Suereth** 12:47 Yeah, this one I can do. This is a… entries, we don't care about that. It's a new license, but I think it's actually an approved license, it's just one of these other stupid things. … Why are you giving me the lawn card entry things?
**Jeremy Blythe** 13:07 This is, like, the most annoying, ….
**Josh Suereth** 13:12 Syntax here.
**Jeremy Blythe** 13:14 Good entries for WASI, wonderful.
**Josh Suereth** 13:17 … Come on, give me the actual thing that you denied.
This key will bring me up to future updates.
Here's the error.
**Jeremy Blythe** 13:28 you know.
**Josh Suereth** 13:28 EZIP 2.
So we're rejecting BZIP2, because I think what happened was BZIP changed their license from something that is acceptable to, like, bzip the license.
And, or they updated the version of the license they use.
**Jeremy Blythe** 13:47 Hmm.
**Josh Suereth** 13:48 So it's something stupid like that, I'll look into it, and if we have to do an exception with CNCF, we can, but we… we have to hold off on this until we know the license is acceptable for us.
So, yay.
… That was what that one was.
And then the other one I was looking into, and this one is actually somewhat significant, … All those error messages we get for doing the JSON schema?
**Jeremy Blythe** 14:15 Yep.
**Josh Suereth** 14:15 They are horribly broken, when we pull in… let's just do test, that might be an easier one to see.
with the bump from .30 to .32, because we're using an unstable JSON schema thing, basically, they changed the name of the enums.
Honest?
**Jeremy Blythe** 14:36 They've added, … so… because this came up… when I was doing the Safir thing, I also bumped the JSON schema thing, so any of… And the one-offs.
Now have a… they now have this context thing.
**Josh Suereth** 14:54 Okay.
**Jeremy Blythe** 14:55 So we just have to update the plain enum, it's an enum with, like, with members, or whatever you call it?
**Josh Suereth** 15:02 Yeah, so hopefully that's not too bad to fix, but what I was going to do was I was going to bump this version at the same time I fixed the error messages.
**Jeremy Blythe** 15:11 what I was wondering, and I didn't, like, I just went, oh, I'm just gonna put curly bracket dot dot, right? But… What I was wondering is whether there's actually something in that context that would be helpful for this problem that we've got.
**Josh Suereth** 15:23 So if you're looking at the problem.
**Jeremy Blythe** 15:25 Because the issue is that we have this any of that's at the very top for 1 or 2, and so you get this any of right at the beginning, but maybe the ENEOF actually has a bunch of extra context in.
It might help with the problem, though.
**Josh Suereth** 15:37 Oh, yeah, okay, cool.
**Jeremy Blythe** 15:40 You know what I mean?
**Josh Suereth** 15:41 I'll take a look at both of those, then.
Okay.
**Jeremy Blythe** 15:45 So, they are kind of all… They all kind of roll together in a strange way.
**Josh Suereth** 15:51 Well, not in a strange way, I think, that's… it's not necessarily by design, but it's not surprising to me.
You know.
That it's all kind of related.
Cool. So… I think… that's that… I actually… yeah, so that was my topic on schema validation, and what to do there. … The one thing I was thinking of doing for the schema validation errors in this, like, Zephyr thing was basically, generating two JSON schemas, one for raw V1, and then one for versioned, and basically… We try to parse everything. When we get a failure, we check the YAML document to see if the version tag has been specified, and if so, we validate with the versioned one. Otherwise, we validate with the other one. That was what I was going to do initially, but if this context thing solves it, I'll just do that.
**Jeremy Blythe** 16:55 Yeah, I was, like… I started doing some really gross things, like, oh, maybe it's got groups in there somewhere? That might be a hint that we're, like, version, like… and then, I don't know, I've started to feel really bad about that, so….
**Josh Suereth** 17:11 No, I mean, we're using a lot of magic to make this all work, so it's not surprising to me that, like, error messages get ugly, because literally what we're doing is really ugly.
**Jeremy Blythe** 17:21 So, making it so that the ugliness is kind of wrapped and special-cased is better.
**Josh Suereth** 17:28 Yeah.
But we should probably, when we're ready, add the version as required. So, if you don't specify version, you get a warning.
**Jeremy Blythe** 17:39 Right, yeah.
**Josh Suereth** 17:40 Are we, ….
**Jeremy Blythe** 17:42 Are we thinking about doing a tool or a command that will take your version 1 and transform it into version 2?
actually make you new files that are in V2 format.
**Josh Suereth** 17:56 Yeah, that's… that's… that's a possibility. I… once… so, the next thing I've been working on is actually the V2, resolve schema.
So when you do Weaver Resolve, I've been working on that, to have that dump V2 instead of V1, and defining what that looks like. When that's done, I think we could have a dash dash version 2 that just requires everything in version 2.
Because we'll have a version 2 output, right?
**Jeremy Blythe** 18:25 Yo, I mean, sorry, I meant… I give it my… Move… Closed.
In YAML.
And I have a new command in… Weaver that says.
take my YAML files and turn them into version 2 YAML.
**Josh Suereth** 18:43 Oh, oh, oh, gotcha.
**Jeremy Blythe** 18:45 Like, the… what's the, the, the, the Rego thing does that. It's not REGO, it's the OPA… is it OPA?
**Josh Suereth** 18:54 Yeah, yeah, yeah.
**Jeremy Blythe** 18:55 You can say, hey, make my stuff version 2, or whatever.
**Josh Suereth** 19:01 Honestly, we could probably do that. Yeah.
Yeah?
….
**Jeremy Blythe** 19:06 I think that'd be useful, because there's a lot of stuff out there in the world, right, that's already V1.
And it'd be a quick way to get… It's a quicker way to… for us to… translate things.
Like, I would 100% use that for my library of stuff that I've got.
work.
**Josh Suereth** 19:32 Yeah, I think, if I remember right, the way I designed it, that tool would be really easy to write, too.
Because I believe… all the V2 stuff has a 2v1.
… No, I don't have 2V2 from V1.
We'll put that as a ticket. We'll open a ticket as an enhancement, and have that as something we'll do.
**Jeremy Blythe** 20:00 I'm getting a little bit of, … What? Python 2 to 3 feelings, but, you know.
**Josh Suereth** 20:05 Yeah.
Well, those are just all the techniques to make going from V1 to V2 easier that you have to build, so….
**Jeremy Blythe** 20:12 Yep.
**Josh Suereth** 20:13 Yeah, regarding V2 schema, that was the other topic I wanted to have. I don't want to take too much time, because we're kind of light, so I'd say we, take a little break and not run long.
… But, for V2 schema, what I've been working on is actually the… going from V1 to V2, but I've been focused on the Resolve schema, not on individual files.
**Jeremy Blythe** 20:38 Yep.
**Josh Suereth** 20:39 And then, I think if I get that done, doing the tool that you suggest would be pretty easy to add as a secondary thing.
But what I'm running into is, I… the approach I'm taking is when I run into a concept that doesn't translate from V1 into V2, I just drop it.
The other thing is lineage.
You know how we track lineage of where things were, where they were adapted and all that?
I'm not sure what to do about lineage in the New World.
I kind of want to kill it. Not kill it, I should say. I kind of want to have a… this came from V1, and that's what it looked like in V1, and then a… here's the V2 lineage, and we'll do a new thing for V2. But all lineage is V1 lineage, because we… We first convert V2 into V1 things, then we calculate lineage, and then we dump it. So, lineage is somewhat problematic.
What I might do initially is do a V2 conversion.
where the lineage is still V1 lineage, and then… do a second CL that updates all the lineage stuff, like, independently.
**Jeremy Blythe** 21:57 How is the lineage stuff actually useful?
**Josh Suereth** 22:00 We use it in our dock generation a good bit, so….
**Jeremy Blythe** 22:05 Okay.
**Josh Suereth** 22:06 for example, I am generating, say, Javadoc, right?
And I want to link to the definition of a attribute. But that attribute comes from a library I depend on. I look at the lineage to see if that… where… where to link to.
To say, this came from this other group.
We actually use it to do references to our registry, so we look at the lineage to say, oh, this came from an attribute registry. We actually might not need that at all in V2 for Semconv, but in multi-registry, I think it'll be important. Because you could say, cool, multi-registry, their docs are at this URL.
And I can generate links to docs in that URL using the lineage to say, okay, this attribute came from over here, just link to that doc, or link to that library.
**Jeremy Blythe** 22:58 No. Yeah.
I see.
**Josh Suereth** 23:00 … Yeah, ironically, we'll need it less in Semcov.
from V2, but we'll need it more in multi-registry.
… What was the other thing? Oh, right.
The other thing is the attributes registry. So, in V2, We have attribute definitions and attribute references, and there are fields in references that are not in the definition.
Okay?
**Jeremy Blythe** 23:29 Okay.
**Josh Suereth** 23:30 In Resolved Registry, we have a catalog of attributes, and then we have the registry of groups.
So, there's a thing called a catalog, which is just a list of all attributes, and then a thing called groups, which is the… List of all the groups.
groups… only have references in Resolved Registry in V1.
And an attribute definition has everything within it.
Okay? So if I have a span that has a sampling relevant attribute.
and that sampling relevant attribute references some other attribute, the catalog will have two attributes. One marked as not sampling relevant, one marked as sampling relevant.
Okay.
I want to change this in some fashion.
Because, what I want to do is just take that attributes group we have and dump it over.
But this means all of those, like, extension things around signals, so, like, whether it's identifying or descriptive on entity.
**Jeremy Blythe** 24:32 Right?
**Josh Suereth** 24:33 The entity group would have, like, a vector for, identifying attributes and a vector for descriptive.
And then for span, should we have, like, a sampling relevant attributes in an other attributes section?
**Jeremy Blythe** 24:48 You know, like….
**Josh Suereth** 24:49 that's… I'm starting to look at that, because when I make this catalog.
I either get all of the concepts bled together in the same catalog, and I have attributes showing up 5 or 6 times, or I need to find a way for those concepts to be part of the signal itself.
**Jeremy Blythe** 25:07 seat.
And so how do you… If the attribute is showing up multiple times, how do you reference the correct one?
I don't.
Sure. Oh, they're showing up… you are referencing the correct one, but they're showing up multiple times in the catalogue.
**Josh Suereth** 25:24 They're showing multiple times in the thing, that's not necessarily the problem, it's more, every single attribute will have to understand if it's sampling relevant, instead of just the ones used in spam.
**Jeremy Blythe** 25:34 Oh, I see.
Oh, I see, because you're in the… Right.
Something relevant isn't… isn't… field on… attribute reference only. That's what you said at the beginning. I get it.
**Josh Suereth** 25:50 Yeah.
**Jeremy Blythe** 25:52 … And then… In a way, you were altering the attribute, because you're now applying that Field.
It's been kind of stung.
So what are you proposing?
**Josh Suereth** 26:13 What I'm proposing is that, I might make changes to what entity and span and things look like, so that some of these override things, show up there.
The, so, like, sampling relevant, right?
We might actually have a sampling relevant and other attributes field and span, instead of Having attributes, and then on each attribute, you say, this is sampling relevant true.
**Jeremy Blythe** 26:42 Right, it's like you would put a map.
In the… that belongs to the span that says.
Or just, yeah, or just a list of… Exactly. Something relevant.
**Josh Suereth** 26:56 Yeah, something….
**Jeremy Blythe** 26:57 Exactly. To the span, not to the….
**Josh Suereth** 27:00 Yeah, where things get weird is requirement level.
So, requirement level is specific to a signal.
So, every single attribute does have a requirement level when it's used in a signal.
**Jeremy Blythe** 27:19 Yep.
**Josh Suereth** 27:20 But when you define an attribute, you don't need to define it at a requirement level.
**Jeremy Blythe** 27:25 But you can, which I find weird. Like, when I'm defining an attribute that's just off in the world floating on its own, why does it have a plan?
**Josh Suereth** 27:33 Pretty sure you can't in V2. Let me check and see what I did there. I thought I took that out in V2.
**Jeremy Blythe** 27:39 Because that was one of my comments I think I made, was that it was just about the… It was about the, … It was in the comment, actually, and you fixed it.
**Josh Suereth** 27:49 Because the… so the… I think it was… originally, it was written, like.
**Jeremy Blythe** 27:54 If I don't… If I don't specify the requirement level, I get recommended as the default. Oh, you're right, yeah. You inherit the requirement level, because it's defined against the attribute.
in, like, you know, in V1, in the attribute group.
**Josh Suereth** 28:10 Yeah.
**Jeremy Blythe** 28:11 just got attributes floating around. I've never… I never really understood… I just always go, oh, required.
**Josh Suereth** 28:19 Yeah, we don't… we… we don't have, let me check and make sure… Common Fields does not have requirement level, yeah. So we have stability, but we don't have requirement level anymore in V2.
**Jeremy Blythe** 28:31 Okay, actually, not yet.
That fixes that.
**Josh Suereth** 28:36 Well, it does, except I need to now figure out how to make the resolved registry and the catalog, right? Where am I going to store requirement level? Do we store it on the sig… like, should we have a signal that has required attributes, recommended attributes, optional attributes, or should we have the signal have a list of attribute references That have the required conditional things right on the signal itself.
But I, I actually… I need to talk to Lawrence about this, but I'm pretty sure I want to have attributeRef on the, on the signal.
Because I think it's actually code gen relevant.
And I think it's only relevant to that, signal.
So, having the signal understand the, requirement level directly, I think, is totally fine.
But I am significantly changing the resolve schema doing this.
**Jeremy Blythe** 29:33 So you're suggesting to move… move that out of AttributeRef?
Up into the signal.
**Josh Suereth** 29:39 No, no, no, I'm suggesting that I would move it into AttributeRef. Like, today… V1 catalog registry stuff.
AttributeRef is literally just an ID. That's it. It's a straight integer, and it just points at… Points there. And then attribute definition has everything in it.
**Jeremy Blythe** 29:58 Yep.
**Josh Suereth** 29:59 What I'm proposing is there'll actually be signal, there'll be attribute ref, which has requirement level, and maybe other things specific to the signal.
And then there will be the attribute ID that goes into the catalog.
Another way to phrase it, I actually think, we might… we might not need… a catalog Definition that's different than the raw file definition going forward.
**Jeremy Blythe** 30:36 Why do we pull the attributes?
Out into the catalogue.
If you look at it, really, the things that you can change on an attribute when you're referencing it belong to the signal.
**Josh Suereth** 30:51 Yeah.
**Jeremy Blythe** 30:52 All of the things we change are… I'm saying, I'm using this attribute, but I'm changing it in this way, in this signal, in this signal only.
**Josh Suereth** 31:00 there's a to-do on V2 we haven't gotten to, which is actually… it's not true that the signal is the only thing that can change stuff. So, what we do in SEMCOM, and what, like, the reason why Laurent does this is we'll have… define the raw attributes, right? Then we'll define a group of attributes, just an independent group that says, here's a group of attributes, with overrides.
Requirement levels, all that kind of junk.
Then we'll say, okay, this span uses that shared group. This other span also uses that shared group.
And can I add more attributes to the shared group if needed in that signal?
We haven't figured out how to do that in V2, so V2 right now is currently super verbose.
… but I think… I actually think, now that we're kind of talking through it, I could probably make the Resolve schema look exactly like the V2 schema today, without those references and things, and everything will be fine. So I might go forward with that and put a proposal out, because You know, the attribute catalog we had before.
the new V2 schema has just that one attribute segment, with all the attributes in it. I'm just taking multiple files and putting it in one. It seems like it'll fit well. Same with signals, like, I actually think this is gonna be a lot more trivial.
for us to put that together. And then if we want to expand the definition.
YAML format, to have this, like, notion of grouping and sharing and stuff.
Basically, the difference between that and what we resolve is the resolved is pure, raw, verbose, and the original has some shared intermediate stuff.
**Jeremy Blythe** 32:45 Okay.
**Josh Suereth** 32:47 I think I need to do it now for it to make more sense. Yeah, I'll have to show it to you, I think, but the, … I think, … Shh, okay.
So, plan… to resolve.
Let me look.
Simple V2 definition schema.
We have no, … Sharing right now, for example.
Extends.
So… so… schema from the two definition is basically just loop and stuff.
Two files.
Yep. Okay.
… Can I show you? I don't… I don't know if I have the brainpower right now to show you anything, I'm kinda… toast from last night. So apologies. We had a… Just a family emergency I had to deal with. ….
**Jeremy Blythe** 33:52 Hmm.
**Josh Suereth** 33:53 I might… I might call it here, unless you had something else you want to talk about, if that sounds good, because I think this gives me enough to figure out how to start working on V2.
**Jeremy Blythe** 34:02 Yeah, no, I don't have anything. I've been struggling to find time to, … to work on stuff, so I've been trying to pick at little bits and bobs, but, ….
**Josh Suereth** 34:14 I think we're all kind of in that state right now, so I… and honestly, like, the way I've seen OpenTelemetry move.
We make a lot… we get a lot done in the fall, we get a lot done in the spring, and then basically summer and winter seem to be hiatuses of people's availability. So, yeah.
**Jeremy Blythe** 34:31 That's.
**Josh Suereth** 34:32 surprised me.
**Jeremy Blythe** 34:33 It's just crazy at work right now, too.
That's my main thing, just soaking up all my time, but….
**Josh Suereth** 34:40 I have the same problem right now. I have, like, it's been a real struggle to get enough free time, because I have a bunch of urgent things that popped up.
**Jeremy Blythe** 34:50 It'd be really interesting to… I don't know if you've ever… this before in this group, so it'd be really interesting to know how you use… ….
**Josh Suereth** 35:01 So she's good.
**Jeremy Blythe** 35:02 not necessarily OpenTelemetry, but, like, OpenTelemetry in the context of Weaver at Google, right? I'd be really interested to know From you, like, your… your personal experience of using… Sure. We're using tools.
At some point.
**Josh Suereth** 35:19 Yeah, yeah, we're still, we're still, … I should show you what we do. We have a whole system that we built before Weaver existed.
**Jeremy Blythe** 35:29 ….
**Josh Suereth** 35:30 And so we still have to maintain that sucker, and so there's still a question about, like.
when these two can converge, because the other thing about Google, you know, it's a large enterprise, and the secret is, it's not like there's one technology that rules the world at Google. Even if there's one named technology, where we say, oh, everyone uses this for metrics.
That one thing has basically 12 different things underneath it that all have the same name, but are subtly different. And so, yeah. That's… I can talk to you specific… maybe about more specifics, I'll have to run it through the team to see what we want to talk about publicly, but ….
**Jeremy Blythe** 36:11 Yeah, I understand.
I just think it'd be interesting to hear more, Like… The challenges of using this at… You know, in huge enterprise settings.
**Josh Suereth** 36:26 Right, yeah.
**Jeremy Blythe** 36:29 … I think….
**Josh Suereth** 36:31 Whatever.
**Jeremy Blythe** 36:32 I don't….
**Josh Suereth** 36:32 You've seen this, by the way.
Oh, sorry, go ahead.
**Jeremy Blythe** 36:36 Just the more that I'm… So, I'm trying to spread the word more across my little company of, like, we're, like, 2,000 people.
So we're not tiny, but, so I'm trying to get more of this going in other groups, and just, like, … really want them to be model-driven, and I'm gonna work with Laurent some more on, like.
There may be some opportunity to use some of the work that he's been doing for… … And all of that.
But, like, just trying to, like, plug… plug it all together with, as… as you kind of… as I get away from my comfort zone of my own little, sort of, part of the org.
And you go further and further out. Anyway, I just… Yeah, they both have similar challenges.
**Josh Suereth** 37:24 If you haven't used Google Cloud, I'll show you one thing that we have. This puts us at a little bit of an advantage. So we actually advertise, for example, all the metrics that are created across Cloud.
So, if I go to Services A to B, we can pick a random… oh, this might take a lot of load, because it's a large page, and … Zoom takes all of my CPU for some reason.
**Jeremy Blythe** 37:47 Well, of course it does.
**Josh Suereth** 37:50 Yeah, I'm not sure what it's doing, but okay, so, like, Google Actions. This is Google Assistant Smart Hub Actions, great. We create metrics from this. We have documentation that says, here's the metric name, right?
Here's the description of that thing, and this is the latency that you expect for it to arrive, so it tells you, like, the sample rate, it tells you how long it might take to show up, and then it tells you the set of labels and what they mean.
Now we have typed labels as well, right? But, like, unlike, … OpenTelemetry type labels are a bit different than us, and we also have, these types for the metric.
Open telemetry.
has types for metric points, but when we say a metric has a type, we mean it always has that type, and OpenTelemetry doesn't quite mean that.
**Jeremy Blythe** 38:45 Hmm.
**Josh Suereth** 38:45 For example, that's, like, one of the things we were just recently talking through. Anyway… But yeah, so this is all documented, and anytime a team wants to expose metrics for people to use on cloud, they have to go through this, and we use this to… you see there's, like, a beta, there's a.
**Jeremy Blythe** 39:03 that she gave.
**Josh Suereth** 39:04 Oh, what's that? Alpha, Beta, I think we have deprecated and GA, let's see. Yeah, AI Platform, this is… most of this is beta, because it's all kind of newish, you know.
**Jeremy Blythe** 39:15 ….
**Josh Suereth** 39:16 maybe BigQuery has some….
**Jeremy Blythe** 39:19 Yeah, GA one, he just signed it on.
**Josh Suereth** 39:21 well, they have a lot of beta metrics, but yeah, they have some GA metrics. These are the ones that, like, you can rely on. … And yeah, this is, like, one thing we advertise so people know, like, what metrics they can depend on, which ones they can see changing. If you have a GA metric, we guarantee we don't change labels, it's all the policies that you expect, right? We implemented all this before Weaver, and we're looking at Weaver like, man… How are we gonna line all this up?
**Jeremy Blythe** 39:47 Yeah, right.
**Josh Suereth** 39:48 So… Yeah, the Weaver-related aspects of that, you know, there's… when you look at one of these things, this may or may not be using OpenTelemetry behind the scenes.
That's… that's, like, an implementation detail, but when it… when it is, like, using Weaver as a goal, like, to make sure that it uses Weaver, that it's enforced and validated that way, but we have to have something slightly more flexible, so they're still figuring out how, like, can the Weaver model support everything we need here, and how does that interact? Or do we do, like, a… … We have a model that generates the Weaver model, which generates the OTEL code.
That kind of stuff. Yeah.
**Jeremy Blythe** 40:28 But if you're.
**Josh Suereth** 40:29 If you ever interact with this, like, it's… this is one reason I got very excited by Weaver, because this is, … it's critical we maintain it, right? Like, this… I cannot emphasize the importance of metrics and stability for the health of your whole company.
**Jeremy Blythe** 40:47 Yep.
**Josh Suereth** 40:47 But it's also something that I don't think enough people pay attention to, or think is important. So, like, the whole Weaver effort, I thought, was, … It's… it's pretty cool. I'm excited.
**Jeremy Blythe** 40:58 Got it. Yeah. Okay, that makes sense.
**Josh Suereth** 41:02 Yeah.
Alright, I'm gonna drop,
**Jeremy Blythe** 41:04 Yeah, yeah, thanks for that.
**Josh Suereth** 41:06 Yep.
**Jeremy Blythe** 41:07 Alright, have a good day.
**Josh Suereth** 41:08 You too.
