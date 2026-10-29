SIG: Semantic Convention Tooling
Date: 2026-10-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth (Google LLC)** 01:22 Hey!
How's it going, man?
**Jeremy Blythe** 01:32 Yeah, it's going… I mean…
**Josh Suereth (Google LLC)** 01:34 It's been a while, right?
**Jeremy Blythe** 01:35 Oh, yeah.
It was… There seems to be a busy period around this time of the year.
Hmm.
**Josh Suereth (Google LLC)** 01:42 It's like Black Friday, and yeah, freezes, and…
**Jeremy Blythe** 01:46 I don't know.
**Josh Suereth (Google LLC)** 01:47 Everybody's rushing to launch crap, yeah.
**Jeremy Blythe** 01:53 I mean…
**Josh Suereth (Google LLC)** 01:57 Yeah. Alright.
Oh, did we not meet last week?
Maybe we didn't.
**Jeremy Blythe** 02:05 That's funny.
**Josh Suereth (Google LLC)** 02:06 Okay.
**Jeremy Blythe** 02:09 Yeah, it was a message from the mother, going… like, really late, my time, going, hey, is anyone going to be there? Of course, my answer was, oh, when… I mean, she was asleep, so… there you go.
Yeah. Anyway, whatever.
**Josh Suereth (Google LLC)** 02:27 Still good. Yeah.
So, I want to talk about moving off Serie Yamel.
**Jeremy Blythe** 02:34 Yeah, let's do it.
**Josh Suereth (Google LLC)** 02:36 I wanna do it, yeah.
Let me open up the PR so I can show you the pain.
It's breaking things, and the reason why it's breaking things is also hilarious.
It turns out that we are violating the latest version of the YAML spec in old versions of semantic conventions, and they can no longer parse with Weaver if we move to Sapphire.
Yeah, I can, I can show you. It's one of those deals where we have a, A continuation string, okay?
Where you do, like, a little block.
But, like, the old versions of SemComf had a few malformed YAMLs, according to the latest spec, where that continuation string, you're supposed to still be indented in.
And we have ones that aren't indented in far enough, but parse on some YAML parsers, and not others. And so when we switch our YAML parser, it actually breaks two versions of old semantic conventions before we fix the, like, formatting of YAML.
So, we basically have to change the minimum version of SemConf that Weaver can read, which I think is fine.
But, let me, because I could… there's, there's, there's two issues… okay, let me just present, to… Let's do… Don't share the whole screen.
Okay.
Right.
So, cert.yaml and cert yaml NG are both marked as abandoned now, and so this is just trying to move to Sapphire, okay?
I can show you the changes, and you'll see all the fun, but the main thing we have to talk about is… this… So, it fails on two versions of Semconf.
Right? 126 and 127. It works on all the rest.
And that is where we have those continuation strings that are embedded improperly in 126 and 127, and it got fixed in 128.
So, to some extent, what I want to talk about is just, hey, does anyone have concerns if we move to 128 as the minimum supported version for Weaver?
**Jeremy Blythe** 05:01 Do we want to stop at 128? Like…
**Josh Suereth (Google LLC)** 05:06 I don't… like, this is one where I feel like we shouldn't move it forward until we have to, kind of a thing.
I don't think there's any… Like, we have a test that checks to make sure we can resolve things. I don't… I don't know if we need to… I don't know, you know?
**Jeremy Blythe** 05:25 Yeah, I guess it doesn't matter.
It doesn't matter until it matters, I guess.
**Josh Suereth (Google LLC)** 05:31 It doesn't matter until it matters, right? Yeah.
**Jeremy Blythe** 05:34 Yeah.
**Josh Suereth (Google LLC)** 05:35 Okay, the other thing is, just so you can see this, there is some changes to how things parse.
Because Sapphire is more pedantic, if you will.
So… what you'll see a whole ton of in the CL is lots of end lines showing up, where before there were none.
Why? Because Sapphire, by default, is making sure there's consistency in when end lines show up on all strings. So endlines will basically always show up.
regardless of how you specify the string. In CERDYAML, you could actually determine Through a convoluted means, whether or not someone uses the pipe syntax, or the, you know, arrow syntax, or if they put a raw string.
Okay?
In this one, it's more consistently putting the end line stuff.
So, oh, but yeah, the other thing that you're seeing is just instead of CERDYAML, we used CERD Sapphire, and then the third change that this had to do was instead of using actual CERDYAML structures in our… Types, right, for annotations and crap, we're using cert.json now.
So those are kind of, like, the three main differences, is basically there's lots of end lines where there used to be none, which we can decide if we want to trim them. Like, if we want Weaver to trim all strings. I'm okay with that. I think that's a mistake, though. I think let's just add the slash N, and if people need to trim in their Jinja template's cool. But it will actually change… like, how semantic conventions are generated and crap, potentially, if trims are missed. So this could be breaking. I need to run the nightly on it.
and then, there's the problem of… This is also now YAML compliant to a particular version of the spec. I think it's, like, 1.2 of YAML.
And… like I said, old versions of SemComp were not YAML 1.2 compliant, but now they are.
**Jeremy Blythe** 07:50 We should make sure that's in the release note, then.
**Josh Suereth (Google LLC)** 07:54 Yes, yes, I'll add it to the release notes. And I can fix… I can fix the test to make sure that we don't have bugs here, but I just wanted to make sure that we're all okay with that, like, before I push this through.
**Jeremy Blythe** 08:09 Makes sense to me.
**Josh Suereth (Google LLC)** 08:11 Okay, cool. It's also kind of fun because we don't have to do these translations between JSON values and YAML values now.
I don't know if you remember us doing that.
Okay, cool.
**Liudmila Molkova** 08:26 I… I kinda wanna see how… how it will break downstream.
I mean, we can merge, and we'll see regardless.
**Josh Suereth (Google LLC)** 08:38 We… okay, are you okay if we merge and then… and then, revert if it's too problematic?
**Liudmila Molkova** 08:44 Yeah, because, like, if we… if we… decide that that's a good way. We will merge it as is anyway, right?
Because of the new lines. That's what I… But I'm worried.
And…
**Josh Suereth (Google LLC)** 08:59 Here's another example of, like, our test data in this YAML, if you look.
This… this demonstrates the problem that it can't parse. Do you see how examples here just had the at, like, right there?
In line with examples, and you're no longer allowed to do that, it has to be indented.
**Liudmila Molkova** 09:22 Oh, so it could be… Oh, and this is the 127 problem.
**Josh Suereth (Google LLC)** 09:28 This is the 127 problem here.
**Liudmila Molkova** 09:30 I see, okay.
**Josh Suereth (Google LLC)** 09:31 Yeah.
Which we fixed, because someone went through and linted all the YAML files.
**Jeremy Blythe** 09:40 Probably unintentionally, but…
**Josh Suereth (Google LLC)** 09:43 Right.
So yeah, I am a bit nervous about breakage with all the slash lines, Ludmila, I agree. Okay, so if you're all comfortable with this, I'll update it to pass tests today.
We'll merge it, we'll do a nightly check.
And then we'll fix the nightly check in some fashion, either by issuing downstream fixes to put trims.
Or, if you want, I can try to consistently trim. I just… that makes me nervous.
I feel like that's… I'd rather have the slash N, and deal with it downstream, then trim everywhere, because what if you want that slash fin? You know what I mean?
**Liudmila Molkova** 10:22 Yeah, and I mean, in the age of AI, it's easy to send fixes downstream.
**Jeremy Blythe** 10:30 I think also the argument that we're now compatible with a certain version of the YAML spec.
is totally fine.
**Josh Suereth (Google LLC)** 10:40 Yes.
Sapphire also probably allows us to configure this in some fashion, I just didn't have the brainpower to figure it out.
And I didn't have the brainpower to argue with Claude and Gemini to figure it out.
So…
**Liudmila Molkova** 10:56 You should've just made them argue with each other, why do you need for this?
**Josh Suereth (Google LLC)** 11:02 You guys go figure this out. Tell me what you decided. Yeah.
**Liudmila Molkova** 11:08 I agree with you both.
**Josh Suereth (Google LLC)** 11:11 Alright, that's… that's kind of the big thing. I think, I was looking through, actually, where is it? We'll go here.
the big, like, security vulnerabilities for TLS and stuff, I think we're actually up to date.
I don't know if we need to cut a release, but I think, I was looking through our dependencies and, like, what Dependabot thinks we need to upgrade.
This Rust TLS OpenSSL, do you know if this is related to the vulnerability? Let's see.
Because this isn't the TLS keys, I think our TLS keys were updated.
**Jeremy Blythe** 11:46 You… where is it? It's in… WebPKI… what's that library?
**Josh Suereth (Google LLC)** 11:54 WebPK routes, yeah.
**Jeremy Blythe** 11:56 Yeah, if… That needs to be updated.
**Josh Suereth (Google LLC)** 12:02 I thought that one… I was looking, and I don't see a security vulnerability reported against us, so I think it was updated?
**Jeremy Blythe** 12:10 Okay, maybe they already are.
Yeah.
**Josh Suereth (Google LLC)** 12:12 Yeah, because I was also looking through our security vulnerabilities detected here.
Which, that one… That one we need to do… that's just moderate. Yeah, the severe ones are gone, right?
**Jeremy Blythe** 12:31 Okay, yeah, maybe we just needed to… merge some of those dependables, then, or renovate.
**Josh Suereth (Google LLC)** 12:38 I went through and merged all the renovates first, and then I looked to see if we had any alerts, so…
**Jeremy Blythe** 12:42 Okay, so he probably did it.
But we could…
**Josh Suereth (Google LLC)** 12:45 I think so. We can check code scanning. These are things we should probably fix, by the way. I don't know if you've seen these. This is, We basically grant write permission at the job level, instead of at the, Or, sorry, we grant it at the entire workflow level instead of on a specific job, apparently.
So that's just moving where we give write permissions to. So for, like, the PR stale bot thing, we only have to grant write permissions in the… particular step.
that actually writes the PR, not in all of the stages, and that's a new security thing that we have to do, so if somebody adds a job, it doesn't get permissions it doesn't need, that kind of crap.
**Jeremy Blythe** 13:28 Yeah, I did a bunch of these the first time around.
**Josh Suereth (Google LLC)** 13:31 I… I… yeah, I was gonna throw… throw something out. I don't have any quota on GitHub on my personal account, so I was gonna throw Gemini at it with work… work quota.
**Jeremy Blythe** 13:41 Yeah, makes sense.
**Josh Suereth (Google LLC)** 13:43 Okay, cool.
I don't have it… I don't know if you guys want to talk about anything else, that's literally the only thing I wanted to talk about, and we're done with that. So, should we talk about release planning or anything?
**Jeremy Blythe** 13:59 There was one thing I threw in.
**Josh Suereth (Google LLC)** 14:02 Oh.
**Jeremy Blythe** 14:02 It would… might be interesting, there's a pull request.
It's something we're doing… now that… now that your tests… the verification is so… is… becomes more and more and more important, right? Because we're not writing the code anymore.
How do you know the tests are any good?
And so there's this thing… That I'm sure you know about, which is the… the mutants.
Where it just… it modifies things a little bit in your code to see if your tests are actually going to catch that you've turned a less than to a greater than, and things like that.
So it mutates the code a little bit, and then… so it's like, how good are your tests, right?
And there's a nice… it's a 1970s thing. But anyway, there's, a really nice Rust Library Cargo Mutants that's been around for a while. So, there's a pull request in there.
which introduces it with a… with a… something that is… comes from the agent's MD, So that when you're creating a PR, before you make the PR, you can… you can do a mutance check over your Diff.
Just to see if your tests are actually, you know.
Decent test from a mutant perspective, right?
**Josh Suereth (Google LLC)** 15:21 Oh, you're putting in knowledge, nice, yeah.
**Jeremy Blythe** 15:23 And I added some… in this one, there's an example just for We The Diff.
where it found a couple that were wrong in Weaver Diff. Just as an example, I threw them into this one, but really then what we could do is go to… go through crate by crate.
So I did it on live check, I haven't submitted it.
I did a life check, and it found, like.
60 things that needed fixing, and… I think we… we just owe it… we owe it to the AI to make its, to make our tests better, I guess.
**Josh Suereth (Google LLC)** 15:52 Well, the way I think of it is, we're putting verifiable, independent checks to make sure we can trust the AI.
**Jeremy Blythe** 15:59 Exactly.
**Josh Suereth (Google LLC)** 16:00 So… The more we have that, like, it can't lie to us, and that help it, like, raise its quality, the better.
**Jeremy Blythe** 16:08 Yeah,
**Josh Suereth (Google LLC)** 16:10 I approved it, I like it.
**Jeremy Blythe** 16:11 Okay, so then we can go crate by crate, so I might do that, and then you'll see a bunch of PLs for each crate.
**Josh Suereth (Google LLC)** 16:20 Cool.
**Jeremy Blythe** 16:21 I'm in on that.
The other thing I was wondering… is… where we are, because I haven't been keeping up for the last few weeks, where we are with having the Semantic Conventions library.
into V2.
**Liudmila Molkova** 16:41 Semantic Conventions Library.
**Jeremy Blythe** 16:44 you know.
**Liudmila Molkova** 16:45 in…
**Jeremy Blythe** 16:46 OpenTelemetry Semantic conventions that… from there.
**Josh Suereth (Google LLC)** 16:49 Mainline Semantic Conventions repo, yeah.
**Jeremy Blythe** 16:54 It's not released as V2 yet, is it? We're still working on converting it.
**Liudmila Molkova** 16:58 Yeah. Oh, by the way.
I… I have a bunch of PRs I'll send you, Josh, to… to approve.
Or comment on, because, there is this V2 entities problem, and it's related to this front.
But… We… no, we don't have… Semantic conventions converted to V2.
But there are just a few more… things to convert, and then it's fully compatible. So, like, if you do minus minus V2 output, then It would produce pretty much what we wanted to produce.
Regardless of the definition language.
version.
**Jeremy Blythe** 17:50 So… Is there a plan to publish the package.
as a V2 package.
And a V1, so that we can… so people who are dependent on it could be dependent on a V2 package.
**Liudmila Molkova** 18:08 There is a plan. We still need to figure out the Hotel I.O. story.
But I have a prototype.
or that would publish it initially as GitHub Artifact, release artifact.
**Josh Suereth (Google LLC)** 18:27 Nice. And then we can figure out how to pull that. I like it.
**Liudmila Molkova** 18:31 Yeah…
**Jeremy Blythe** 18:33 What do you do internally?
Let me just make a GitHub artifact, and then the manifest references to the download directory.
**Liudmila Molkova** 18:43 And I can show you how the release… would look like… It's been a while. I don't know what's going on here, but I'm just calling the publish, I guess, and adding them to release artifacts, and post-release workflow. Or no, not in post-release, it should be… During the release.
**Josh Suereth (Google LLC)** 19:20 Yeah.
**Jeremy Blythe** 19:21 But that will be a.
**Liudmila Molkova** 19:22 Oh, I think that, yeah, the way to make it work is to automate release process more.
**Jeremy Blythe** 19:30 Right.
**Josh Suereth (Google LLC)** 19:31 Yeah.
**Jeremy Blythe** 19:36 Because I think once that… once we get that, I'm gonna switch my… Company over to… pointing at V2, and then we'll… we'll… we'll move every… all of our internal definitions to V2.
And everything will be V2.
**Liudmila Molkova** 19:52 Oh, excuse me.
**Jeremy Blythe** 19:52 the only thing I'm waiting for.
So we're end-to-end V2.
**Liudmila Molkova** 19:56 Why? Oh, because you don't want to check out the SemConfrepo.
**Jeremy Blythe** 20:01 Doctor.
**Liudmila Molkova** 20:03 Oh, I see. And you don't want to provide the pass to some control for the definition schemas.
**Jeremy Blythe** 20:09 Right.
**Liudmila Molkova** 20:10 For some reason.
**Jeremy Blythe** 20:10 Just to get the package.
**Liudmila Molkova** 20:14 But then… you would need to provide this registry pass over right until we actually publish it on the schema URL.
**Jeremy Blythe** 20:24 Yes.
**Liudmila Molkova** 20:25 And this might take a bit longer, because we need to.
**Jeremy Blythe** 20:28 I guess that's one from the brain.
What's the bit longer, do you think?
**Liudmila Molkova** 20:35 So… The bit longer is that we need… at least figure out how to publish the new one on Autel.io.
**Jeremy Blythe** 20:49 Okay.
**Liudmila Molkova** 20:49 This should be easy.
But… we wanted to change the schema URL format a little bit.
And this needs a spec change.
And they think Joshua.
**Josh Suereth (Google LLC)** 21:02 Going to take it.
**Liudmila Molkova** 21:04 Yeah.
**Josh Suereth (Google LLC)** 21:05 I was, and I dropped it. Yeah, I can pick that up.
I have… I have that, the OTEP around it that is still not approved, like, or merged, so I don't know if I should do that first, or just start making spec changes, because we kind of already… you know what I mean?
We're kind of already there.
**Liudmila Molkova** 21:24 Yeah, where the… the OTAP is about fidgeted Semantic Conventions, right? And this can… it's… I feel it's… it's orthogonal. It's just the spec change based on the OTAP we have merged.
For your tab, we had a discussion on the TC call, and people were like, do we need an ATEP for this, if it's just in the semantic conventions?
a PR, that's totally fine.
So Semantic conventions control how things are federated.
**Josh Suereth (Google LLC)** 21:56 Okay.
Right, right, right. Okay, yeah, because the… the OTEP is just… It's funny, though, because the Federation OTEP, we're actively doing, and your OTEP, we haven't finished the specification or are doing yet for publishing.
Like, your OTEP is the schema, and then my OTEP was the thing. So, like, the thing we're actually doing is not approved or merged, and the thing we haven't done is approved and merged.
Okay, I had it backwards. Anyway, cool. Yeah, I can, I can, I can make that change. Awesome.
**Liudmila Molkova** 22:36 Thank you.
Yeah.
So, but… The way to make semantic conventions properly compatible with V2 is to fix the entities.
**Josh Suereth (Google LLC)** 22:54 Yeah, so what is up with us here?
**Liudmila Molkova** 22:58 So, the story is that I… I don't know if it was intentional, or it looks like just an oversight, that… Oy… when we have an entity in V1, And we convert it to V2.
We validate the entity against V1, and we accept whatever was there.
After it's converted in V2, and we don't validate things again.
And… It's been a while, I don't remember what happened there, but essentially what I'm trying to achieve is that we do not accept V… Two entities without identity attributes.
**Josh Suereth (Google LLC)** 23:49 That… that makes sense. Yeah, I was… so this was actually… I wasn't sure… This was intentional, it wasn't an oversight, but it is horrible. This was because we had so many entities that did not have identifying attributes in Semcov that I was just allowing them, initially.
And they would be rejected or, like, flagged later, was the idea.
But I'm on board with doing this and just making them hard errors. I think that's better.
So…
**Liudmila Molkova** 24:18 Yeah, and we only have just a few left to fix.
So, good, that's the way we did it.
**Josh Suereth (Google LLC)** 24:28 Oh, so this is after you convert V1 to V2, then you also check, right?
**Liudmila Molkova** 24:34 And I hope it's a test.
I hope this is a test code, because why would it have a hard-coded thing?
**Josh Suereth (Google LLC)** 24:41 It is in modests.
**Liudmila Molkova** 24:43 Okay, good.
**Josh Suereth (Google LLC)** 24:47 Entity missing identity… yeah, this all looks good.
I'm gonna approve this now, because this makes sense to me.
Cool.
Alright, so that goes through, and then… what else do we have here?
**Liudmila Molkova** 25:09 More fun… oh, this one is trivial, so we… Trying to remember… So when you… Or if… Fine.
Oh, when we def… in the definition schema.
We had note as, required… well, not required, not optional.
And it defaulted to an empty string.
And then it was not possible to override the parent node.
Saying, okay, this does not apply here.
And…
**Josh Suereth (Google LLC)** 25:49 Gotcha.
**Liudmila Molkova** 25:50 The proposal is to differentiate them, but then… It actually does not change anything for the output.
Because we deseralyze, if not empty, anyway.
**Josh Suereth (Google LLC)** 26:02 Yep.
Oh, that's cool. So this gives you the ability to kind of blank something out.
**Liudmila Molkova** 26:12 Yeah.
**Josh Suereth (Google LLC)** 26:13 Okay.
**Liudmila Molkova** 26:14 And we have this ability for… some of the things, or maybe we had it on V1, but somehow some… something slipped, and… Somewhere it doesn't work.
**Josh Suereth (Google LLC)** 26:27 Yeah, this looks good. I'm gonna approve it as well. Okay.
And then, once those are merged, I can do my third YAML fix, which will break everything dramatically across all the codebase, because of all the stupid YAML changes to JSON.
And I'll get that out.
Is there… are these the last two things for V2, then? For Zemcov?
**Liudmila Molkova** 26:48 No. There is one more that I started typing and didn't finish, and… This one, we might need to have a discussion, and I… I'm really sorry, I didn't prepare, and I forgot the context a little bit, so we'll need to find out together. So remember the problem with annotations?
**Josh Suereth (Google LLC)** 27:08 Yeah.
**Liudmila Molkova** 27:08 that we Had annotations, not merging.
And you said they are merging. They are, but they are merging… for definitions. So, like, if I reference…
**Josh Suereth (Google LLC)** 27:20 Oh, God.
**Liudmila Molkova** 27:21 a nice.
**Josh Suereth (Google LLC)** 27:21 contribute.
**Liudmila Molkova** 27:22 definition, then they are merging.
But then, if I… Add things in the refinement.
then all the hell breaks loose. It's not just we don't merge them.
We actually… it's… it's undeterminist… well, it's… it's unstable, I think.
Because…
**Josh Suereth (Google LLC)** 27:42 it…
**Liudmila Molkova** 27:44 How we do this is that we resolve all the attributes at the same time.
Regardless if they are refinements or the… They are originals.
And then… It's okay for the string properties, but when you need to merge, you need to know the order in which they were defined. So, you take the definitions, then you merge in the parent attributes, and then you merge the refinements.
And unhappy way would be to actually Have them ordered, first resolve.
The signal definitions, and then… Resolve the refinement attributes. And that's what this one is trying to do.
And turns out we had some interesting things with lineage because of it, because lineage has the same problem.
That you… the order matters.
And there are some changes in the expected schema because of it, but it's only for the lineage.
**Josh Suereth (Google LLC)** 29:00 Yep.
Oh, God. Okay.
You know, I have to jump to another meeting, but, I think this is my final sign.
that we have to implement the resolution algorithm on V2.
like… where we have to decompose the resolve to not go from V2 to back to V1, and vice versa, where we actually make resolution be V1 or V2.
To solve this, because we… the problem is we erase all knowledge of what you're saying here. And I think that's what's leading to the… inconsistency, right? Because when we do the resolution algorithm, we don't frickin' know any of the things you're saying.
Because we're just making this weird, giant table of doom, right?
Okay. Did you… did you already, try to solve this in code?
**Liudmila Molkova** 30:04 Yeah, and I think it's… it's solving it. I don't remember how, though. Oh, well, I mean, I remember that it makes the order Predictable, so we resolve the signal definitions before the refinements.
**Josh Suereth (Google LLC)** 30:24 I see. So you're basically ordering the unknown, unresolved attributes before you actually resolve them?
I will take a look at this and see. If you think this is… this is good, I… I feel like… how do I want to phrase it?
I'm okay accepting this if we think it's good, and it's not gonna cause unknown other things, because it might be just ordering as all we needed, but this is the straw that's breaking the camel's back for me with the resolution algorithm. That thing is getting too… Too unwieldy.
To where I want to actually make it be, like, we have a dedicated V2 behavior, right?
**Liudmila Molkova** 30:59 Yeah, I… my impression of AI doing this work… The code, and me trying to understand what it did, and what's going on, is that it's so convoluted that it's too hard to understand.
**Josh Suereth (Google LLC)** 31:15 Yeah, yeah, which is why I want to decrease.
**Liudmila Molkova** 31:17 Compose it. Yeah.
**Josh Suereth (Google LLC)** 31:18 Yeah.
**Liudmila Molkova** 31:19 Yeah.
let's then maybe decompose it. I… like… we can solve this problem, but, like, it's not a burning bug that we have. We need to solve it by stability, but, like, it's better to spend a couple more weeks on the resolution algorithm.
**Josh Suereth (Google LLC)** 31:40 Okay.
Alright, I will, I will kill… Arbilla.
your PR, we should do, and I will kill the existing algorithm and start, thinking about a new one, and make that. So first, I'll do the third YAML thing, because I think that's actually important for stability, because we'll actually have a YAML standard we're on, and then I'll, I'll work on that next, is the thing I focus on.
**Liudmila Molkova** 32:08 Awesome. Thank you.
**Josh Suereth (Google LLC)** 32:10 Okay.
Alright.
I will see you.
I gotta…
**Liudmila Molkova** 32:14 I got…
**Josh Suereth (Google LLC)** 32:15 jump. Sorry, guys.
**Liudmila Molkova** 32:16 Yeah, I also need to jump. Sorry, Jeremy.
**Jeremy Blythe** 32:18 Bye.
**Liudmila Molkova** 32:20 Thanks.
